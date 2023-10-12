from flask import Flask, render_template, request
from flask_mail import Mail, Message

# Create a Flask app
app = Flask(__name__)
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = "hydghani@gmail.com"
app.config["MAIL_PASSWORD"] = "ulow gnng vjjw vsvn"
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html',  methods=['GET', 'POST'])
def contact():
    if request.method == 'GET' or request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        subject = request.form.get('subject')

        msg = Message(subject, sender='hydghani@gmail.com', recipients=['hydghani@gmail.com'])
        msg.body = message
        mail.send(msg)

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
