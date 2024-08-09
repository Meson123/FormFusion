import json
from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
from protocols.submission import submit_proto
from protocols.query import query_proto, FormStatus

class OrganizationAgent:
    def __init__(self):
        self.forms = {}
        self.agent = Agent(
            name="organisation",
            port=2257,  # Ensure this port is not used by any other process
            seed="org secret phrase",
            endpoint=["http://127.0.0.1:2257/submit"],
        )
        print("Initializing agent...")
        fund_agent_if_low(self.agent.wallet.address())
        self.agent.include(query_proto)
        self.agent.include(submit_proto)
        print("Agent initialized and protocols included.")

    def add_form(self, form_title, description, organizing_body, fields):
        form_status = FormStatus(
            body=description,
            title=form_title,
            description=description,
            fields=fields
        ).dict()
        self.forms[form_title] = form_status

        try:
            print(f"Attempting to save form '{form_title}'...")
            self.agent._storage.set(form_title, form_status)
            print(f"Form '{form_title}' saved successfully.")
        except Exception as e:
            print(f"Error saving form data: {e}")

    def get_form_description(self, form_title):
        form = self.forms.get(form_title)
        if form:
            return form.get("description", "Description not available.")
        return "Form not found."

    def get_form_fields(self, form_title):
        form = self.forms.get(form_title)
        if form:
            return form.get("fields", "Fields not available.")
        return "Form not found."

    def get_form_organization(self, form_title):
        form = self.forms.get(form_title)
        if form:
            return form.get("organization", "Organization not specified.")
        return "Form not found."

    def prompt_user_for_form(self):
        user_input = input("Would you like to create a new form? (yes/no): ").strip().lower()
        if user_input == 'yes':
            form_title = input("Please enter the form title: ").strip()
            description = input("Please provide the description of the form: ").strip()
            organizing_body = input("Please enter the organizing body: ").strip()
            fields = input("Please enter the fields required (comma separated): ").strip().split(',')

            self.add_form(form_title, description, organizing_body, fields)

            print("\nForm Created:")
            print(f"Title: {form_title}")
            print(f"Description: {description}")
            print("Fields required: ", ", ".join(fields))
            print("Please provide your name, roll no, and contact department.")
        else:
            print("No form created.")

# Example usage
if __name__ == "__main__":
    print("Starting OrganizationAgent...")
    agent = OrganizationAgent()
    agent.prompt_user_for_form()
    print("Running agent...")
    agent.agent.run()
