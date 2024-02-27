# zkOptions

zkOptions simplifies the process of exercising stock options, involving employees submitting requests, company authorization, and providing a dashboard for employees to track their requests.
![zkOptions](https://github.com/christam96/zkOptions/assets/20301223/007565c1-5494-4bd1-8979-99dae4ae5a00)

## Requirements
- Python
- Pipenv

## Installation
1. Clone the repository
2. Navigate to the project directory

```bash
cd path/to/project
```

3. Install dependencies using Pipenv

```bash
pipenv install
```

## Running the App

Run the Flask App:

```bash
pipenv run python zkOptions.py
```

Below is the flow of how to use the application:

1. Access the Application:
    Open the application in a web browser.

2. Submit Exercise Options Request: On the main page (index.html), fill out the form with the required information
```
Employee Name
Employee ID (Identity Proof)
Stock Symbol
Quantity
```

4. Confirmation of Request Submission:
    - After submitting the form, you will be redirected to the confirmation page (`exercise_confirmation.html`).
    - The page will display details of the submitted request, including the employee's name, employee ID, stock symbol, quantity, and the initial status set to 'Pending'.
    - If there are any issues with the submission, an error message will be displayed using the error.html template.

6. Company Authorization:
    - The company can access the /company_authorization route to view a dashboard (`company_authorization.html`) listing all pending exercise options requests.
    - For each request, the company can choose to authorize or deny the request using the provided links.
    - If authorized, the status of the request is updated to 'Approved'.

7. Treasury Direction Form:
    - Upon company authorization, the application generates a Treasury Direction form using the `treasury_direction_form.html` page.
    - This form includes key details such as the employee's name, employee ID, stock symbol, and quantity.

8. Employee Dashboard:
    - Employees can view a dashboard (`employee_dashboard.html`) listing all of their exercise options requests.
    - The dashboard displays a table with columns for stock symbol, quantity, and status for each submitted request.

9. Track Request Status:
    - Employees can track the status of their requests on the dashboard. The status can be 'Pending' if awaiting company authorization or 'Approved' if the company has authorized the request.

## Demo
**http://127.0.0.1:5000/:**

- Form submission page
- Employee provides details, initiates exercise options request
<img width="468" alt="Exercise Options Request" src="https://github.com/christam96/zkOptions/assets/20301223/c16b068d-7ae2-44f1-8394-053906a7b85f">

**exercise_options.html:**

- Confirmation page after form submission.
- Displays employee's name, ID, stock symbol, quantity, and initial status ('Pending')
- Redirects after successful submission; error message for issues
<img width="543" alt="Exercise Options Confirmation" src="https://github.com/christam96/zkOptions/assets/20301223/0850745c-7714-4772-97a0-a5a1e5ec5233">

**company_authorization.html:**

- Dashboard for company authorization
- Lists pending exercise options requests
- Company decides to authorize or deny each request
<img width="616" alt="Company Authorization" src="https://github.com/christam96/zkOptions/assets/20301223/4799d39b-62e4-407d-b8a4-c7636e20a93f">

**treasury_direction_form.html:**

- Treasury Direction form
- Generated upon company authorization
- Includes employee's name, ID, stock symbol, and quantity
<img width="440" alt="TD Form" src="https://github.com/christam96/zkOptions/assets/20301223/b285bd06-e9ba-40d9-9f14-474b7fc9ed7b">

**employee_dashboard.html:**

- Employee's dashboard 
- Displays all exercise options requests
- Features a table with columns for stock symbol, quantity, and status
<img width="412" alt="Request Dashboard" src="https://github.com/christam96/zkOptions/assets/20301223/cbd6cba3-5430-4fff-a113-b092168dce47">

