import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "jakuborafal@gmail.com"
    password = "annrybwpgwbrwheq"
    context = ssl.create_default_context()
    receiver = "jakuborafal@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


