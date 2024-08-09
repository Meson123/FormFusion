class OrganizationAgent:
    def __init__(self):
        self.forms = {}

    def add_form(self, form_title, description, organizing_body, fields):
        self.forms[form_title] = {
            "description": description,
            "organization": organizing_body,
            "fields": fields
        }

    def get_form_description(self, form_title):
        form = self.forms.get(form_title)
        if form:
            return form["description"]
        return "Form not found."

    def get_form_fields(self, form_title):
        form = self.forms.get(form_title)
        if form:
            return form["fields"]
        return "Form not found."

    def get_form_organization(self, form_title):
        form = self.forms.get(form_title)
        if form:
            return form["organization"]
        return "Form not found."

    def prompt_user_for_form(self):
        user_input = input("Would you like to create a new form? (yes/no): ").strip().lower()
        if user_input == 'yes':
            form_title = input("Please enter the form title: ").strip()
            description = input("Please provide the description of the form: ").strip()
            organizing_body = input("Please enter the organizing body: ").strip()
            fields = input("Please enter the fields required (comma separated): ").strip().split(',')

            self.add_form(form_title, description, organizing_body, fields)

            print("\nHi..")
            print(f"Here's a form for the {form_title} domain by {organizing_body}")
            print(f"{description}")
            print("Kindly provide your {fields}.")

        else:
            print("No form created.")

# Example usage
if __name__ == "__main__":
    agent = OrganizationAgent()
    agent.prompt_user_for_form()
