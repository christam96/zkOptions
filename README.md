# zkOptions

zkOptions simulates the process of exercising stock options, involving employees submitting requests, company authorization, and providing a dashboard for employees to track their requests.

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
