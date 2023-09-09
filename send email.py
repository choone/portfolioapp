import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "jakuborafal@gmail.com"
password = "annrybwpgwbrwheq"

context = ssl.create_default_context()

receiver = "rmjakubowski@gmail.com"

message = """\
Subject: Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)

