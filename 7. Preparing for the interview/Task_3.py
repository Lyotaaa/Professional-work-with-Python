import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def send_message_to_email(self, recipients, subject, message, protocol):
        send_message = MIMEMultipart()
        send_message["From"] = self.login
        send_message["To"] = ", ".join(recipients)
        send_message["Subject"] = subject
        send_message.attach(MIMEText(message))
        server = smtplib.SMTP(protocol + ": " + str(587))
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(send_message["From"], self.password)
        result = server.sendmail(
            send_message["From"], send_message["To"], send_message.as_string()
        )
        server.quit()
        return result

    def recieve_an_email(self, protocol, header=None):
        login_email = imaplib.IMAP4_SSL(protocol)
        login_email = login(self.login, self.password)
        login_email.list()
        login_email.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else "ALL"
        result, data = login_email.uid("search", None, criterion)
        assert data[0], "There are no letters with current header"
        latest_email_uid = data[0].split()[-1]
        result, data = login_email.uid("fetch", latest_email_uid, "(RFC822)")
        raw_email = data[0][1]
        result_query = email.message_from_string(raw_email)
        login_email.logout()
        return result_query


if __name__ == "__main__":
    login = "login@gmail.com"
    password = "qwerty"
    gmail = Email(login, password)
    recipients = ["vasya@email.com", "petya@email.com"]
    subject = "Subject"
    message = "Message"
    protocol_send = "smtp.gmail.com"
    send_message = gmail.send_message_to_email(
        recipients, subject, message, protocol_send
    )
    protocol_recieve = "imap.gmail.com"
    header = None
    recieve_message = gmail.recieve_an_email(protocol_recieve, header)
