# Vendor Privacy Review Skill

Systematic analysis of vendor data processing agreements (DPAs) and privacy notices for compliance issues, red flags, and inconsistencies.

## Overview

This skill provides comprehensive privacy and data protection review of vendor documentation against GDPR, CCPA, and EU Standard Contractual Clauses requirements. It analyzes 14 key dimensions to identify compliance gaps, risks, and problematic provisions.

## Usage

```
/vendor-privacy-review
```

Then provide vendor documentation via:
- File upload (PDF, Word, etc.)
- Web URL to DPA or privacy notice

The skill will analyze the documents and produce a structured compliance report.

## What It Analyzes

### 14 Analytical Dimensions

1. **Data Processing Scope** - What data is collected, for what purposes, with what limitations
2. **Data Sharing & Subprocessors** - Who has access, where are they located, notification requirements
3. **High-Risk Processing** - AI training, biometrics, tracking, automated decisions, ad sharing
4. **Processing Limitations** - Carve-outs, exclusions, vendor controller claims
5. **Liability & Warranties** - Caps, indemnification, disclaimers, risk allocation
6. **Controller vs Processor Roles** - Role clarity, alignment with actual control
7. **International Transfers** - SCCs, adequacy decisions, geographic restrictions
8. **Retention & Deletion** - Retention periods, deletion procedures, backup handling
9. **Breach Notification** - Timeline, information requirements, cost allocation
10. **Audit Rights** - Frequency, scope, cost, restrictions
11. **Data Subject Rights** - DSAR support, timelines, fee structures
12. **Security Measures (TOMs)** - Specific controls, certifications, encryption standards
13. **Non-Standard Provisions** - Unusual definitions, unilateral changes, IP claims
14. **Document Consistency** - Cross-check DPA vs privacy notice contradictions

## Output Format

### Executive Summary
- Overall risk assessment (Low/Medium/High)
- Top 3-5 critical issues
- Quick recommendation (approve/negotiate/reject)

### Detailed Findings
For each dimension:
- Assessment with precise citations
- Risk level for that category
- Recommended actions

### Standards Comparison
- GDPR compliance gaps (with article citations)
- CCPA compliance gaps (with section citations)
- EU SCC deviations (if applicable)

### Recommendations
- Priority fixes
- Negotiation points
- Clarifying questions for vendor

## Key Features

**Precise Citations:**
Every issue includes exact document reference:
- Format: `[Document Type, Section/Clause Number, Title]`
- Example: `DPA, Clause 10.2, Data Subject Rights`

**Critical Eye:**
- Assumes adversarial review posture
- Flags provisions designed to obscure obligations
- Considers regulatory perspective, not just business convenience

**Comprehensive Coverage:**
- Both DPA and privacy notice analysis
- Cross-document consistency checking
- Comparison against regulatory standards

**Actionable Output:**
- Specific negotiation points
- Risk-prioritized findings
- Questions to ask vendor

## Use Cases

- **Vendor onboarding** - Assess new vendor privacy terms before contract
- **Annual reviews** - Check if vendor has updated terms unfavorably
- **Regulatory compliance** - Validate vendor compliance with GDPR/CCPA
- **Risk assessment** - Identify high-risk processing or liability gaps
- **Contract negotiation** - Arm legal team with specific issues to negotiate
- **Audit preparation** - Document vendor privacy posture for auditors

## Technical Requirements

**Document formats supported:**
- PDF
- Microsoft Word
- Web pages (via URL)
- Plain text

**Regulatory frameworks:**
- EU General Data Protection Regulation (GDPR)
- California Consumer Privacy Act (CCPA)
- EU Standard Contractual Clauses (all modules)

## Example Analysis Scope

A typical vendor review covers:

**Data Processing Agreement (DPA):**
- Processor obligations
- Subprocessor management
- Data subject rights support
- Security requirements
- International transfers
- Breach notification
- Audit rights
- Liability and indemnification

**Privacy Notice/Policy:**
- Data collection and use
- Sharing and disclosure
- Retention periods
- Individual rights
- Security measures
- Contact information

**Cross-checks:**
- Do DPA and privacy notice align?
- Are there contradictions?
- Do vendor's practices match stated policies?

## Red Flags the Skill Identifies

- Overly broad data collection
- Undisclosed subprocessors
- Hidden controller claims
- Inadequate breach notification timelines
- Restricted audit rights
- Vendor disclaiming security responsibility
- Asymmetric liability protection
- No international transfer mechanisms
- Vague "industry standard" security claims
- Unilateral amendment rights
- IP claims over customer data

## Author Background

Built for privacy professionals, DPOs, legal counsel, and compliance teams conducting vendor privacy assessments. Reflects deep knowledge of:
- GDPR Article 28 processor requirements
- CCPA service provider obligations
- EU Standard Contractual Clauses
- Common vendor contract pitfalls
- Regulatory enforcement priorities

## License

MIT
