---
name: stack-forensics
description: Use when debugging careyaibox's local AI stack — a request is slow, missing, 400ing, or may be hitting the paid API instead of the local model; when asked which model is running, whether a nanoclaw agent or scheduled task fired, or where a hop logs. Covers litellm, llama-server, nanoclaw/ncl, claude-local, FeedForward backends.
---

# Stack Forensics

The addresses. `superpowers:systematic-debugging` supplies the method; this supplies where
to look, so no time goes on rediscovering fixed facts.

## First move, always

```bash
stack-check                    # services, toolchain, model aliases, nanoclaw socket. exit 1 = something failed
ls -t ~/.local/state/stack-check/ | head -3    # nightly run history (07:45 timer), colour stripped
```

Most questions end here. Do not `find /` for any of the paths below — they are fixed.

## The hop map

| Hop | Where it lives | How to see it work |
|---|---|---|
| Claude Code → proxy | `claude-local` sets `ANTHROPIC_BASE_URL=localhost:8000` | `tr '\0' '\n' < /proc/<pid>/environ \| grep ANTHROPIC` |
| LiteLLM proxy | `:8000`, config `homelab/stacks/inference/litellm-config.yaml` | `journalctl -u litellm --since "10 min ago"` → `POST /v1/messages` or `/v1/chat/completions` |
| llama-server (chat) | `127.0.0.1:8080`, qwen3.6-35b | `journalctl -u llama-server \| grep print_timing` — **tokens here = it really ran locally** |
| llama-embed | `127.0.0.1:8081`, nomic-embed-text | same journal, `local-embed` alias |
| nanoclaw agents | `~/nanoclaw`, model alias `nanoclaw-local` | `ncl tasks list`, `ncl groups list`, `ncl dropped-messages list`, `docker logs --tail 200 <c>` |
| FeedForward | `feedforward/llm.py` → `LOCAL_LLM_BASE_URL` (`:8000`), model `LOCAL_LLM_MODEL` (`local`) | `journalctl -u ffwd-pipeline -n 50` |

Reproduce any caller's request without waiting for the caller:

```bash
curl -sS http://localhost:8000/v1/chat/completions -H "Authorization: Bearer sk-local-dummy" \
  -H 'Content-Type: application/json' \
  -d '{"model":"local","messages":[{"role":"user","content":"reply ok"}],"max_tokens":10}'
```

## Facts that look like bugs

- **A local session displays "Sonnet 5".** Claude Code validates `--model` against its own
  catalog before any request leaves the process, so the proxy serves `claude-*` compat
  aliases. The label is the alias; `print_timing` in llama-server is the truth.
- **`local` is a stable alias**, not a model. Swapping models is a one-line edit in
  `litellm-config.yaml`. `local-qwen` names the specific model; `nanoclaw-local` is
  nanoclaw's, and is the only alias with a paid fallback (`nanoclaw-anthropic-fallback`,
  which has never fired — check before assuming a surprise bill).
- **`sk-local-dummy` is a placeholder**, not a leaked key. Real keys live in
  `~/.config/litellm/env` (mode 600) and are injected by systemd `EnvironmentFile`.
- **`--backend claude` does NOT mean the paid API.** `get_anthropic()` passes no
  `base_url`, so the SDK reads `ANTHROPIC_BASE_URL` from FeedForward's `.env`
  (`http://localhost:8000`) and sends `model=ANTHROPIC_MODEL` (`local-qwen`). Both
  backends land on the local model; only `real=True` (Batch API) escapes the proxy.
  Verified 2026-09-09: the 18:00 scheduled run produced 203 llama-server completions and
  litellm's whole journal contains zero `api.anthropic.com`.
- **`--backend gemma` no longer exists** (renamed to `local`, 2026-09-09).
- **`systemctl --user` needs `XDG_RUNTIME_DIR=/run/user/1000`** inside a system unit, or
  user services report phantom "not active".
- **OneCLI is not in systemd.** `pgrep -af onecli`; dashboard is `172.17.0.1:10254`.

## Common mistakes

| Mistake | Instead |
|---|---|
| `find /` for a config | Paths above are fixed; `systemctl cat <unit>` names the real one |
| Concluding "paid" from the model label | Check `print_timing` in llama-server |
| Reading a config to decide what runs | The running process may predate the edit — compare `ps -o lstart` against the file mtime, or just reproduce with curl |
| Inferring a run happened from log shape | `~/.local/state/stack-check/` holds actual run logs |

Fuller detail, including recovery procedures: `~/Runbooks/Local_AI_Stack_Runbook.md`,
`Nanoclaw_Runbook.md`, `FeedForward_Runbook.md`.
