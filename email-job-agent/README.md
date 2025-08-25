# Portia AI Email Processing Agent (CLI Version)

This project is a command-line intelligent agent built with the Portia AI SDK. It automates the processing of your Gmail inbox and spam folder by classifying emails, sending alerts to Slack for important items, and creating draft replies.

This agent is built following the best practices from the official `portia-agent-examples` repository. It uses a `.env` file for secure configuration and runs directly in your terminal.

---
## 🔹 Workflow Overview

1.  **Planning**: The agent first analyzes the high-level goal and creates a detailed, step-by-step plan of action.
2.  **Execution**: The agent then executes the plan, processing your inbox and spam folder. It uses an LLM to classify emails and takes the appropriate actions (sending Slack alerts, creating Gmail drafts).
3.  **Output**: The agent prints the final JSON summary of the completed run to your terminal.

---
## 🚀 Setup and Installation

### Step 1: Clone the Project and Set Up Environment

First, clone this project and navigate into the directory. Then, create and activate a Python virtual environment.

```bash
# It is recommended to use Python 3.12
python3.12 -m venv .venv
source .venv/bin/activate