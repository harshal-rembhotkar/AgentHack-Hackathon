# Automated Inbox Assistant - Setup Guide

Follow these steps to get the agent up and running on your local machine.

### Prerequisites

Before you begin, ensure you have the following:

1.  **Python 3.10+** installed on your system.
2.  **`uv`**, the Python package installer. If you don't have it, you can install it with:
    ```bash
    pip install uv
    ```
3.  **API Keys and Credentials**:
    * **Google API Key**: For authenticating with Gmail.
    * **Slack Channel IDs**: The specific IDs for the channels where you want to receive alerts.
    * **Portia's API key**

---

### ⚙️ Installation & Configuration

1.  **Clone the Repository**

    Open your terminal and clone this repository to your local machine:
    ```bash
    git clone <your-repository-url>
    cd <repository-directory-name>
    ```

2.  **Create Your Environment File**

    Create a file named `.env` in the root of the project directory. This file will store your secret keys and configuration variables. Copy the contents of `.env.example` (if available) or use the template below:

    ```ini
    # .env

    # Google API Key for LLM and Gmail access
    GOOGLE_API_KEY="your-google-api-key-here"

    # Slack Bot Token (starts with 'xoxb-')
    PORTIA_API_KEY="your-PORTIA_API_KEY-here"

    # ID of the primary Slack channel for general email alerts
    SLACK_CHANNEL_ID="xxxxxxxxx"

    # ID of the dedicated channel for job posting alerts
    SLACK_CHANNEL_ID2="xxxxxxxxxx"
    ```
    > **Note:** Make sure to replace the placeholder values with your actual credentials.

3.  **Install Dependencies**

    This project uses `uv` to manage dependencies. Run the following command to install all the required packages:
    ```bash
    pip install -r requirements.txt
    ```

---

### ▶️ Running the Agent

Once the setup is complete, you can start the agent with a single command:

```bash
uv run main.py
