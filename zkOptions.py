from flask import Flask, render_template, request

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
        'quantity': quantity
    }

    # Store the exercise request
    exercise_requests.append(request_data)

    return render_template('exercise_confirmation.html', request_data=request_data)

def verify_identity(employee_name, employee_id):
    # Placeholder identity verification logic; replace with identity proof logic
    return employee_name == "CT" and employee_id == "12345"

if __name__ == '__main__':
    app.run(debug=True)
