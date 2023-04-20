from configparser import ConfigParser
from Task_3 import Email
from pprint import pprint


def open_a_token(file_name):
    cofing = ConfigParser()
    cofing.read(file_name)
    login = cofing["token_info"]["login"]
    password = cofing["token_info"]["password"]
    recipients = cofing["token_info"]["recipients"]
    return login, password, recipients.split(",")


if __name__ == "__main__":
    login_info = open_a_token("confing.ini")
    login = login_info[0]
    password = login_info[1]
    gmail = Email(login, password)
    recipients = login_info[2]
    subject = "LOL"
    message = "KEK"
    protocol_send = "smtp.gmail.com"
    send_message = gmail.send_message_to_email(
        recipients, subject, message, protocol_send
    )
    print(send_message)
    protocol_recieve = "imap.gmail.com"
    recieve_message = gmail.recieve_an_email(protocol_recieve)
    print(*recieve_message, sep="\n")
