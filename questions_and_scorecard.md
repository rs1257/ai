# Capgemini Invent – GenAI Interview Question Bank & Scorecard

## Candidate Details

| Field       | Details |
| ----------- | ------- |
| Candidate   |         |
| Interviewer |         |
| Date        |         |

## Assessment Guide

Assess each criterion using demonstrated evidence. Use the same qualitative judgement across all parts; do not calculate a numeric total.

| Assessment                       | Guidance                                                                    |
| -------------------------------- | --------------------------------------------------------------------------- |
| **Exceeds expectations**         | Complete, well-reasoned evidence; anticipates relevant production concerns. |
| **Meets expectations**           | Solid evidence with only minor gaps.                                        |
| **Partially meets expectations** | Core capability is present, but there are notable gaps.                     |
| **Below expectations**           | Significant omissions, misunderstandings or errors.                         |
| **Not demonstrated**             | No supporting evidence, or the response is fundamentally incorrect.         |
| **Not assessed**                 | There was no reasonable opportunity to assess this criterion.               |

### Grade calibration

Use the criteria below to calibrate expectations to the candidate's grade. Core correctness and the same qualitative assessment scale apply to both grades; do not treat C2's more modest implementation expectations as permission to accept incorrect calculations.

| Part | C2 evidence consistent with expectations | C3 evidence consistent with expectations |
| ---- | ---------------------------------------- | ---------------------------------------- |
| **Part 1: Technical test** | Correct, understandable conditional logic for the tax bands and some relevant tests. The candidate recognises that the conditionals should be refactored as rules grow. | A well-structured solution that iterates over the tax bands, with meaningful tests for representative values, band boundaries and invalid inputs. |
| **Part 3: System design** | Uses the provided starter to produce and explain a coherent end-to-end design. Assess the flow, component responsibilities and reasoning; do not require exhaustive vendor-specific service or model names. | Starts from a blank canvas, produces a clear end-to-end design, and identifies suitable named cloud services and model(s), explaining selection and trade-offs. Candidates may research individual services and models, but the design must be their own. |

---

# Part 1: Technical Test – Stamp Duty Calculator

Use these questions after the **30-minute coding exercise**.

## Solution & Python

| Question                                                                    | Strong-answer signals                                                                    | Comments |
| --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | -------- |
| Talk me through your approach. What assumptions did you make?               | Clear decomposition, validation, progressive tax bands and sensible assumptions.         |          |
| How did you decide what to test? What defects could your tests still miss?  | Boundaries, invalid inputs, happy paths, integration gaps and incorrect business rules.  |          |
| Why might you use `Decimal` rather than `float` for financial calculations? | Floating-point precision, predictable decimal arithmetic and rounding.                   |          |
| How would you structure the code as the application became larger?          | Separation of domain logic, API, configuration and infrastructure.                       |          |
| Would you use classes here? Why or why not?                                 | Avoids unnecessary abstraction; understands when domain objects/classes become valuable. |          |
| How would you model additional cases such as second homes or reliefs?       | Extensible/versioned rules rather than increasingly complex conditionals.                |          |
| What would you improve given more time?                                     | Prioritises testing, validation, maintainability and production readiness.               |          |

## Testing & Quality

| Question                                                                    | Strong-answer signals                                                                                          | Comments |
| --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------- |
| How do you ensure you catch bugs sooner?                                    | Unit tests, typing, linting, small PRs, code review and CI.                                                    |          |
| What other ways could you test the calculator?                              | Integration, contract, property-based, mutation and performance testing where appropriate.                     |          |
| What would you look for in a code review?                                   | Correctness, boundary cases, readability, duplication, validation and test coverage.                           |          |
| What is the difference between unit, integration and contract testing here? | Calculator independently; service and dependencies together; API expectations between consumers and providers. |          |

## API & Microservices

| Question                                                                      | Strong-answer signals                                                                            | Comments |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------- |
| How would you expose this calculator as a microservice for an AI application? | FastAPI or equivalent, validated schemas, structured responses and a clear API contract.         |          |
| How would you design the calculator API?                                      | Clear request/response schema, validation, error handling, versioning and deterministic results. |          |
| How would the frontend communicate with it?                                   | Backend-owned business logic, HTTP API and appropriately typed contracts.                        |          |
| What happens if a user submits the same request multiple times?               | Understands concurrency and idempotency where required.                                          |          |
| How would you handle failures and exceptions?                                 | Domain exceptions mapped to consistent API errors rather than exposing stack traces.             |          |

## Docker, CI/CD & Production

| Question                                                   | Strong-answer signals                                                                                        | Comments |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | -------- |
| How would you containerise the application?                | Small pinned Python image, non-root user, dependency management, health checks and no secrets in the image.  |          |
| What would you include in CI?                              | Formatting/linting, typing, tests, vulnerability/dependency scanning and build validation.                   |          |
| What would you include in CD?                              | Environment promotion, deployment checks, smoke tests, monitoring and rollback.                              |          |
| How would you manage secrets?                              | Managed identities where possible and a managed secret store such as Azure Key Vault or AWS Secrets Manager. |          |
| How would you diagnose the API if it suddenly became slow? | Metrics/traces first, isolate application versus dependency latency, then profile the measured bottleneck.   |          |

## Part 1 Scorecard

| Criterion                          | Evidence to look for                                                                                                                  | Assessment | Comments |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------- | -------- |
| Functional correctness             | Implements progressive bands correctly: first £125,000 at 0%, next £600,000 at 5%, remainder at 15%; produces £71,250 for £1,000,000. |            |          |
| Boundaries and input handling      | Considers zero, negative or invalid input and values around £125,000 and £725,000; defines sensible behaviour rather than guessing.   |            |          |
| Tests                              | C2: some relevant tests. C3: meaningful representative, band-boundary and invalid-input tests. Tests behaviour rather than implementation details. |            |          |
| Python quality                     | C2: clear, understandable conditional logic and awareness of when it needs refactoring. C3: readable, well-structured iteration over the tax bands without unnecessary complexity. |            |          |
| Error handling and maintainability | Keeps behaviour predictable, avoids swallowed errors and duplication, and makes business rules easy to review and change.             |            |          |
| Reasoning and productionisation    | Explains assumptions and trade-offs, identifies PoC limitations and describes practical production improvements.                      |            |          |

**Part 1 overall assessment:**

**Key evidence / comments:**

---

# Part 2: AI Task – Guidance Assistant Prompt

Use these questions after the **15-minute prompt-design exercise**.

## Prompt Design

| Question                                                                   | Strong-answer signals                                                                   | Comments |
| -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | -------- |
| Talk me through how you structured your system prompt.                     | Role, responsibilities, boundaries, tools, evidence requirements and failure behaviour. |          |
| What instructions keep the assistant grounded in supplied guidance?        | Explicit evidence requirements and refusal/clarification when evidence is unavailable.  |          |
| How do system instructions, user instructions and supplied context differ? | Understands instruction hierarchy and differing trust levels.                           |          |
| What shouldn't be placed in a system prompt?                               | Secrets, rapidly changing data and deterministic security/business controls.            |          |
| How would you version and test this prompt?                                | Source control, evaluation suite, release process and rollback.                         |          |

## Tool Calling & Agents

| Question                                                               | Strong-answer signals                                                                      | Comments |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | -------- |
| How would you ensure every numerical calculation uses the calculator?  | Explicit tool requirement and no model arithmetic fallback.                                |          |
| How does an LLM decide which tool to call?                             | Tool descriptions/schema → model selection → structured arguments → application execution. |          |
| Should we trust tool parameters generated by the LLM?                  | No. Validate them server-side before execution.                                            |          |
| What happens if required transaction information is missing?           | Ask targeted clarification questions rather than inventing values.                         |          |
| What happens if the calculator fails?                                  | Don't calculate independently; return a controlled failure/degraded response.              |          |
| What's the difference between deterministic and agentic orchestration? | Application-defined workflow versus model-directed decisions.                              |          |
| Would you make this application fully agentic?                         | Probably not initially; controlled flows are simpler, cheaper and easier to evaluate.      |          |
| How would you prevent an agent repeatedly calling tools?               | Iteration/tool limits, timeouts, budgets and repeated-call detection.                      |          |

## GenAI & LLM Fundamentals

| Question                                               | Strong-answer signals                                                                                        | Comments |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | -------- |
| What actually happens when we send a prompt to an LLM? | Tokenisation, transformer inference and probabilistic next-token generation.                                 |          |
| What is a token and why does it matter?                | Context limits, cost and latency.                                                                            |          |
| What is a context window?                              | Limited amount of information the model can process; bigger isn't automatically better.                      |          |
| Why might an LLM answer a question incorrectly?        | Hallucination, ambiguity, insufficient or conflicting information, poor tool usage or model limitations.     |          |
| What does temperature do?                              | Controls sampling variability; not an accuracy or safety mechanism.                                          |          |
| When would you use a smaller model?                    | Classification, extraction or routing where evaluation shows it meets the requirement at lower cost/latency. |          |

## Structured Outputs

| Question                                                                                    | Strong-answer signals                                                             | Comments |
| ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | -------- |
| How could structured outputs help this assistant?                                           | Extract transaction details into a validated schema before calculator invocation. |          |
| Why use structured output rather than simply asking for JSON?                               | Stronger structural guarantees while still requiring semantic validation.         |          |
| What happens if structured output passes schema validation but contains an incorrect value? | Schema validity isn't factual correctness; business validation is still required. |          |
| How would you stop the model inventing calculator parameters?                               | Required fields, validation and user clarification.                               |          |

## AI Security

| Question                                                                | Strong-answer signals                                                                            | Comments |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------- |
| How would you test that a user cannot override the system instructions? | Adversarial evaluation plus controls outside the prompt.                                         |          |
| What is prompt injection?                                               | An attempt to manipulate model behaviour via untrusted instructions.                             |          |
| Can a system prompt completely prevent prompt injection?                | No; prompts are only one control layer.                                                          |          |
| Why shouldn't the LLM control authorization?                            | A probabilistic model isn't a security boundary.                                                 |          |
| How would you protect tools exposed to an agent?                        | Authentication, authorization, schemas, validation, least privilege, rate limiting and auditing. |          |

## AI Evaluation

| Question                                                                | Strong-answer signals                                                                                 | Comments |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------- |
| How would you test and refine this prompt?                              | Representative evaluation dataset with expected behaviours rather than manually trying a few prompts. |          |
| What test cases would you include?                                      | Normal, boundary, ambiguous, missing data, adversarial, tool failure and unsupported requests.        |          |
| How do you test something where the exact wording changes between runs? | Evaluate factual and behavioural criteria rather than exact text matching.                            |          |
| Would you use another LLM to evaluate the output?                       | Potentially, but calibrate against human-labelled or deterministic ground truth.                      |          |
| What should block a prompt change from being released?                  | Regression beyond agreed thresholds, particularly critical safety or tool-use behaviour.              |          |

## Part 2 Scorecard

| Criterion                        | Evidence to look for                                                                                                    | Assessment | Comments |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ---------- | -------- |
| Role and scope                   | Defines the assistant's purpose and limits responses to supplied guidance, user-provided facts and calculator results.  |            |          |
| Grounding and source authority   | Treats official guidance as authoritative for rules and the calculator as authoritative for numerical results.          |            |          |
| Calculator tool use              | Requires the calculator for calculations, estimates, comparisons and hypotheticals; doesn't alter tool results.         |            |          |
| Missing information and failures | Reuses known facts, asks only for necessary information, avoids material assumptions and handles tool failure safely.   |            |          |
| Prompt clarity and robustness    | Instructions are specific, consistent and organised; handles conflicting or untrusted instructions.                     |            |          |
| GenAI understanding              | Demonstrates understanding of LLM behaviour, structured outputs, tools/agents and appropriate deterministic boundaries. |            |          |
| AI security                      | Understands prompt injection, untrusted model output, authorization boundaries and tool protection.                     |            |          |
| Testing and refinement           | Proposes representative tests and repeatable evaluation covering tools, unsupported questions and failure cases.        |            |          |

**Part 2 overall assessment:**

**Key evidence / comments:**

---

# Part 3: System Design – AI-Powered Guidance Platform

Use these questions during the **10-minute architecture discussion**.

## End-to-End Architecture

| Question                                                                          | Strong-answer signals                                                                                                     | Comments |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------- |
| Walk me through your architecture from the user's question to the final response. | Clear end-to-end flow and responsibilities rather than simply listing cloud services.                                     |          |
| What would you ask before starting the design?                                    | Users, scale, availability, security, data sensitivity, latency, regulatory requirements, budget and expected AI quality. |          |
| Where does the calculator run?                                                    | Independent deterministic service/tool behind the orchestration layer.                                                    |          |
| How do you guarantee every calculation uses it?                                   | Enforced application/tool workflow rather than prompt instruction alone.                                                  |          |

## RAG & Government Guidance

| Question                                                   | Strong-answer signals                                                                         | Comments |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------------- | -------- |
| Explain how RAG works in this architecture.                | Ingest → chunk → embed/index → retrieve → context → model → cited answer.                     |          |
| Why does retrieval select particular documents?            | Similarity/relevance, metadata filters, lexical matching and potentially reranking.           |          |
| How do you ingest and keep government guidance current?    | Controlled ingestion pipeline, metadata/versioning and scheduled or change-triggered updates. |          |
| Why might you combine vector and keyword search?           | Semantic matching plus strong exact-term or number retrieval.                                 |          |
| What is reranking?                                         | More accurate second-stage ordering of retrieval candidates.                                  |          |
| What happens when retrieval can't find a reliable answer?  | Don't hallucinate; communicate uncertainty and escalate appropriately.                        |          |
| How would you make the model cite its source?              | Preserve source metadata through ingestion, retrieval and response generation.                |          |
| What's a simple way of improving retrieval speed and cost? | Metadata filtering, sensible top-k/context limits and caching where appropriate.              |          |

## Scalability & Reliability

| Question                                               | Strong-answer signals                                                                         | Comments |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------- | -------- |
| How would you make the solution scale?                 | Stateless services, load balancing, autoscaling and independently scalable components.        |          |
| How is load distributed between application instances? | Managed load balancing across healthy instances.                                              |          |
| What would you autoscale on?                           | Request rate, latency, queue depth, CPU or another component-appropriate metric.              |          |
| What happens if the calculator is unavailable?         | Fail safely and don't allow the LLM to substitute its own calculation.                        |          |
| What happens if the model provider is unavailable?     | Appropriate timeout/retry, graceful failure and potentially approved fallback models.         |          |
| Where is the architecture most likely to fail?         | Identifies concrete dependencies and failure modes rather than generic availability concerns. |          |

## Data & Consistency

| Question                                                                       | Strong-answer signals                                                                                                         | Comments |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- | -------- |
| For the vector store, would you favour availability or consistency?            | Search may favour availability, while guidance/index versions require controlled publication to avoid inconsistent knowledge. |          |
| The government changes the tax bands tomorrow. What happens?                   | Calculator rules and guidance/index follow controlled but separate update processes.                                          |          |
| How would you prevent users receiving answers from mixed versions of guidance? | Versioned indexes/configuration and controlled publication or switch-over.                                                    |          |

## Security & Privacy

| Question                                         | Strong-answer signals                                                                            | Comments |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------ | -------- |
| How would you protect user data and credentials? | Encryption, identity, least privilege, secret management and data minimisation.                  |          |
| What information shouldn't be sent to the model? | Unnecessary PII, credentials, secrets and unrelated sensitive information.                       |          |
| What is indirect prompt injection?               | Malicious instructions arriving through retrieved or external content.                           |          |
| How would you protect against it?                | Treat external content as untrusted and enforce tool and authorization controls outside the LLM. |          |

## Observability & LLMOps

| Question                                          | Strong-answer signals                                                                                       | Comments |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | -------- |
| How would you monitor the system in production?   | Logs, metrics, traces, correlation IDs, AI/tool telemetry, latency and failures.                            |          |
| How do you know the AI is giving correct answers? | Golden evaluation datasets, production feedback, sampled review and regression monitoring.                  |          |
| What AI-specific metrics would you collect?       | Tool success, retrieval quality indicators, evaluation scores, failures/refusals, tokens, latency and cost. |          |
| How would you safely upgrade to a new model?      | Offline evaluation → shadow/canary testing → monitoring → gradual release → rollback.                       |          |
| How would you roll back a bad prompt?             | Versioned prompts/configuration and independent deployment or rollback.                                     |          |

## Cost & Sustainable AI

| Question                                             | Strong-answer signals                                                                                                    | Comments |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | -------- |
| How would you control cost per answer?               | Model selection/routing, token limits, context optimisation, caching and monitoring.                                     |          |
| How do you stop anonymous users running up the bill? | Rate limits, quotas, authentication where appropriate and abuse detection.                                               |          |
| How would you make the solution more sustainable?    | Smaller appropriate models, avoiding unnecessary inference, reduced token usage, caching and efficient batch processing. |          |
| Would every request use the same model?              | Not necessarily; use evaluated task-appropriate model routing if the additional complexity is justified.                 |          |

## GenAI Extensions

Use these to assess whether the candidate can **evolve the architecture**, rather than only defend their initial design.

| Question                                                                               | Strong-answer signals                                                                                                             | Comments |
| -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Users can now upload property documents. How would you extend the platform?            | Secure storage, file validation, document extraction/OCR or multimodal models, PII handling and confirmation of extracted values. |          |
| We want users to talk to the assistant by voice. What changes?                         | Speech-to-text, streaming, text-to-speech, latency and confirmation of important financial information.                           |          |
| Someone suggests multiple collaborating agents. Would you use them?                    | Only where measurable value outweighs additional latency, cost, orchestration complexity and failure modes.                       |          |
| The assistant should remember users between sessions. How would you implement it?      | Explicit memory store, authentication, consent, retention/deletion and user isolation.                                            |          |
| AI should detect government rule changes automatically. How far would you automate it? | AI can detect/propose changes; critical tax-rule deployment remains validated, tested and controlled.                             |          |
| The assistant should send reports to third parties. What changes?                      | Explicit write tools, authentication/authorization, confirmation, audit trail and idempotency.                                    |          |
| When should a tool action require human approval?                                      | Consequential actions or important record changes; risk-based approval.                                                           |          |

## Agile Delivery

| Question                                                                                        | Strong-answer signals                                                                                  | Comments |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | -------- |
| How would you break this platform into deliverable stories?                                     | Vertical slices delivering user value rather than separate frontend, backend and AI technical stories. |          |
| What would you build first?                                                                     | Smallest production-quality journey that validates major assumptions.                                  |          |
| Halfway through the sprint this turns out to be twice as difficult as expected. What do you do? | Raise early, re-scope with the team/PO and preserve the highest-value increment.                       |          |
| The deadline is approaching and you're asked to skip testing. What do you do?                   | Explain the risk and negotiate scope rather than dropping critical quality controls.                   |          |
| Another engineer disagrees strongly with your architecture. What do you do?                     | Compare options against evidence and requirements and optimise for the team/client outcome.            |          |
| How would you manage technical debt introduced while building the PoC?                          | Make it visible, understand its impact and prioritise it alongside feature delivery.                   |          |

## Consulting & Communication

| Question                                                                              | Strong-answer signals                                                                                           | Comments |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | -------- |
| How would you explain this architecture to a non-technical client?                    | User/business outcomes first, minimal jargon and progressively introduced technical detail.                     |          |
| A client wants more AI in the solution. How do you decide whether that's appropriate? | Starts with the user problem and assesses reliability, cost and complexity rather than adding AI automatically. |          |
| How would you explain the biggest risk of this system to the client?                  | Clear business impact, likelihood and mitigation.                                                               |          |
| How would you challenge a requirement you believed was unsafe?                        | Explains evidence/risk and proposes a safer alternative constructively.                                         |          |

## Part 3 Scorecard

| Criterion                      | Evidence to look for                                                                                                | Assessment | Comments |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------- | ---------- | -------- |
| End-to-end architecture        | Clearly connects UI, API, orchestration, calculator, retrieval, data stores and response flow.                      |            |          |
| Calculator integration         | Routes calculations to the calculator as the sole numerical authority and explains service boundaries and failures. |            |          |
| RAG and trusted content        | Uses official documentation with provenance/citations, freshness and a clear source-of-truth strategy.              |            |          |
| Answer quality and guardrails  | Handles missing evidence safely and separates guidance from deterministic calculation results.                      |            |          |
| Scalability and reliability    | Explains load balancing, scaling, dependency failures and appropriate resilience patterns.                          |            |          |
| Security and privacy           | Addresses access controls, data minimisation, secrets, AI security and appropriate trust boundaries.                |            |          |
| Observability and LLMOps       | Covers monitoring, AI evaluation, model/prompt versioning, controlled releases and rollback.                        |            |          |
| Cost and sustainability        | Controls model/token expenditure and explains appropriate model selection/routing; for C3, can identify and justify suitable model(s), researching details as needed. |            |          |
| GenAI extensibility            | Can evolve the architecture for multimodal, memory, voice and agentic use cases without unnecessary complexity.     |            |          |
| Diagram clarity and trade-offs | Produces a readable end-to-end design and explains key choices, risks, bottlenecks and alternatives.                |            |          |

**Part 3 overall assessment:**

**Key evidence / comments:**

---

# Cross-Part Assessment

These questions can be asked after any of the three exercises.

## Cross-Part Follow-Ups

| Question                                                                      | Strong-answer signals                                                                                 | Comments |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------- |
| What is the most important assumption you've made? How would you validate it? | Identifies something material and describes a practical validation approach.                          |          |
| What is the biggest risk before launch?                                       | Prioritises meaningful risk rather than listing everything that could fail.                           |          |
| If you had another week, what would you improve first?                        | Prioritises based on risk/value rather than gold-plating.                                             |          |
| What would you deliberately **not** build yet?                                | Good scope control and avoidance of premature complexity.                                             |          |
| Where have you deliberately chosen deterministic software instead of AI?      | Calculation, validation, authentication/security and critical business rules.                         |          |
| What trade-off in your solution are you least comfortable with?               | Self-awareness and ability to reason about compromises.                                               |          |
| What changes if usage increases 100×?                                         | Identifies actual bottlenecks rather than simply saying "autoscaling".                                |          |
| How would you prove to the client that this is production-ready?              | Evidence from testing, AI evaluation, security, observability, performance and operational readiness. |          |
| How would you present this solution to the client?                            | Outcome-led communication adapted to the audience.                                                    |          |

## Cross-Part Scorecard

| Criterion                       | Evidence to look for                                                                                                         | Assessment | Comments |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------- | -------- |
| Communication and collaboration | Thinks aloud where appropriate, listens to clarification and explains technical ideas clearly to different audiences.        |            |          |
| Judgement and ownership         | States assumptions, recognises limitations, weighs trade-offs and responds constructively to feedback.                       |            |          |
| Agile delivery                  | Can prioritise and slice work, manage uncertainty, maintain quality and collaborate effectively within a delivery team.      |            |          |
| Consulting mindset              | Connects technology to user/client outcomes and constructively challenges inappropriate, unnecessary or unsafe requirements. |            |          |

---

# Candidate-Facing Interview Feedback

> **CANDIDATE-FACING SECTION**
>
> **Only this section should be shared with the candidate.**
>
> Do **not** share the interview question bank, strong-answer signals, comments, scorecards, assessments, internal recommendation, or evaluation rationale above.

## Candidate

**Name:**

**Interview date:**

**Role:** GenAI Full-Stack Engineer

---

## Interview Outcome

**Outcome:**

## Feedback

Thank you for taking the time to complete the Capgemini Invent GenAI interview assessment. The feedback below reflects your performance across the technical exercise, GenAI task and system design discussion.

### Strengths

-
-
-

### Development Areas

-
-
-

### Overall Feedback

---
