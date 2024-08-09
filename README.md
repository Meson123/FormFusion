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

# Checkpoint 2: Implementing and Testing the Organization and User Agents
Folders: agents, protocols
## Overview

This project involves the implementation and testing of two intelligent agents: `organisation.py` and `user.py`. The `organisation.py` agent is responsible for handling and processing various forms, while the `user.py` agent interacts with it to query and submit forms. In this checkpoint, we focus on managing restaurant reservations, including both initial bookings and modifications.

## Components

### 1. `organisation.py`

The `organisation.py` script serves as the backend service that manages forms. It handles queries from the `user.py` agent and provides form details, including the fields that need to be filled out.

**Key Features:**
- Provides descriptions of available forms.
- Lists required fields for each form.
- Handles and responds to form queries from `user.py`.

### 2. `user.py`

The `user.py` script is the client-side agent that interacts with `organisation.py`. It queries form details, collects input from the user, and submits the filled form back to the `organisation.py` agent.

**Key Features:**
- Sends queries to the `organisation.py` agent to retrieve form details.
- Submits completed forms to the `organisation.py` agent.
- Receives and handles responses indicating the success or failure of the submission.

### 3. Protocol Definitions

Two protocol files, `submission.py` and `query.py`, define the communication between `organisation.py` and `user.py`.

- **`submission.py`**: Defines the structure of form submission requests and responses.
- **`query.py`**: Defines the structure of form query requests and responses.

### 4. JSON Configuration

A JSON file is used to define the details of the forms managed by `organisation.py`. This file includes the form title, description, and a list of fields that users need to fill out, such as name, email, reservation date, and more.
