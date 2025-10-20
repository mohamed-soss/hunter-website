from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', year=datetime.now().year)

@app.route('/services')
def services():
    return render_template('services.html', year=datetime.now().year)

@app.route('/why-us')
def why_us():
    return render_template('why_us.html', year=datetime.now().year)

@app.route('/case-studies')
def case_studies():
    return render_template('case_studies.html', year=datetime.now().year)

@app.route('/about')
def about():
    return render_template('about.html', year=datetime.now().year)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        # Placeholder for form handling
        print(f"Contact form submitted: Name={name}, Email={email}, Phone={phone}")
    return render_template('contact.html', year=datetime.now().year)

if __name__ == '__main__':
    app.run(debug=True)