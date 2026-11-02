# Capgemini Invent - GenAI Interview Questions

## Part 1: Technical Test - Stamp Duty Calculator

- Talk me through your approach before you start coding. What assumptions are you making?
- How did you decide what to test? What defect might your tests still miss?
- What would you change to productionise this PoC, and how would you keep the tax rules correct as they change?
- How could this be implemented as a microservice for an AI Agent?
- How could the solution be improved further given more time?
- How would you adapt your solution if there are additional cases such as buying a second home?

## Part 2: AI Task - Guidance Assistant Prompt

- What instructions would you give the assistant to keep its answers grounded in supplied guidance?
- How would you ensure it uses the calculator for every numerical calculation, including estimates and comparisons?
- What should the assistant do when required transaction details are missing or the calculator fails?
- How should it respond if a user asks about a rule that is not covered by the supplied guidance?
- How would you test and refine the prompt? Which test cases would you include?
- How would you test that user-provided instructions cannot override the assistant's role or tool-use requirements?
- Why might an LLM fail to answer a question correctly?
- How does an agent decide on what tools to use given a prompt?

## Part 3: System Design - Guidance Platform

- Walk me through your end-to-end architecture and the flow from a user's question to the answer.
- Where does the calculator run, and how do you ensure every calculation uses it as the authoritative source?
- How would you ingest, retrieve, and cite official government guidance? How would you keep it current?
- What should happen when retrieval finds no reliable answer, or when the calculator or an upstream service is unavailable?
- How would you protect user data and credentials, and monitor the platform in production?
- What trade-offs did you make in your design, and what would you change first as usage grows?
- How would you make the solution scale?
- How would tool calling be implemented? And for what purposes?
- How does RAG work, and why do we get a specific selection of documents used as an input to the LLM

## Cross-Part Follow-Ups

- What is the most important assumption in your solution, and how would you validate it?
- What is the biggest risk before launch, and how would you reduce it?
- What would you prioritize if you had more time to improve your work?
