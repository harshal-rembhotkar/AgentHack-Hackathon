# Automated Inbox Assistant

**This is an autonomous AI agent, built with the Portia AI SDK, that transforms your inbox from a chore into a command center and proactively finds your next career opportunity while you focus on what matters.**

### 🎯 Potential Impact

In a world of constant digital noise, this agent addresses two of the most significant productivity drains for any professional: managing email overload and conducting a job search.

This agent doesn't just filter emails; it understands them. It doesn't just find jobs; it delivers curated opportunities directly to you. By automating these high-volume, low-focus tasks, the Automated Inbox Assistant frees up hours of valuable time each week, reducing stress and allowing users to focus on high-impact work, meaningful connections, and interview preparation. It turns a reactive, manual process into a proactive, automated workflow, creating a significant positive impact on daily productivity and long-term career growth.

### 🎨 Creativity & Originality

This agent stands out by creatively orchestrating a suite of tools to create a seamless, hybrid automation workflow that bridges the gap between structured APIs and the unstructured web.

* **Intelligent Triage:** It uses an LLM not just for summarization, but as a core **decision-making engine** to classify emails and determine the appropriate next action (alert, draft, or ignore). This moves beyond simple rule-based filtering into nuanced, content-aware automation.

* **API-to-Browser Synthesis:** The agent fluidly transitions from making precise API calls to Gmail and Slack to launching a **fully autonomous browser session**. It navigates a real-world job site (Wellfound), performs searches, and scrapes data—a novel combination that demonstrates a sophisticated level of automation.

* **Proactive & Reactive Intelligence:** It operates in two modes simultaneously: **reacting** to incoming information (emails) and **proactively** seeking out new information (job hunting), creating a comprehensive and truly helpful digital assistant.

### 🌱 Learning & Growth

This project was an ambitious dive into the world of AI agents and automation. Our key learning was in the art of **prompt architecture**. Our initial approach with a single, monolithic prompt for the agent led to planning failures, as the complexity overwhelmed the AI's ability to generate a valid step-by-step plan.

This challenge forced us to learn a crucial lesson in agentic design: **decomposition**. By breaking down the complex goal into smaller, sequential, and more focused tasks, we were able to guide the Portia planning agent to success. This iterative process of refining the prompt taught us how to "think" like an agent and was a significant step in our journey from simple scripting to building robust, multi-step AI systems. We also navigated the complexities of managing authentication for multiple services, a foundational skill for any real-world AI application.

### 🛠️ Implementation of the Idea

The Automated Inbox Assistant is built using the **Portia AI SDK**, leveraging its powerful natural language planning and tool-use capabilities to translate a high-level goal into an executable, multi-step plan. The idea was executed effectively by integrating several key components:

* **The Orchestrator (`main.py`):** The central script that defines the agent's configuration and its ultimate goal in a clear, human-readable format.

* **The Brain (Google's LLM via Portia):** The agent uses a Large Language Model for the complex classification and decision-making tasks, making it adaptable and intelligent.

* **The Toolkit:** A versatile set of tools are employed to interact with the digital world:

    * `google_gmail`: For reading the inbox and spam folders, and drafting replies.

    * `slack`: For sending real-time, critical alerts.

    * `browser`: For navigating, searching, and scraping job information from websites.

The agent functions exactly as intended, successfully processing emails and searching for jobs based on the initial natural language prompt. This demonstrates a strong and effective use of Portia's core features to build a functional, multi-faceted AI agent.
