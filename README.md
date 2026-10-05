# Capgemini Invent – GenAI Interview

## Assessment Overview

The assessment is divided into three parts:

1. **Technical Test**
2. **AI Task**
3. **System Design**

---

# Part 1: Technical Test

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

---

# Part 2: AI Task

## AI-Powered Stamp Duty Guidance Assistant

### Objective

Create a prompt for an AI assistant that helps users understand Stamp Duty regulations and calculations.

---

### Requirements

The assistant should:

- Explain Stamp Duty rules and tax bands.
- Answer user questions about Stamp Duty.
- Verify calculations when requested.
- Use the **Stamp Duty Calculator** from Part 1 as a trusted calculation tool.
- Invoke the calculator whenever a calculation is required instead of performing calculations independently.

---

### Key Considerations

- The calculator should be treated as the **authoritative source** for all tax calculations.
- You will **not** run the prompt, we are interesting in the thought behind developing the prompt rather than the actual result.

---

# Part 3: System Design

## AI-Powered Stamp Duty Guidance Platform

### Objective

Design a scalable, production-ready platform that helps users:

- Understand Stamp Duty rules.
- Verify Stamp Duty calculations.
- Ask natural language questions about Stamp Duty.
- Receive answers based on trusted government guidance.

As an output we expect an end-to-end architecture diagram produced with [**Draw.io**](https://app.diagrams.net/) that illustrates the complete solution.

You may use **Google Gemini AI** in your browser to assist with research, ideation, and architecture design however, the final architecture diagram should be your own work.

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
