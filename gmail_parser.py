import imaplib
import email

gmail = 'ur gmaul'
password_of_gmail = 'ur password'

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(gmail, password_of_gmail)

mail.list()
mail.select("inbox")

def parser():
    result, data = mail.search(None, "ALL")

    ids = data[0]
    id_list = ids.split()
    latest_email_id = id_list[-1]

    result, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')

    email_message = email.message_from_string(raw_email_string)

    to_data = email_message['To']
    from_data = email.utils.parseaddr(email_message['From'])
    data_data = email_message['Date']
    subject_data = email_message['Subject']

    print(to_data)
    print(from_data)
    print(data_data)