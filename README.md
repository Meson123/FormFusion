# Checkpoint 1
File: organisation.py
# Functions
We used the class OrganisationAgent to manage this form within the organisation in order to allow users to add new forms or to retreive form details. 
1. _init_ function <br/>
   We used this function to contain the variable self.forms and each entry under this contains description, organisation and fields.
2. add_form function <br/>
   We used this to add a new form to self.forms with the defined parameters with form.title as the key.
3. get_form_description, get_form_fields, get_form_organization, prompt_user_for_form functions <br/>
   these functions retrieve the information related to the corresponding field
Lastly, we take a user prompt to print.
When we give yes as a user input, it prompts for the 4 functions.
THen it calls to add_form to add a new form to self.forms and then prints a greeting and the details of the newly created form.
If user gives no as input, it indicates that no form was created.

# Variables
1. self.forms <br/>
it is a dictionary to store form details using form_title as key

2. description <br/>
Stores the description of the form, and is a key.

3. organisation <br/>
Stores the name of the organisation for the form, and is a key.

4. fields <br/>
Stores the fields of the form, and is a key.

# Checkpoint 2
Folders: agents, protocols
# Issue: Form Submission Data Storage Issue
## Steps Involved
1. Agent Definition: We have created an agent called user with the specified parameters.
2. Funding: The agent's wallet is funded if it has a low balance so that it is ensured that it can perform the required actions
3. Protocols: used to handle query and submission related tasks.
4. Defining the form: a dictionary named FORMS is created and stored in the agent's local storage, and run if the script is executed directly.
5. 

