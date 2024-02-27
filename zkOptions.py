from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Placeholder for storing exercise requests
exercise_requests = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exercise_options', methods=['POST'])
def exercise_options():
    # Get form data
    employee_name = request.form['employee_name']
    employee_id = request.form['employee_id']
    stock_symbol = request.form['stock_symbol']
    quantity = int(request.form['quantity'])

    # Verify identity (you may implement a more robust verification process)
    if not verify_identity(employee_name, employee_id):
        return render_template('identity_verification_failed.html', employee_name=employee_name)

    # Create exercise request
    request_data = {
        'employee_name': employee_name,
        'employee_id': employee_id,
        'stock_symbol': stock_symbol,
        'quantity': quantity,
        'status': 'Pending'
    }

    # Store the exercise request
    exercise_requests.append(request_data)

    # return render_template('exercise_confirmation.html', request_data=request_data)

    # Request authorization from the company
    authorization_status = request_company_authorization(request_data)

    if authorization_status:
        return render_template('exercise_confirmation.html', request_data=request_data, authorized=True)
    else:
        return render_template('exercise_confirmation.html', request_data=request_data, authorized=False)

@app.route('/company_authorization')
def company_authorization():
    print(exercise_requests)
    return render_template('company_authorization.html', exercise_requests=exercise_requests)

@app.route('/authorize_request/<int:request_index>')
def authorize_request(request_index):
    # Placeholder for actual company authorization logic
    # For example, you might update the status in a database or contact relevant personnel
    exercise_requests[request_index]['status'] = 'Approved'
    return redirect(url_for('company_authorization'))

@app.route('/deny_request/<int:request_index>')
def deny_request(request_index):
    # Placeholder for denying the request
    exercise_requests[request_index]['status'] = 'Denied'
    return redirect(url_for('company_authorization'))

def verify_identity(employee_name, employee_id):
    # Placeholder identity verification logic; replace with identity proof logic
    return employee_name == "CT" and employee_id == "12345"

def request_company_authorization(request_data):
    # Placeholder for company authorization logic
    # You can implement your own logic to request and check authorization
    # For example, you might check with an internal system or contact relevant personnel
    return True  # Placeholder, assuming authorization is always granted

if __name__ == '__main__':
    app.run(debug=True)
