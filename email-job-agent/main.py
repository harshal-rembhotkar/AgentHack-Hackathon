import os
import json
from dotenv import load_dotenv
from portia import Config, DefaultToolRegistry, Portia, LLMProvider
from portia.cli import CLIExecutionHooks
from portia.open_source_tools.browser_tool import (
    BrowserInfrastructureOption,
    BrowserTool,
)

browser_tool = BrowserTool(
    infrastructure_option=BrowserInfrastructureOption.LOCAL
)


load_dotenv(override=True)

def main():
    """
    The main function that sets up and runs the email processing agent.
    """
    print("🤖 Starting the Portia Email Agent...")

    my_config = Config.from_default(llm_provider="google")

    portia = Portia(
        config=my_config,
        tools=DefaultToolRegistry(my_config) + [browser_tool],
        execution_hooks=CLIExecutionHooks(),
    )

    # Get the Slack channel ID from the environment to use in the prompt.
    slack_channel = os.getenv("SLACK_CHANNEL_ID")
    slack_channel2 = os.getenv("SLACK_CHANNEL_ID2")
    
    
    task = f"""
    Your primary goal is to process my Gmail inbox and spam folder.

    1.  **Process Inbox**:
        - Use the `google_gmail-search_email` tool to find unread emails from the last 7 days. The query is `is:unread newer_than:7d`.
        - For each email found, use the `llm` tool to classify its content (subject and snippet) into one of these categories: `Promotions`, `Personal`, `Jobs`, `Sales`.
        - Based on the classification, perform an action:
            - If the category is `Jobs`, use the `slack-send_message` tool to send an alert to the channel ID '{slack_channel}'. The message must be: "📢 Job email detected: {{subject}} -> https://mail.google.com/mail/u/0/#inbox/{{thread_id}}".
            - If the category is `Personal` or `Sales`, use the `google_gmail-draft_email` tool to create a draft reply. The draft body should be something like "Thanks for reaching out, I’ll get back to you soon.".
            - For all other categories, do nothing.

    2.  **Process Spam Folder**:
        - Use `google_gmail-search_email` to find unread emails in the spam folder from the last 14 days. The query is `in:spam is:unread newer_than:14d`.
        - For each spam email, use the `llm` tool to classify if it is `Maybe Important` or `Ignore`.
        - If an email is `Maybe Important`, use `slack-send_message` to send an alert to '{slack_channel}': "⚠️ Important email found in Spam: {{subject}} -> https://mail.google.com/mail/u/0/#spam/{{message_id}}".

    3. **Search for Jobs on Wellfound**:
        - Use the `browser` tool to first navigate to 'https://wellfound.com/jobs'.
        - On the page, perform a search for jobs with the keywords "software engineer" and then "backend engineer".
        - For the top 5 job postings you find for each search, extract the job title and the direct link (URL) to the job posting.
        - For each job you find, use the `slack-send_message` tool to send an alert to the dedicated jobs channel with ID '{slack_channel2}'. The message must be: " New Job Posting Found on Wellfound: {{job_title}} -> {{job_link}}".
           
    4. **Final Step**:
        - After completing all tasks, create and output a final JSON summary of all actions taken.
    """
    
    print(" Task defined. Generating a plan...")
    
    # Step 1: Generate the plan from the user query.
    plan = portia.plan(task)
    print(" Plan generated successfully.")
    
    # Step 2: Execute the generated plan.
    print(" Executing the plan...")
    plan_run = portia.run_plan(plan)

    print("\n✅ Agent run complete!")
    print("\n--- Agent Result ---")
    print(plan_run.model_dump_json(indent=2))



if __name__ == "__main__":
    
    main()