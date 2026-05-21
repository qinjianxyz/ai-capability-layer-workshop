# Interview Memory OS for Link School — deep research memo

I’m treating the uploaded brief as the governing scope: standalone business/product plan, one-cycle v0 wedge, GBrain as knowledge layer, skill graph/process inspiration, and no automated admissions decisions. 

Citations below are the source URLs for the major claims.

---

## 1. Executive recommendation

### Build / narrow / park / kill

**Build, but narrow hard.**

### One-paragraph rationale

Link School should build **Interview Memory OS v0** because the pain is real, the initial wedge is small, and the research supports better structure, calibration, documentation, and year-over-year institutional learning. Structured interviews are consistently favored over unstructured interviews for reliability, fairness, and validity, but admissions-interview prediction remains limited and should not be over-weighted or automated. The safe value proposition is not “AI admissions”; it is **faculty memory, rubric consistency, question improvement, retrospective learning, and next-cycle preparation**. That fits LGPD principles of purpose limitation, necessity, transparency, security, non-discrimination, and accountability, provided Link separates raw identifiable evidence from de-identified canonical memory and keeps any projection layer advisory, aggregate, explainable, and human-reviewed. ([U.S. Office of Personnel Management][1])

### Recommended wedge

**Interview Memory OS v0** for **one faculty team, one program, one rubric, one interview cycle, and one post-cycle retrospective**:

Raw governed vault → source/consent ledger → redaction/de-identification → canonical memory assets → GBrain knowledge base → internal skill graph → advisory projection packet → faculty review → next-cycle playbook.

The product should initially answer questions like: “Which rubric dimensions lacked evidence?”, “Which interview questions produced low signal?”, “Where did interviewers disagree?”, “What edge cases should next year’s team prepare for?”, and “What did we learn that should not be forgotten?”

---

## 2. Decision memo

| Topic                  | Recommendation                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Problem**            | Faculty learn a lot during interview cycles, but the learning evaporates across scattered notes, chats, spreadsheets, recordings, and memory. The immediate problem is institutional memory loss, not decision automation.                                                                                                                                                     |
| **Customer / users**   | Buyer: dean, program director, admissions leader, or Link’s innovation owner. Users: faculty interviewers, admissions operations, committee chair, privacy/legal owner, and a technical/knowledge steward.                                                                                                                                                                     |
| **Why now**            | Structured admissions processes, institutional-data governance, AI retrieval, and AI-risk governance have matured enough to make a small, governed memory layer practical. UNESCO, OECD, and NIST all emphasize human-centered AI, privacy, transparency, traceability, lifecycle risk management, and human oversight—exactly the controls this workflow needs. ([UNESCO][2]) |
| **Status quo**         | CRM/admissions tools manage applicants and decisions; qualitative tools analyze transcripts; Notion/Airtable store notes; generic RAG searches documents. None naturally creates a governed, de-identified, year-over-year faculty-memory system with a skill graph and human-reviewed projection layer. This is an expert inference from the market map below.                |
| **Differentiation**    | The differentiator is **canonical interview memory**, not another CRM. Link’s system should preserve “what faculty learned” as evidence-linked, de-identified, reusable assets: rubric lessons, question-bank lessons, calibration lessons, edge-case logs, and next-cycle playbooks.                                                                                          |
| **Business model**     | First: internal operating system plus facilitated consulting sprint. Later: hybrid productized service for small-to-mid business schools or executive-education programs. Do not sell as predictive admissions software unless legal, validity, fairness, and governance evidence justifies it.                                                                                |
| **Adoption risks**     | Faculty may see it as extra admin; privacy review may block recordings/transcripts; AI outputs may be distrusted; poorly handled de-identification may expose candidates; projection language may drift into prohibited scoring.                                                                                                                                               |
| **Build/buy decision** | **Build v0 internally with lightweight tools; buy commodity components if needed.** Use existing storage, spreadsheets, markdown, and GBrain first. Do not build custom software until the workflow has survived one cycle and one retrospective.                                                                                                                              |

---

## 3. Product spec

### Scope

**v0 must include:**

1. **Raw evidence vault** for identifiable interview notes, transcripts, recordings, rubrics, committee notes, and decision logs.
2. **Source and consent ledger** showing candidate notice version, legal basis, recording/transcription status, data owner, retention period, and vendor exposure.
3. **Extraction/redaction workflow** to convert raw evidence into de-identified canonical memory.
4. **Canonical memory assets**: rubric lessons, question-bank lessons, interviewer-calibration lessons, edge cases, decision-process lessons, retrospective findings.
5. **GBrain knowledge system** for retrieval over approved de-identified memory, playbooks, and skill cards.
6. **Link School interview skill graph**: reusable skills with triggers, inputs, outputs, owner, verifier, and memory-update behavior.
7. **Projection packet** limited to aggregate/process hypotheses for the next cycle.
8. **Faculty review** before any memory asset or projection becomes official.

### Non-goals

v0 should not:

* Admit, reject, rank, or score individual candidates.
* Predict individual candidate performance, “fit,” personality, emotion, or leadership potential.
* Infer protected or sensitive traits.
* Use raw identifiable candidate data in public or unapproved AI tools.
* Replace faculty judgment or committee deliberation.
* Become a general admissions CRM.

These constraints align with LGPD principles of necessity, transparency, security, prevention, non-discrimination, and accountability, and with AI-governance expectations for human oversight, traceability, and risk management. ([Serviços e Informações do Brasil][3])

### User workflows

**Before cycle**

Faculty chair opens the next-cycle playbook in GBrain, reviews last cycle’s canonical memory, pressure-tests the rubric, selects interview questions, and runs a calibration workshop.

**During interview**

Interviewers use a structured note template: question asked, rubric dimension, evidence observed, score if used, confidence, uncertainty, and follow-up probes. The system captures source metadata but does not expose raw data broadly.

**Committee review**

The committee logs edge cases, rationale, dissent, unresolved questions, and evidence references. The log is for consistency and retrospective learning, not automated decisioning.

**Post-cycle**

A knowledge steward extracts patterns, removes identifiers, checks re-identification risk, drafts canonical memory assets, and submits them for faculty and privacy review.

**Next-cycle planning**

The projection layer proposes aggregate hypotheses: weak rubric coverage, low-signal questions, calibration gaps, note-quality issues, and workload risks. Faculty approve, reject, or revise.

### Architecture

**Practical v0 architecture**

```
Raw interview evidence
  → governed vault with restricted access
  → source / consent / retention ledger
  → extraction and redaction workspace
  → de-identification review
  → canonical memory assets
  → GBrain knowledge system
  → Link School skill graph
  → advisory projection packet
  → faculty review
  → next-cycle playbook
```

**What can live in spreadsheets/markdown in v0**

* Interview-cycle registry.
* Consent/source ledger.
* Rubric/question inventory.
* Structured note template, if access-controlled.
* Decision-log template.
* Skill cards.
* Canonical memory assets.
* Projection packet.
* Retrieval test set.

**What later requires custom software**

* Role-based access controls across raw/de-identified layers.
* Automated redaction with human review.
* Provenance graph and lineage visualization.
* Data-subject request workflows.
* Retention/deletion automation.
* Vendor logging.
* Projection evaluation dashboard.
* AI safety tests and audit trail.

This separation follows qualitative-data guidance: keep identifiable, de-identified, and anonymized versions distinct; preserve anonymization logs separately; and document the context, consent, methods, codebooks, and restrictions needed for reuse. ([UK Data Service][4])

### Minimal data model

| Entity                     | Key fields                                                                                                                                                                                                                                                         |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **interview_cycle**        | `cycle_id`, `program_id`, `cycle_year`, `rubric_id`, `faculty_team_id`, `owner`, `privacy_owner`, `notice_version`, `legal_basis_record`, `start_date`, `end_date`, `retention_policy`, `status`, `created_at`, `review_signoffs`                                  |
| **candidate_record**       | `candidate_pseudonym_id`, `raw_candidate_id_vault_ref`, `cycle_id`, `age_category`, `notice_version`, `recording_status`, `transcription_status`, `interview_panel_id`, `data_subject_request_status`, `retention_date`, `raw_access_group`                        |
| **interview_note**         | `note_id`, `cycle_id`, `candidate_pseudonym_id`, `interviewer_id`, `question_id`, `rubric_dimension_id`, `evidence_text`, `score_if_used`, `confidence`, `followup_probe`, `timestamp`, `source_ref`, `redaction_status`, `identifier_flag`, `sensitive_data_flag` |
| **decision_log**           | `decision_log_id`, `cycle_id`, `case_type`, `meeting_date`, `evidence_refs`, `rationale_summary`, `dissent_or_uncertainty`, `unresolved_questions`, `human_decision_owner`, `ai_used_for_summary_flag`, `approved_for_memory_flag`                                 |
| **canonical_memory_asset** | `asset_id`, `title`, `asset_type`, `cycle_id`, `validity_scope`, `deidentified_summary`, `source_lineage`, `confidence_label`, `privacy_review_status`, `faculty_review_status`, `owner`, `version`, `review_by_date`, `supersedes_asset_id`                       |
| **skill_node**             | `skill_id`, `name`, `trigger`, `input_contract`, `output_contract`, `owner`, `verifier`, `phase`, `memory_update_rule`, `source_assets`, `status`, `promotion_history`                                                                                             |
| **projection_hypothesis**  | `hypothesis_id`, `cycle_id`, `statement`, `allowed_use`, `blocked_use`, `evidence_refs`, `assumptions`, `confidence_label`, `falsifiers`, `reviewer`, `decision`, `outcome_check_date`, `result`                                                                   |

### Skill graph

The skill graph is not a bloated prompt library. It is a small map of repeated interview-cycle behaviors that Link wants to make reliable.

| Skill                                   | Trigger                     | Input                                   | Output                               | Owner             | Verifier                | Memory update                      |
| --------------------------------------- | --------------------------- | --------------------------------------- | ------------------------------------ | ----------------- | ----------------------- | ---------------------------------- |
| **1. Cycle intake and governance gate** | New interview cycle starts  | Program, rubric, data types, vendors    | Approved scope and data map          | Admissions ops    | Privacy owner           | Creates cycle record and ledger    |
| **2. Rubric pressure test**             | Rubric is reused or changed | Rubric, last-cycle memory               | Rubric risks and clarification list  | Faculty chair     | Faculty panel           | Updates rubric memory asset        |
| **3. Question-bank calibration**        | Questions selected          | Question inventory, rubric              | Approved question/probe set          | Faculty lead      | Calibration group       | Updates question performance asset |
| **4. Interviewer calibration**          | Before live interviews      | Sample responses, rubric anchors        | Calibration notes and disagreements  | Faculty trainer   | Committee chair         | Updates calibration asset          |
| **5. Structured evidence capture**      | Interview completed         | Notes, rubric dimensions                | Evidence-coded note                  | Interviewer       | Admissions ops          | Adds source-linked note            |
| **6. Edge-case decision logging**       | Committee ambiguity arises  | Candidate evidence, rubric, issue       | Rationale, dissent, unresolved issue | Committee chair   | Second faculty reviewer | Adds edge-case memory              |
| **7. Redaction and de-ID review**       | Raw evidence becomes memory | Draft summary, raw source               | De-identified asset or rejection     | Knowledge steward | Privacy owner           | Updates anonymization log          |
| **8. Canonical memory distillation**    | Post-cycle synthesis        | Notes, logs, retrospective              | Canonical memory asset               | Knowledge steward | Faculty chair           | Publishes to GBrain                |
| **9. Retrospective facilitation**       | Cycle ends                  | Metrics, examples, unresolved questions | Retro decisions and action list      | Facilitator       | Faculty team            | Updates playbook                   |
| **10. Projection packet creation**      | Planning next cycle         | Canonical assets, metrics               | Aggregate hypotheses                 | Knowledge steward | Faculty chair           | Adds projection records            |
| **11. Projection falsifier review**     | Projection proposed         | Hypothesis, evidence, counterexamples   | Approve/revise/block                 | Faculty panel     | Privacy/ethics reviewer | Updates projection status          |
| **12. Next-cycle playbook publishing**  | New cycle preparation       | Approved memory and projections         | Playbook                             | Faculty chair     | Program owner           | Supersedes prior playbook          |

**Process inspiration**

* **gstack office-hours** → use for business/scope pressure-testing: “What is the real decision? What is out of scope? What would make this not worth doing?”
* **Superpowers planning/TDD/verification** → use for implementation discipline: every workflow has acceptance tests, verification checks, and failure cases.
* **Matt Pocock grill-me** → use for unresolved faculty decisions: “What are we avoiding deciding? What evidence would change our mind? What is still ambiguous?”

### Projection layer

**v0 projection model: safe aggregate hypothesis review.**

Allowed projections:

* “Rubric dimension X had weak evidence coverage last cycle.”
* “Question Y produced low signal or generic responses.”
* “Interviewers diverged most on dimension Z; add calibration anchors.”
* “Committee edge cases clustered around motivation vs. evidence; clarify rubric language.”
* “Week 2 had note-quality degradation; adjust scheduling.”

Disallowed projections:

* Individual admit/reject recommendation.
* Individual ranking or “fit” score.
* Protected-trait inference.
* Emotion/personality scoring.
* Black-box leadership, grit, or success prediction.
* Candidate-level risk labels.
* Automated committee decision summaries without human approval.

The comparative EU AI Act guardrail is important even if not directly governing Link School in Brazil: AI used to determine educational access/admission is listed as high-risk, and high-risk systems require risk management, data governance, technical documentation, record-keeping, transparency, human oversight, accuracy, robustness, cybersecurity, and fundamental-rights assessment. ([AI Act Service Desk][5])

### Governance controls

* Purpose register per data use.
* Legal basis per processing activity.
* Candidate-facing Portuguese notice.
* Separate raw vault and de-identified memory.
* Access control by role.
* Human review of all AI-generated outputs.
* No public AI tools for raw candidate data.
* Provenance on every memory asset.
* Retention/deletion schedule.
* Incident-response procedure.
* Vendor/model registry.
* Projection red-line policy.
* Annual review and decommission path.

### Acceptance criteria

v0 is acceptable only if:

1. Every raw source has a ledger record.
2. Every memory asset has lineage to approved sources.
3. Every memory asset passes de-identification review.
4. No GBrain answer about interview memory appears without source links.
5. No system output recommends an admissions decision.
6. Faculty can retrieve last-cycle lessons in under five minutes.
7. At least eight skill nodes are used in a real workshop.
8. The retrospective produces a next-cycle playbook.
9. Privacy/legal owner signs off before live candidate data is used.
10. The projection packet contains only aggregate/process hypotheses.

---

## 4. Research findings

|  # | Finding                                                                                                                                                     | Evidence and source URL                                                                                                                                                                                                                                                                                 | Implication for Link School                                                                                                                        |
| -: | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|  1 | **Confirmed:** Structured interviews are more consistent than unstructured interviews.                                                                      | OPM defines structured interviews as predetermined questions, same order, same rating scale, and same standards; OPM says this gives candidates equal opportunity and improves consistency. ([U.S. Office of Personnel Management][1])                                                                  | Link should standardize core questions, probes, rubrics, and rating anchors before adding AI.                                                      |
|  2 | **Confirmed:** Unstructured interviews have lower reliability/validity and more bias/legal risk.                                                            | OPM’s structured interview guide states unstructured interviews have low reliability, low-to-moderate validity, and susceptibility to legal challenges, while structured interviews have demonstrated reliability, validity, and legal defensibility. ([U.S. Office of Personnel Management][6])        | v0 should focus on interview structure and documentation, not prediction.                                                                          |
|  3 | **Confirmed, with context limit:** Employment-selection meta-analysis favors structured interviews.                                                         | McDaniel et al.’s meta-analysis found structured employment interviews more valid than unstructured interviews for predicting job performance; this is not admissions-specific but supports structure as a general selection principle.                                                                 | Use the evidence as process guidance, not as proof that business-school interviews predict student outcomes.                                       |
|  4 | **Confirmed:** Admissions interviews can be less predictive than grades/exams and may discriminate.                                                         | A medical-school admissions review notes interviews can supplement portfolios but are less reliable/predictive than GPA and national exams, and some interview processes may discriminate by race, gender, or other demographics. ([Perspectives on Medical Education][7])                              | Do not overweight interviews or automate candidate-level decisions.                                                                                |
|  5 | **Confirmed:** Structured or MMI-style admissions interviews can improve reliability, but evidence is still limited.                                        | A five-school medical study found inter-interviewer consistency was generally lower for traditional interviews than MMIs; the systematic review still calls for more research and suggests scaling down interview weight pending stronger evidence. ([Springer][8])                                     | Link can borrow MMI-style discipline—multiple structured stations, clear rubrics, trained raters—without claiming predictive certainty.            |
|  6 | **Confirmed:** Interview design needs explicit competencies, format, questions, rating scales, probes, pilot testing, interviewer guide, and documentation. | OPM’s eight-step guide includes job analysis, competencies, format/questions, rating scales, probes, pilot testing, interviewer guide, and documentation. ([U.S. Office of Personnel Management][6])                                                                                                    | Translate “job analysis” into “program-success/rubric analysis” for Link.                                                                          |
|  7 | **Confirmed:** Local validity studies require defined cohorts, criteria, and predictor quality.                                                             | College Board’s ACES study framework evaluates how admissions measures predict institutional success criteria such as first-year GPA and encourages examining measures alone/in combination. ([ACES][9])                                                                                                | Any future projection or validity work must define outcomes and sample size before making claims.                                                  |
|  8 | **Confirmed:** Qualitative interview data needs planned anonymization, not ad hoc redaction.                                                                | UK Data Service says qualitative richness creates anonymization challenges and recommends planning for direct/indirect identifiers, separate versions, and context-based re-identification risk. ([UK Data Service][4])                                                                                 | Build de-identification into the workflow before transcripts enter GBrain.                                                                         |
|  9 | **Confirmed:** Over-anonymization can destroy usefulness; under-anonymization can expose people.                                                            | UK Data Service recommends balanced anonymization, consistent pseudonyms, clear replacement markers, and a separate anonymization log. ([UK Data Service][4])                                                                                                                                           | Canonical memory should preserve useful patterns while removing candidate-identifying details.                                                     |
| 10 | **Confirmed:** Reusable qualitative data needs context, consent, methods, codebooks, and sharing restrictions.                                              | UNC’s qualitative data package guidance says reusable qualitative data requires documentation of collection/analysis, interview schedules, consent forms, codebooks, and restrictions; sharing is not simply open/closed. ([tdx.unc.edu][10])                                                           | Treat Interview Memory OS as a governed qualitative-data package, not just a notes folder.                                                         |
| 11 | **Confirmed:** FAIR and PROV-O are relevant metadata/provenance foundations.                                                                                | FAIR emphasizes findability, accessibility, interoperability, reuse, rich metadata, qualified references, and detailed provenance; W3C PROV-O defines a provenance ontology for interchange across systems. ([GO FAIR][11])                                                                             | Every memory asset should include source lineage, version, owner, status, and reuse constraints.                                                   |
| 12 | **Confirmed but product-inference:** GraphRAG is relevant for narrative institutional memory.                                                               | Microsoft describes GraphRAG as combining text extraction, network analysis, LLM prompting, and summarization for understanding text datasets. ([Microsoft][12])                                                                                                                                        | GBrain should eventually use graph-like links among rubrics, questions, cycles, decisions, and skills, but v0 can be simpler.                      |
| 13 | **Confirmed:** LGPD requires purpose, adequacy, necessity, transparency, security, prevention, non-discrimination, and accountability.                      | LGPD Article 6 lists these principles for personal-data processing. ([Serviços e Informações do Brasil][3])                                                                                                                                                                                             | The system’s legal design must start from purpose and minimization, not from “what data would be useful.”                                          |
| 14 | **Confirmed:** Legitimate interest is not a blanket basis and requires careful balancing.                                                                   | LGPD allows legitimate interest where fundamental rights and liberties do not prevail; ANPD’s guide says legitimate interest applies to non-sensitive personal data and requires careful case-by-case analysis and a balancing test. ([Serviços e Informações do Brasil][3])                            | Use legitimate interest cautiously for internal process improvement; do not use it for sensitive data or candidate profiling without legal review. |
| 15 | **Confirmed:** Sensitive data, children/adolescent data, and anonymization have special rules.                                                              | LGPD Article 11 restricts sensitive-data processing; Article 14 requires children/adolescent processing in their best interest; Article 12 says anonymized data is not personal data unless reversibility is possible by reasonable efforts. ([Serviços e Informações do Brasil][3])                    | Avoid collecting sensitive traits; if candidates volunteer them, isolate/redact them unless legally necessary.                                     |
| 16 | **Confirmed:** AI governance requires human-centered design, privacy, traceability, risk management, and human oversight.                                   | UNESCO calls for a human-centered approach and warns that unregulated GenAI can leave privacy unprotected; NIST AI RMF uses govern/map/measure/manage; OECD principles require human rights, fairness, privacy, explainability, safety, traceability, and accountability. ([UNESCO][2])                 | Link’s projection layer must be reviewed, source-linked, auditable, and overrideable.                                                              |
| 17 | **Confirmed current status:** Brazil’s AI bill should be monitored but is not the current operating baseline.                                               | The Senate page shows PL 2338/2023 approved in the Senate and sent to the Chamber; the Chamber page shows it awaiting rapporteur opinion in a special committee. ([www25.senado.leg.br][13])                                                                                                            | Current compliance baseline should be LGPD/ANPD plus global AI-governance best practice; monitor PL 2338/2023.                                     |
| 18 | **Expert inference from market sources:** Current tools solve fragments, not Link’s full memory problem.                                                    | Slate, Salesforce, WebAdMIT, Acuity/Casper, Kira, Qualtrics, ATLAS.ti, MAXQDA, NVivo, Notion, Airtable, and enterprise RAG tools each address CRM, assessments, surveys, qualitative coding, or knowledge search, but not this exact governed faculty-memory/skill/projection workflow. See market map. | Build a lightweight internal OS first; integrate or buy components later.                                                                          |

---

## 5. Legal / privacy / ethics checklist

### LGPD gates

**1. Controller/operator roles**

Link School should be the **controller** for admissions-interview data because it determines purposes and means. Vendors that provide storage, transcription, AI, CRM, or analytics should be treated as processors/operators and contractually bound to Link’s instructions. LGPD requires controllers and processors to maintain records of processing operations, especially where legitimate interest is used. ([Serviços e Informações do Brasil][3])

**2. Legal basis by purpose**

Do not choose one legal basis for the whole system. Create a processing matrix:

* Candidate scheduling and admissions operations.
* Interview note-taking.
* Recording/transcription, if used.
* Committee decision logging.
* Internal process improvement.
* De-identified institutional memory.
* Research/validation, if future outcomes are studied.
* AI-assisted summarization/retrieval, if used.

LGPD Article 7 lists legal bases including consent, legal obligation, contract/pre-contract procedures, studies by research bodies with anonymization where possible, regular exercise of rights, and legitimate interest where fundamental rights do not prevail. ([Serviços e Informações do Brasil][3])

**3. Legitimate interest**

Legitimate interest may be plausible for internal process improvement using non-sensitive personal data, but only after a documented balancing test. ANPD emphasizes purpose, necessity, safeguards, transparency, and documented reasoning; it also says there is no one-size-fits-all balancing test. 

**4. Consent**

Consent is likely advisable for optional recordings, transcription, research reuse beyond the admissions process, and any use that candidates would not reasonably expect. Consent should be specific, informed, distinguishable, revocable, and in Portuguese.

**5. Purpose limitation and minimization**

Interview data should be processed only for specific, explicit, communicated purposes. LGPD necessity requires limiting processing to the minimum required for the purpose. ([Serviços e Informações do Brasil][3])

**6. Sensitive data**

Do not design questions that solicit sensitive data unless legal/privacy review says it is necessary. Sensitive data includes data that can reveal racial/ethnic origin, religious belief, political opinion, union membership, health, sex life, genetic or biometric data. If volunteered, route it to redaction or special handling. LGPD Article 11 imposes stricter bases for sensitive-data processing. ([Serviços e Informações do Brasil][3])

**7. Children/adolescents**

If any candidates are under 18, process their data in their best interest. For children, LGPD requires specific and distinguishable consent from at least one parent or legal representative; ANPD has also clarified that children/adolescent data processing may rely on LGPD legal bases but best interest must prevail. ([Serviços e Informações do Brasil][3])

**8. Data-subject rights**

The system must support confirmation, access, correction, anonymization/blocking/deletion of unnecessary or excessive data, portability, information about sharing, revocation of consent, and objection where applicable. LGPD also gives data subjects rights around review of solely automated decisions affecting their interests, which is one more reason v0 should avoid automated decisioning. ([Serviços e Informações do Brasil][3])

**9. Retention/deletion**

Raw candidate records should be retained only as long as needed for admissions operations, appeals/legal defense, audit, or a documented lawful purpose. LGPD Article 16 says personal data should be erased after processing ends, except for legal/regulatory obligation, research with anonymization where possible, transfer under legal requirements, or exclusive controller use with anonymization. ([Serviços e Informações do Brasil][3])

**10. Cross-border transfer**

If raw or pseudonymized candidate data goes to a foreign AI, transcription, storage, or analytics vendor, Link needs an international-transfer basis and safeguards such as adequate protection, contractual clauses, binding corporate rules, certificates/codes, specific consent, or another LGPD Article 33 basis. ([Serviços e Informações do Brasil][3])

**11. RIPD / DPIA**

A RIPD/data protection impact assessment is advisable before live candidate data if any of the following are true: recordings/transcripts, AI summarization, cross-border vendor processing, legitimate interest, possible sensitive data, adolescent data, automated profiling risk, or outcome validation. LGPD allows ANPD to require an impact report and specifies that such a report should include data types, collection/security methodology, safeguards, and risk mitigations. ([Serviços e Informações do Brasil][3])

**12. Security incident response**

The incident plan should be ready before live data. ANPD’s security incident regulation requires controllers to notify ANPD and data subjects when an incident may entail relevant risk or damage; significant-risk criteria include sensitive data, children/adolescents/elderly, financial data, authentication data, secrecy-protected data, or large scale. Communication to ANPD must occur within three working days from controller knowledge that personal data was affected. 

### Candidate-facing transparency

Candidate notice should be in Portuguese and explain:

* Who controls the data.
* What data is collected.
* Whether interviews are recorded or transcribed.
* Whether AI tools assist with de-identified summarization or internal memory.
* What data is not used for automated admissions decisions.
* Legal bases by purpose.
* Retention periods.
* Vendor/cross-border sharing.
* Data-subject rights and contact.
* Optional vs. mandatory processing.
* How consent can be revoked where consent is used.

### What not to send to external AI tools

Do not send to public or unapproved AI systems:

* Candidate names, IDs, contact details.
* Raw recordings or transcripts.
* Raw interviewer notes with identifiable details.
* Sensitive data or protected-trait references.
* Committee deliberations tied to identifiable candidates.
* Admissions outcomes tied to identifiable candidates.
* Consent records or legal documents with personal data.
* Authentication credentials or internal security details.

Approved enterprise AI use could be considered only after vendor review, DPA/operator terms, no-training commitment, logging, access controls, data-region/cross-border review, deletion guarantees, and human review.

---

## 6. Market map

| Alternative                                    | What it solves                                                                                                                                                       | What it misses vs. Link’s need                                                                                             | Build/buy/partner recommendation                                                |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Slate**                                      | Admissions CRM: application management, reading facilitation, decision release. ([Technolutions][14])                                                                | Not designed as a de-identified faculty-memory OS with canonical assets, skill graph, and projection review.               | Use if Link already has it; do not build v0 as a CRM replacement.               |
| **Salesforce Education Cloud**                 | Education CRM across recruitment/admissions, student success, academic operations, AI insights. ([Salesforce][15])                                                   | Broad platform, not interview-cycle memory discipline. Implementation overhead may be too high for v0.                     | Buy only for enterprise CRM strategy; integrate later.                          |
| **WebAdMIT / Liaison**                         | Applicant management, application review, communication, admissions decisions. ([Liaison][16])                                                                       | Focuses on applicant workflow and admissions management, not year-over-year faculty learning.                              | Buy/retain for admissions operations if needed; don’t use as core memory layer. |
| **Acuity Insights / Casper**                   | Situational judgment assessment for people-centered professions; applicant insights from structured scenarios. ([Take Casper][17])                                   | Assessment product, not internal memory, rubric-learning, or retrospective engine.                                         | Consider only if Link wants external SJT-style assessment; not v0.              |
| **Kira Talent**                                | On-demand timed video/written admissions assessments; standardized assessment workflows. ([Kira Talent][18])                                                         | Captures applicant responses but does not solve canonical faculty memory and LGPD-specific de-ID workflow by itself.       | Possible partner/vendor if asynchronous interviews are adopted.                 |
| **Qualtrics**                                  | Surveys, feedback, program evaluations, research/data collection. ([Qualtrics][19])                                                                                  | Strong for candidate/faculty feedback, weak for raw-evidence vault, canonical memory, and skill graph.                     | Use for post-interview feedback surveys, not as core OS.                        |
| **ATLAS.ti**                                   | Qualitative coding, AI-assisted coding, transcription/search, document chat. ([ATLAS.ti][20])                                                                        | Great for research analysis; not a governed admissions workflow or next-cycle playbook system.                             | Use for one-off qualitative analysis if volume justifies.                       |
| **MAXQDA**                                     | Qualitative/mixed-methods analysis, transcription, coding, AI reports, team cloud. ([MAXQDA][21])                                                                    | Strong QDA, but not purpose-built for admissions governance, memory promotion, or projection review.                       | Consider for research-heavy pilots; otherwise too much.                         |
| **NVivo**                                      | Organize/code/query interviews, surveys, audio/video; memos, annotations, collaboration. ([Lumivero][22])                                                            | Powerful research tool, but faculty adoption may be heavy and it does not create skill graph/playbook behavior by default. | Consider only if Link hires a qualitative researcher.                           |
| **Notion**                                     | Wiki, docs, search, project pages, decision pages. ([Notion][23])                                                                                                    | Easy to misuse for sensitive raw data; limited provenance/privacy controls unless carefully configured.                    | Good for de-identified playbooks and skill cards; not raw vault.                |
| **Airtable**                                   | Relational no-code workflows, interfaces, automations, integrations, governance features. ([Airtable][24])                                                           | Useful database layer but not enough for de-ID, LGPD workflow, and AI governance on its own.                               | Good v0 ledger/projection tracker if access controls are sufficient.            |
| **Generic RAG-over-Drive / enterprise search** | Retrieval and grounded answers over enterprise data; Google Agent Search supports RAG over enterprise data with citations and privacy controls. ([Google Cloud][25]) | Retrieval alone does not solve consent, redaction, canonical memory promotion, or red-line enforcement.                    | Useful later as retrieval infrastructure; do not start here.                    |

### Build / buy / partner recommendation

**Build the workflow, buy the commodity tools, partner only where necessary.**

The product is not the vault, spreadsheet, CRM, QDA package, or RAG engine. The product is the **governed process** that turns one interview cycle into reusable, de-identified, evidence-linked institutional memory.

---

## 7. Implementation roadmap

### One-day workshop prototype

**Goal:** Prove that faculty memory can be captured, structured, de-identified, and turned into a next-cycle playbook in one day.

**Morning**

1. Confirm v0 scope and red lines.
2. Map one program, one rubric, one interview cycle.
3. Identify raw sources: notes, questions, rubrics, committee logs, recordings if any.
4. Run a rubric pressure test.
5. Run “grill-me” session on unresolved faculty decisions.

**Afternoon**

1. Create 5–7 sample canonical memory assets from historical or synthetic data.
2. Draft 8–12 skill cards.
3. Create a projection packet with allowed and disallowed examples.
4. Review de-identification risks.
5. Decide v0 pilot owner, timeline, and kill criteria.

**Successful one-day output**

* One source/consent ledger template.
* One raw-vault policy.
* One canonical memory template.
* One rubric lesson asset.
* One question-bank lesson asset.
* One edge-case decision-log template.
* One next-cycle playbook skeleton.
* One projection packet with human-review workflow.

### 30-day pilot

**Objective:** Build the operating skeleton before live data.

Deliverables:

* Data map and legal-basis matrix.
* Candidate notice draft in Portuguese.
* Raw vault and access policy.
* Source/consent ledger.
* Structured interview-note template.
* Decision-log template.
* Skill graph v0.
* De-identification checklist.
* GBrain space with only approved, non-live or de-identified material.
* Retrieval test set.
* Faculty calibration session.

Success metrics:

* 100% of planned data types mapped.
* Privacy owner signs pre-live gate.
* Faculty can use the note template without major friction.
* At least five skills tested in workshop conditions.
* No raw candidate data enters GBrain or AI tools.

### 60-day pilot

**Objective:** Use the workflow during one live or simulated interview cycle.

Deliverables:

* Active source ledger.
* Structured notes captured.
* Committee decision logs captured.
* Weekly quality review.
* Redaction/de-ID queue.
* Initial canonical memory drafts.
* Retrieval tests over approved memory.
* Incident-response tabletop.

Success metrics:

* ≥90% of interviews have structured notes.
* ≥80% of notes link evidence to rubric dimension.
* All AI-assisted summaries are human-reviewed.
* Zero unapproved raw-data exposure.
* Faculty report the workflow improves preparation or consistency.

### 90-day decision checkpoint

**Objective:** Decide whether to continue, narrow, or stop.

Deliverables:

* Post-cycle retrospective.
* Canonical memory asset library.
* Next-cycle playbook.
* Projection packet v0.
* Risk review.
* Market/productization assessment.

Success metrics:

* At least 10 approved canonical memory assets.
* At least 3 concrete question/rubric improvements.
* At least 2 calibration improvements.
* Faculty can name specific knowledge that would otherwise have been lost.
* Privacy/legal owner approves the v1 direction.
* No candidate-level prediction or automation drift.

### Evidence that validates demand

* Faculty voluntarily ask to use the playbook before the next cycle.
* Committee chair says the decision log improved consistency.
* New faculty can prepare faster using prior memory.
* Rubric/question changes are traceable to evidence.
* Admissions ops sees fewer scattered artifacts.
* Privacy/legal owner is comfortable with the separation model.

### Evidence that kills or narrows the idea

* Faculty refuse structured notes.
* De-identification destroys too much usefulness.
* The process increases interview burden without improving retrospectives.
* Legal/privacy cannot approve live-data use.
* Existing CRM already solves 80% of the need.
* Projection outputs are repeatedly speculative or unsafe.
* Faculty try to use projections as candidate decision recommendations.

---

## 8. Open questions

### Questions for Victor

1. Who is the real buyer: dean, admissions director, program director, or Link innovation owner?
2. Is the first pilot meant to improve faculty experience, decision consistency, candidate fairness, or operational efficiency?
3. What existing systems already store interview data?
4. Is Link willing to prohibit candidate-level AI prediction in v0?
5. What would make this worth funding after 90 days?
6. Is external productization a real goal, or should this remain an internal capability?
7. Who owns GBrain governance at Link?
8. What political risk exists if faculty perceive this as surveillance?

### Questions for faculty

1. Which rubric dimensions are hardest to judge?
2. Which questions feel low-signal?
3. Where do interviewers disagree most?
4. What edge cases recur every year?
5. What knowledge did last year’s team wish it had inherited?
6. What notes are actually useful during committee review?
7. What would make structured notes too burdensome?
8. What should never be summarized by AI?

### Questions for legal/privacy owner

1. What is the approved legal basis for each processing purpose?
2. Are interviews recorded today?
3. Are candidates under 18 possible?
4. Are any external vendors currently used for transcription, storage, CRM, or AI?
5. What is the retention policy for raw admissions records?
6. What is the process for data-subject requests?
7. What cross-border transfers already exist?
8. Is an RIPD required before live data?

### Questions for technical implementer

1. Where will the raw vault live?
2. What access controls are available?
3. Can raw and de-identified layers be technically separated?
4. Can GBrain enforce source restrictions?
5. Can every memory asset carry provenance metadata?
6. Can logs show who accessed raw data and when?
7. What deletion and retention automation exists?
8. How will retrieval and projection tests be run?

---

## 9. Red lines

### What not to automate

* Admit/reject recommendations.
* Candidate ranking.
* Candidate “fit” scoring.
* Protected-trait inference.
* Emotion recognition.
* Personality scoring.
* Individual success prediction.
* Automated committee rationale generation without human approval.
* Automated adverse-impact conclusions without statistical/legal review.

### What not to store

* Unnecessary direct identifiers.
* Sensitive data unless legally necessary.
* Raw recordings longer than needed.
* Unredacted transcripts in GBrain.
* Candidate data in public AI tools.
* Faculty gossip or informal impressions unrelated to rubric evidence.
* Unsupported labels like “high potential,” “low resilience,” or “poor culture fit.”
* Demographic or protected-trait attributes unless a lawful, reviewed purpose exists.

### What not to claim

* “This predicts successful students.”
* “This removes bias.”
* “This makes admissions fair.”
* “This AI improves selection.”
* “This candidate should be admitted/rejected.”
* “This is anonymized” unless re-identification risk has been reviewed.
* “Fully compliant” without legal signoff.
* “Evidence-based prediction” without validation study.

### What requires human or legal approval

* Live candidate data use.
* Recordings/transcripts.
* External AI or transcription vendors.
* Cross-border data transfer.
* Sensitive-data processing.
* Children/adolescent data processing.
* Outcome validation studies.
* Projection layer expansion.
* Any productization outside Link.
* Any use in admissions decisions.

---

## 10. Appendices

### Appendix A — Source bibliography

**Brazil / LGPD / ANPD**

* LGPD English publication, ANPD / Brazilian law text. ([Serviços e Informações do Brasil][3])
* ANPD legitimate interest guide. 
* ANPD children/adolescents statement. ([Serviços e Informações do Brasil][26])
* ANPD security incident regulation. 
* Brazil PL 2338/2023 official Senate and Chamber pages. ([www25.senado.leg.br][13])

**Structured interviews and admissions validity**

* OPM structured interviews. ([U.S. Office of Personnel Management][1])
* OPM Structured Interview Guide. ([U.S. Office of Personnel Management][6])
* McDaniel et al. employment interview validity meta-analysis. 
* Lin et al. systematic review of medical-school admissions interviews. ([Perspectives on Medical Education][7])
* Jerant et al. MMI vs traditional interview reliability. ([Springer][8])
* AAMC Admissions Interview Foundations. ([AAMC][27])
* College Board ACES Admission Validity Study. ([ACES][9])

**AI governance**

* UNESCO generative AI in education and research. ([UNESCO][2])
* UNESCO Recommendation on the Ethics of AI. ([UNESCO][28])
* NIST AI Risk Management Framework Core. ([NIST AI Resource Center][29])
* OECD AI Principles. ([OECD][30])
* EU AI Act Service Desk, Annex III and high-risk requirements index. ([AI Act Service Desk][5])

**Qualitative data, anonymization, provenance, knowledge graphs**

* UK Data Service qualitative anonymization. ([UK Data Service][4])
* UNC qualitative data package guidance. ([tdx.unc.edu][10])
* FAIR Principles. ([GO FAIR][11])
* W3C PROV-O. ([W3C][31])
* Microsoft GraphRAG overview. ([Microsoft][12])
* GOV.UK user research data/privacy guidance. ([GOV.UK][32])

**Market sources**

* Slate. ([Technolutions][14])
* Salesforce Education Cloud. ([Salesforce][15])
* WebAdMIT / Liaison. ([Liaison][16])
* Acuity Insights / Casper. ([Acuity Insights][33])
* Kira Talent. ([Kira Talent][18])
* Qualtrics. ([Qualtrics][19])
* ATLAS.ti. ([ATLAS.ti][20])
* MAXQDA. ([MAXQDA][21])
* NVivo. ([Lumivero][22])
* Notion. ([Notion][23])
* Airtable. ([Airtable][24])
* Google Agent Search / enterprise RAG. ([Google Cloud][25])

### Appendix B — Suggested retention model

| Data type               | Recommended v0 handling                                                                                      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------ |
| Candidate identifiers   | Raw vault only; restricted access; delete/anonymize after approved retention period.                         |
| Interview recordings    | Collect only if necessary and noticed/consented; delete after transcript verification unless legally needed. |
| Raw transcripts         | Raw vault only; short retention; never in GBrain.                                                            |
| Interviewer notes       | Raw vault if identifiable; de-identified excerpts can become memory after review.                            |
| Committee decision logs | Raw vault if candidate-specific; de-identified edge-case patterns can become memory.                         |
| Consent/notice records  | Retain with source ledger for audit.                                                                         |
| Canonical memory assets | Longer-lived if de-identified and periodically reviewed.                                                     |
| Skill cards/playbooks   | Long-lived; no personal data.                                                                                |
| Projection hypotheses   | Long-lived as governance artifacts if aggregate and de-identified.                                           |
| Anonymization logs      | Store separately from anonymized assets; restricted access.                                                  |

### Appendix C — Sample candidate notice outline

**Aviso de Privacidade — Entrevistas de Admissão**

1. **Quem somos:** Link School of Business as controller.
2. **Finalidades:** admissions interview administration, evaluation support by faculty, process consistency, internal retrospective, and de-identified improvement of future interview cycles.
3. **Dados coletados:** application identifiers, interview scheduling data, interviewer notes, rubric scores if used, committee records, optional recordings/transcripts if applicable.
4. **Uso de IA:** AI tools, if approved, may assist with de-identified internal summaries and retrieval; they will not make admissions decisions.
5. **O que não faremos:** no automated admit/reject decisions; no individual ranking by AI; no protected-trait inference; no emotion/personality scoring.
6. **Base legal:** specify legal basis per purpose.
7. **Compartilhamento:** internal faculty/admissions/legal/technical roles; approved vendors if applicable.
8. **Transferência internacional:** disclose if any vendor processes data outside Brazil.
9. **Retenção:** raw records retained only for stated periods; de-identified memory may be retained for institutional learning.
10. **Direitos do titular:** confirmation, access, correction, anonymization/blocking/deletion, information on sharing, revocation of consent where applicable, objection, and contact channel.
11. **Contato:** DPO/encarregado contact and response process.

### Appendix D — Sample canonical memory asset

**Asset title:** Rubric dimension “entrepreneurial judgment” had weak evidence coverage
**Asset type:** Rubric lesson
**Cycle:** MBA Admissions 2026 — Pilot Program
**Validity scope:** One program, one rubric, one interview cycle
**De-identified summary:** Interviewers often rated entrepreneurial judgment without citing a specific observed decision, tradeoff, or example. Notes frequently described general ambition but not judgment under constraint.
**Evidence lineage:** 18 de-identified interview-note excerpts; 3 committee edge-case logs; post-cycle faculty retro item R-04.
**Privacy status:** De-identified; no candidate quotes longer than approved threshold; no direct identifiers.
**Confidence:** Medium
**Recommended action:** Add one structured probe: “Tell us about a time you made a business or project decision under uncertainty. What options did you reject and why?”
**Verifier:** Faculty chair + privacy reviewer
**Review date:** Before next interview cycle

### Appendix E — Sample projection hypothesis

**Hypothesis:** Question Q7 will produce low signal for “collaborative leadership” unless paired with a behavioral follow-up probe.
**Allowed use:** Faculty preparation and question-bank revision.
**Blocked use:** Candidate scoring, ranking, or prediction.
**Evidence:** Last cycle, Q7 responses were often generic; only 22% of de-identified notes contained a concrete behavior example linked to the collaborative-leadership rubric dimension.
**Confidence:** Medium
**Assumptions:** Note quality was sufficient to evaluate evidence density.
**Falsifiers:** If calibrated mock interviews produce concrete behavioral evidence from Q7 without probes, the hypothesis weakens.
**Human reviewer:** Faculty calibration group
**Outcome check:** Compare evidence density for Q7 in next cycle after adding probe.

### Appendix F — Final recommendation

Link School should build **Interview Memory OS v0** as a **governed memory-and-retrospective workflow**, not as an admissions AI product.

Before using live candidate data, Link must have: legal-basis matrix, Portuguese candidate notice, raw vault, role-based access, source/consent ledger, retention policy, external-vendor review, de-identification checklist, human-review policy, and a clear written ban on automated admissions decisions.

Before implementing projections beyond aggregate process/rubric hypotheses, Link should research: local validity outcomes, sample sizes, fairness metrics, legal classification, faculty acceptance, LGPD/RIPD requirements, and whether any Brazilian AI law has entered into force.

Top five risks and mitigations:

| Risk                                       | Mitigation                                                                      |
| ------------------------------------------ | ------------------------------------------------------------------------------- |
| Privacy breach or re-identification        | Raw/de-ID separation, anonymization log, access controls, privacy review.       |
| Automation drift into admissions decisions | Written red lines, UI labels, no candidate-level predictions, human review.     |
| Faculty non-adoption                       | Minimal templates, workshop prototype, focus on pain relief.                    |
| Low-quality memory assets                  | Source lineage, verifier role, confidence labels, review-by dates.              |
| Invalid projection claims                  | Aggregate-only hypotheses, falsifiers, outcome checks, no predictive marketing. |

A successful 90-day pilot would leave Link with a reusable playbook, a small library of approved canonical memory assets, a functioning skill graph, a safe projection packet, and faculty saying: **“Next year’s team will not start from scratch.”**

[1]: https://www.opm.gov/policy-data-oversight/assessment-and-selection/structured-interviews/ "Structured Interviews"
[2]: https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research "Guidance for generative AI in education and research | UNESCO"
[3]: https://www.gov.br/anpd/pt-br/centrais-de-conteudo/outros-documentos-e-publicacoes-institucionais/lgpd-en-lei-no-13-709-capa.pdf/%40%40display-file/file "Capa LGPD em inglês 2"
[4]: https://ukdataservice.ac.uk/learning-hub/research-data-management/anonymisation/anonymising-qualitative-data/ "Anonymising qualitative data - UK Data Service"
[5]: https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3 "Annex III | AI Act Service Desk"
[6]: https://www.opm.gov/policy-data-oversight/assessment-and-selection/structured-interviews/guide.pdf " Structured Interview Guide"
[7]: https://pmejournal.org/articles/10.1007/S40037-022-00726-8 "Best practices for interviewing applicants for medical school admissions: a systematic review | Perspectives on Medical Education"
[8]: https://link.springer.com/article/10.1186/s12909-017-1030-0 "Reliability of Multiple Mini-Interviews and traditional interviews within and between institutions: a study of five California medical schools | BMC Medical Education | Springer Nature Link"
[9]: https://aces.collegeboard.org/aces-studies/admission-validity-study "Admission Validity Study – ACES™ | College Board"
[10]: https://tdx.unc.edu/TDClient/33/Portal/KB/ArticleDet?ID=412 "
	Article - RDMC Data Management Guide:...
"
[11]: https://www.go-fair.org/fair-principles/ "FAIR Principles - GO FAIR"
[12]: https://www.microsoft.com/en-us/research/project/graphrag/overview/ "Project GraphRAG - Microsoft Research: Overview"
[13]: https://www25.senado.leg.br/web/atividade/materias/-/materia/157233 "PL 2338/2023 - Senado Federal"
[14]: https://technolutions.com/admissions "Admissions & Enrollment — Technolutions"
[15]: https://www.salesforce.com/education/cloud/ "Salesforce Education Cloud | Education CRM | Salesforce"
[16]: https://www.liaisonedu.com/application-management/webadmit/ "WebAdMIT: Enrollment Management & Admissions System"
[17]: https://acuityinsights.app/casper/ "About Casper - Take Casper"
[18]: https://www.kiratalent.com/ "Kira Talent | The world’s only holistic admissions solution for higher education"
[19]: https://www.qualtrics.com/education/ "Student & Staff Experience Management for Education"
[20]: https://atlasti.com/ "ATLAS.ti | The #1 Software for Qualitative Data Analysis - ATLAS.ti"
[21]: https://www.maxqda.com/ "MAXQDA Official Site | All-In-One Tool for Qualitative Data Analysis"
[22]: https://lumivero.com/products/nvivo/ "NVivo by Lumivero | Qualitative data analysis (QDA) software"
[23]: https://www.notion.com/product/wikis "Your connected workspace for wiki, docs & projects | Notion"
[24]: https://www.airtable.com/platform "The digital operations platform - Airtable"
[25]: https://cloud.google.com/products/gemini-enterprise-agent-platform/agent-search "Agent Search on Gemini Enterprise Agent Platform | Google Cloud"
[26]: https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-divulga-enunciado-sobre-o-tratamento-de-dados-pessoais-de-criancas-e-adolescentes "ANPD divulga enunciado sobre o tratamento de dados pessoais de crianças e adolescentes"
[27]: https://www.aamc.org/services/admission-interview-foundations "Undergraduate Admission Interview Foundations: Role and Setup | AAMC"
[28]: https://www.unesco.org/en/artificial-intelligence/recommendation-ethics "Ethics of Artificial Intelligence - AI | UNESCO"
[29]: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ "

      
  AI RMF Core


      
  
  \- AIRC


    "
[30]: https://www.oecd.org/en/topics/sub-issues/ai-principles.html "AI principles | OECD"
[31]: https://www.w3.org/TR/prov-o/ "PROV-O: The PROV Ontology"
[32]: https://www.gov.uk/service-manual/user-research/managing-user-research-data-participant-privacy "Managing user research data and participant privacy - Service Manual - GOV.UK"
[33]: https://acuityinsights.com/ "Home - Acuity Insights"
