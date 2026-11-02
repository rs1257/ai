# Capgemini Invent – GenAI Interview

## Assessment Overview

The assessment is divided into three parts:

1. **Technical Test - 30 minutes**
   - Followed by 10 minutes for questions and discussion
2. **AI Task - 15 minutes**
   - Followed by 5 minutes for questions and discussion
3. **System Design - 30 minutes**
   - Followed by 10 minutes for questions and discussion

---

# Part 1: Technical Test - 30 minutes

## Stamp Duty Calculator

### Objective

Build a Proof of Concept (PoC) for a **Stamp Duty Calculator**.

The solution should:

- Accept a property purchase price as input.
- Calculate the total Stamp Duty owed.
- Return the correct tax amount based on the defined tax bands.

---

### Requirements

The calculator should using the following rules to calculate stamp duty:

| Property Value Range | Tax Rate |
| -------------------- | -------- |
| £0 – £125,000        | 0%       |
| £125,001 – £725,000  | 5%       |
| £725,001+            | 15%      |

Stamp Duty is applied progressively across tax bands:

1. The first **£125,000** is taxed at **0%**.
2. The next **£600,000** (from **£125,001 to £725,000**) is taxed at **5%**.
3. Any amount above **£725,000** is taxed at **15%**.

---

### Worked Example

The following shows an example for a property of value **£1,000,000**

| Tax Band         | Taxable Amount | Rate | Tax Due |
| ---------------- | -------------- | ---- | ------- |
| First £125,000   | £125,000       | 0%   | £0      |
| Next £600,000    | £600,000       | 5%   | £30,000 |
| Remaining Amount | £275,000       | 15%  | £41,250 |

```text
£0 + £30,000 + £41,250 = £71,250
```

**Expected Result:** **£71,250**

---

### Key Considerations

During the exercise:

- Google may be used.
- AI tools and coding assistants are **not permitted**.
- Unit tests should be included.
- Candidates should explain their thinking and approach while completing the task.
- Produce the best solution possible given the time you have available.

---

## Questions and Discussion - 10 minutes

Following the technical test, there will be 10 minutes for questions and discussion.

Candidates should be prepared to:

- Walk through and explain their solution.
- Explain the technical decisions they made.
- Discuss any trade-offs or assumptions.
- Explain what they would improve or change given more time.
- Answer follow-up questions about their implementation and tests.

---

# Part 2: AI Task - 15 minutes

## AI-Powered Stamp Duty Guidance Assistant

### Objective

- Create a **system prompt** for an AI assistant that helps users understand Stamp Duty regulations and calculations.
- Provide 3 example user prompts and the expected output.

---

### Requirements

The assistant should:

- Explain Stamp Duty rules and tax bands.
- Answer user questions about Stamp Duty.
- Verify calculations when requested.
- Use the **Stamp Duty Calculator** from Part 1 as a trusted calculation tool.
- Invoke the calculator whenever a calculation is required instead of performing calculations independently.

### Key Considerations

- The calculator should be treated as the **authoritative source** for all tax calculations.
- You will **not** run the prompt, we are interesting in the thought behind developing the prompt rather than the actual result.
- The prompt is for use with a chatbot or an agent and is not one for code generation.

---

## Questions and Discussion - 5 minutes

Following the AI task, there will be 5 minutes for questions and discussion.

Candidates should be prepared to:

- Explain the reasoning behind their prompt design.
- Discuss how they have instructed the AI to use the calculator.
- Explain how they have considered accuracy, reliability and appropriate AI behaviour.
- Answer follow-up questions about their approach.

---

# Part 3: System Design - 30 minutes

## AI-Powered Stamp Duty Guidance Platform

### Objective

Design a scalable, production-ready platform that helps users:

- Understand Stamp Duty rules.
- Verify Stamp Duty calculations.
- Ask natural language questions about Stamp Duty.
- Receive answers based on trusted government guidance.

As an output we expect an end-to-end architecture diagram produced with [**Excalidraw**](https://excalidraw.com/) that illustrates the complete solution.

You may use **Google Gemini AI** in your browser to assist with research, ideation, and architecture design however, the final architecture diagram should be your own work.

Use of any other AI tools is **not permitted** to ensure candidates are assessed fairly.

---

### Requirements

The platform must incorporate:

- The **Stamp Duty Calculator** from Part 1 for all calculations.
- A **Retrieval-Augmented Generation (RAG)** solution for guidance and question answering.
- **Official government documentation** as the primary and authoritative source of truth.

---

### Key Considerations

Examples may include but not limited to the following:

- User interface
- API layer
- AI orchestration layer
- Stamp Duty Calculator service
- RAG components
- Data stores
- Monitoring and observability

---

## Questions and Discussion - 10 minutes

Following the system design exercise, there will be 10 minutes for questions and discussion.

Candidates should be prepared to:

- Walk through their architecture from end to end.
- Explain the technologies and services they selected and why.
- Explain how the calculator and RAG solution integrate into the architecture.
- Discuss scalability, security, reliability and observability.
- Discuss trade-offs and alternative design choices.
- Explain how they would evolve the solution for production use.

<!-- TODO
- Create C3 scorecard where we expect them to give example service names from a hypervisor, selected models and why and they can google this.
- Create a separate scorecard for C2s
- Create a C2 system design boiler plate solution
- tech test for C3 grade we expect good loop solution and tests.
- tech test for C2 grade they can pass with if statements and some tests if they mention its not the best and should refactor it. -->
