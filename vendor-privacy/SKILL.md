---
name: vendor-privacy
description: Systematic analysis of vendor data processing agreements (DPAs) and privacy notices for compliance issues, red flags, and inconsistencies. Use when conducting vendor privacy assessments, reviewing DPAs or privacy policies for vendor management programs, comparing vendor terms against GDPR/CCPA requirements, or when user mentions "vendor privacy review", "DPA analysis", "/vendorreview", or uploads vendor privacy documentation.
---

# Vendor Privacy Review

## Overview

Conduct systematic privacy and data protection reviews of vendor DPAs and privacy notices. Identify compliance issues, red flags, contradictions, and gaps against GDPR, CCPA, and EU Standard Contractual Clauses. Output structured analysis with precise document citations.

## Analysis Framework

Execute a comprehensive review across 14 analytical dimensions. For each dimension, identify issues and provide precise citations in format: `[Document Type, Section/Clause Number, Title]`

Example citation: `Privacy Notice, Section 8.3, Subprocessors` or `DPA, Clause 10, Data Subject Rights`

### 1. Document Intake

**CRITICAL: If you cannot read or access any provided document (upload failed, link inaccessible, format unreadable), STOP immediately and inform the user. Do not attempt analysis without full document access. Do not guess or improvise.**

Read all provided documents (uploaded files or web links). Identify:
- Which document is the DPA vs. privacy notice/policy
- Document version dates and effective dates
- Scope and applicability statements
- Whether documents reference each other or contain conflicting terms

### 2. Data Processing Scope

**Analyze:**
- What data categories will be collected and processed
- Stated processing purposes
- Broad or unusual processing activities outside normal vendor services
- Vague language that could permit scope expansion

**Flag:** Overly broad data collection, undefined "related purposes", lack of data minimization

### 3. Data Sharing and Subprocessors

**Analyze:**
- Complete list of subprocessors vs. vague references vs. no mention
- Geographic locations of subprocessors
- Whether prior notice/consent is required for new subprocessors
- Notification mechanism and timeline for subprocessor changes

**Flag:** Undisclosed subprocessors, blanket authorization without notice, offshore processing without clear transfer mechanisms

### 4. High-Risk Processing Activities

**Scan for these specific activities:**
- Sharing data with advertisers or marketing partners
- Law enforcement data access provisions
- AI/ML model training using customer data
- Precise geolocation tracking
- Biometric data processing (facial imagery, fingerprints)
- Automated decision-making or profiling
- Cross-context behavioral advertising
- Aggregated/de-identified data reuse
- Employee monitoring capabilities

**Flag:** Any high-risk processing not clearly disclosed or consented to, especially if buried in fine print

### 5. Processing Limitations and Exclusions

**Analyze:**
- What processing activities are explicitly excluded from DPA scope
- Carve-outs for vendor's own purposes vs. customer purposes
- Whether vendor claims controller rights for certain data
- Restrictions on customer's audit or oversight rights

**Flag:** Broad exclusions that undermine DPA protections, hidden controller claims

### 6. Liability Limitations and Warranty Disclaimers

**Analyze:**
- Liability caps and their adequacy given risk
- Indemnification obligations (who indemnifies whom)
- Force majeure clauses that could excuse breach obligations
- Warranty disclaimers that shift security responsibility to customer
- "As-is" provisions for security measures

**Flag:** Asymmetric liability (vendor protected, customer exposed), inadequate caps for data breaches, disclaimers inconsistent with GDPR processor obligations

### 7. Controller vs. Processor Roles

**Analyze:**
- Who is designated as controller (or "business" under CCPA)
- Who is designated as processor (or "service provider" under CCPA)
- Whether role assignments align with actual data control and processing
- Whether vendor claims independent controller rights

**Flag:** Role misalignment, vendor acting as controller but claiming processor status, joint controller situations not addressed

### 8. International Data Transfers

**Analyze:**
- Legal transfer mechanisms cited (Standard Contractual Clauses, adequacy decisions, BCRs, etc.)
- Whether EU SCCs are incorporated or referenced
- If SCCs are used, which module (C2C, C2P, P2P, P2C)
- Geographic locations where data will be processed
- Whether UK/Swiss variations of SCCs are mentioned if applicable

**Flag:** No transfer mechanism specified, outdated transfer tools, processing in high-risk jurisdictions without adequate safeguards

### 9. Data Retention and Deletion

**Analyze:**
- Specified retention periods for different data categories
- Retention justification and legal basis
- Process and timeline for data deletion upon contract termination
- Whether deletion certification is provided
- Backup deletion procedures

**Flag:** Indefinite retention, vague "as needed" language, no deletion procedures, retained data not covered by DPA

### 10. Security Breach Notification

**Analyze:**
- Notification timeline (hours/days after discovery)
- What information must be included in breach notice
- Whether vendor provides incident response support
- Cost allocation for breach response (who pays)
- Whether notification obligation survives contract termination

**Flag:** Excessive notification delays (>72 hours), no detail requirements, customer bears all costs, no post-termination obligations

### 11. Audit Rights

**Analyze:**
- Frequency of permitted audits (annual, ad-hoc, unlimited)
- Scope of audit access (on-site, remote, documentation-only)
- Whether auditor must be pre-approved by vendor
- Cost allocation (who pays for audit)
- Whether SOC 2/ISO certifications substitute for direct audits
- Notice period required for audit requests

**Flag:** Highly restricted audit rights (e.g., only with 90 days notice, only if customer pays, only using vendor-approved auditors), audit rights limited to reviewing third-party reports only

### 12. Data Subject Rights Support

**Analyze:**
- Which party handles data subject access requests (DSARs)
- Whether vendor assists with DSARs or forwards to customer
- Timeline for vendor response to DSAR assistance requests
- Whether vendor charges fees for DSAR support
- Support for other rights (rectification, erasure, portability, objection)

**Flag:** Vendor does not assist with DSARs, charges unreasonable fees, excessive response times (>30 days), limited support only for access requests

### 13. Technical and Organizational Measures (TOMs)

**Analyze:**
- Specific security controls listed in DPA or privacy notice
- Whether TOMs are in a separate exhibit/annex
- Reference to certifications (SOC 2, ISO 27001, etc.)
- Link to security documentation or trust portal
- Encryption standards (at rest, in transit)
- Access controls and authentication requirements
- Incident response procedures

**Flag:** Vague "industry-standard" language without specifics, no certifications, TOMs subject to unilateral vendor changes

### 14. Non-Standard Provisions and Red Flags

**Scan for:**
- Unusual definitions that narrow scope (e.g., "Personal Data excludes IP addresses")
- Unilateral amendment rights (vendor can change terms without notice)
- Automatic renewal with limited termination windows
- Non-compete or exclusivity provisions
- Intellectual property claims over customer data or insights
- Governing law and jurisdiction (especially if non-EU for EU processing)
- Severability clauses that could gut key protections
- Integration clauses that override prior representations

**Flag anything unusual, non-standard, or that shifts obligations asymmetrically to customer**

## Output Structure

Deliver findings in this format:

### Executive Summary
- Overall risk assessment (Low/Medium/High)
- Top 3-5 critical issues requiring immediate attention
- Quick recommendation (approve as-is, negotiate changes, reject)

### Detailed Findings by Category
For each of the 14 dimensions above:
- **[Category Name]**: Brief assessment
- **Issues Identified**: Bullet list with precise citations
- **Risk Level**: Low/Medium/High for this category
- **Recommended Actions**: What to negotiate or clarify

### Document Inconsistencies
Cross-reference contradictions between DPA and privacy notice with citations from both documents

### Comparison to Standards
- GDPR compliance gaps (cite specific articles)
- CCPA compliance gaps (cite specific sections)
- Deviations from EU Standard Contractual Clauses (if SCCs claimed)

### Additional Observations
Any other concerns not covered by the 14 dimensions

## Important Notes

- Always provide precise citations with document name, section/clause number, and section title
- Quote concerning language verbatim when highlighting red flags
- If documents are unclear or ambiguous, note this and suggest clarifying questions for vendor
- Maintain a critical eye - assume adversarial review posture
- Consider regulatory perspective, not just business convenience
- Flag provisions that appear designed to obscure or limit obligations
