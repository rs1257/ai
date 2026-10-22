# Capgemini Invent - GenAI Interview Scorecard

## Candidate Details

| Field       | Details |
| ----------- | ------- |
| Candidate   |         |
| Interviewer |         |
| Date        |         |

## Assessment Guide

Assess each criterion using demonstrated evidence. Use the same qualitative judgment across all parts; do not calculate a numeric total.

| Assessment                   | Guidance                                                                    |
| ---------------------------- | --------------------------------------------------------------------------- |
| Exceeds expectations         | Complete, well-reasoned evidence; anticipates relevant production concerns. |
| Meets expectations           | Solid evidence with only minor gaps.                                        |
| Partially meets expectations | Core capability is present, but there are notable gaps.                     |
| Below expectations           | Significant omissions, misunderstandings, or errors.                        |
| Not demonstrated             | No supporting evidence, or the response is fundamentally incorrect.         |
| Not assessed                 | There was no reasonable opportunity to assess this criterion.               |

## Part 1: Technical Test - Stamp Duty Calculator

| Criterion                          | Evidence to look for                                                                                                                          | Assessment / notes |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Functional correctness             | Implements progressive bands correctly: first £125,000 at 0%, next £600,000 at 5%, and the remainder at 15%; produces £71,250 for £1,000,000. |                    |
| Boundaries and input handling      | Considers zero, negative or invalid input, and values at or around £125,000 and £725,000; defines sensible behavior rather than guessing.     |                    |
| Tests                              | Includes meaningful happy-path, band-boundary, and invalid-input tests; tests behavior rather than implementation details.                    |                    |
| Python quality                     | Uses clear names, appropriate data structures, readable functions, and idiomatic Python without unnecessary complexity.                       |                    |
| Error handling and maintainability | Keeps behavior predictable, avoids swallowed errors and duplication, and makes tax bands or business rules easy to review and change.         |                    |
| Reasoning and productionization    | Explains assumptions and trade-offs, identifies PoC limitations, and can describe practical production improvements.                          |                    |

**Suggested follow-up:** What would you change to productionize this PoC, and how would you ensure the tax rules stay correct as they change?

## Part 2: AI Task - Guidance Assistant Prompt

| Criterion                        | Evidence to look for                                                                                                                                         | Assessment / notes |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| Role and scope                   | Clearly defines the assistant's purpose and limits answers to supplied guidance, user-provided facts, and calculator results.                                |                    |
| Grounding and source authority   | Treats official/supplied guidance as authoritative for rules and the calculator as authoritative for numerical results; avoids unsupported claims.           |                    |
| Calculator tool use              | Requires the tool for every calculation, including estimates, comparisons, and hypothetical scenarios; prohibits mental arithmetic or changing tool results. |                    |
| Missing information and failures | Reuses known facts, asks only for necessary missing information, avoids material assumptions, and defines safe behavior when the tool fails.                 |                    |
| Prompt clarity and robustness    | Instructions are specific, consistent, and organized; handles conflicting instructions or untrusted user content without overriding its rules.               |                    |
| Testing and refinement approach  | Proposes representative test cases and a repeatable evaluation/refinement process, including tool calls, unsupported questions, and failure cases.           |                    |

**Suggested follow-up:** How would you test and refine this prompt, and what would you do when the user asks for a calculation but the required details are missing?

## Part 3: System Design - Guidance Platform

| Criterion                          | Evidence to look for                                                                                                                            | Assessment / notes |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| End-to-end architecture            | Diagram clearly connects user interface, API, orchestration, calculator, retrieval, data stores, and response flow.                             |                    |
| Calculator integration             | Routes every calculation to the Part 1 calculator as the sole source of numerical results; explains service boundaries and failure behavior.    |                    |
| RAG and trusted content            | Shows ingestion and retrieval of official government documentation, with provenance/citations, freshness, and a clear source-of-truth strategy. |                    |
| Answer quality and guardrails      | Grounds responses in retrieved material, handles low-confidence or missing evidence, and separates guidance answers from calculator results.    |                    |
| Security, privacy, and reliability | Addresses appropriate access controls, data minimization, secrets, resilience, scaling, and relevant monitoring or alerting.                    |                    |
| Diagram clarity and trade-offs     | Produces a readable end-to-end Draw.io diagram, explains key choices and bottlenecks, and identifies risks or production considerations.        |                    |

**Suggested follow-up:** How would you keep retrieved guidance current and prove which source supported an answer?

## Cross-Part Assessment

| Criterion                       | Evidence to look for                                                                                                | Assessment / notes |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Communication and collaboration | Thinks aloud where appropriate, listens to clarification, and explains technical ideas clearly to a non-specialist. |                    |
| Judgment and ownership          | States assumptions, recognizes limitations, weighs trade-offs, and responds constructively to feedback.             |                    |

## Overall Assessment

| Part                   | Overall assessment | Evidence / notes |
| ---------------------- | ------------------ | ---------------- |
| Part 1: Technical test |                    |                  |
| Part 2: AI task        |                    |                  |
| Part 3: System design  |                    |                  |
| Cross-part assessment  |                    |                  |

**Recommendation:** Yes / No

**Strengths:**

- **Risks or development areas:**

- **Evidence and rationale for recommendation:**
