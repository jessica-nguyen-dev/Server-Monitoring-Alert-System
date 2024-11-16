import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import settings

def send_email(subject, body, to_email):
    from_email = settings.EMAIL_USERNAME
    password = settings.EMAIL_PASSWORD

    # Create the email message (HTML)
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    html_body = f"""
    <html>
        <body>
            <h1>Alert!</h1>
            <p>{body}</p>
        </body>
    </html>
    """
    msg.attach(MIMEText(html_body, "html"))

    # This block connects to the email server, log in using the provided credentials,
    # send the email message, and then closes the connection. If an error occurs during any step,
    # it catches the exception and prints an error message.

    try:
        server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")