---
name: runbook
description: Write or update the operator runbook for a project in ~/Runbooks. Use when a project is created or materially changed (new command, service, flag, or failure mode), before pushing to GitHub, when a push hook reports a stale runbook, or when the user says "runbook", "update the runbook", "/runbook".
---

# Runbook

One runbook per project in `~/Runbooks`, named `<Project>_Runbook.md`. It is the
operator's copy — what Carey types, not what the docs claim.

## Rules

1. **Verify, never transcribe.** Every command in a runbook must have been run,
   or read out of a live service file, script, or `--help`. Documentation lies;
   `systemctl cat`, `ps -eo args=`, and the script itself do not. A command
   copied from a README without checking is the failure mode this file exists
   to prevent.
2. **Real invocations only.** The flags actually used, not the full CLI surface.
   If Carey always runs `ffwd pipeline daily --backend local-qwen
   --summarize-limit 500`, that line goes in — not `ffwd pipeline --help`.
3. **Name credentials, never values.** "Key lives in `~/.config/restic/env`" is
   right. The key itself is never written to a runbook.
4. **Link, don't copy.** In-repo README/CHEATSHEET/DESIGN files get linked. A
   copied section drifts and then lies.
5. **Audience split.** Machine-specific paths, personal hacks, and recovery
   procedures belong here. What a stranger needs to install and start the thing
   belongs in the repo README. If operator detail is found in a public README,
   move it here and say so.

## Procedure

1. Read `~/Runbooks/_TEMPLATE.md` for the section order.
2. If the runbook exists, read it first and update in place — preserve what is
   still true, rewrite what changed, delete what is now wrong.
3. Gather evidence for the project before writing:
   - `systemctl cat <unit>` and `systemctl list-timers` for anything scheduled
   - the entrypoint scripts themselves, read — never executed to discover flags
   - config files at their real paths
   - `git log --oneline -10` for what recently changed
4. Fill every section. An empty section means the evidence was not gathered.
5. Set `last_verified` to today. Add the repo's absolute path to `repos:` — the
   push hook matches on it.
6. Add or update the one-line entry in `~/Runbooks/00-INDEX.md`.
7. Commit in `~/Runbooks` with a message naming what changed.

## Push validation

When invoked before a push, or after the push hook blocks: diff what is being
pushed against the runbook. Anything that changed a command, a service, a path,
or a failure mode gets reflected. Then bump `last_verified` and commit.
