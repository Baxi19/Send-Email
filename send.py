from flask import Flask
from flask_mail import Mail, Message

#You should Turning on 'less secure apps' in your Gmail
app = Flask(__name__)
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'sender@gmail.com',    #Change with your email
    "MAIL_PASSWORD": 'yourpassword'         #Change with your password
}

app.config.update(mail_settings)
mail = Mail(app)

if __name__ == '__main__':
    with app.app_context():
        msg = Message(subject="Hello From Python",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=["recipient1@gmail.com", "recipient2@gmail.com"], # replace with your email for testing
                      body="This is a test email I sent with Gmail and Python!")
        mail.send(msg)