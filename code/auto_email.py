import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "ashSMTPserver@gmail.com"
#receiver_email = "a.b.pursglove@gmail.com"
receiver_email = "catycastro1987@gmail.com"
password = "AshandfidelSMTP"
message = """\
:-) !!!

Woop woop!!

xxxxxxxxxxxxxxxxxxxxxxx

"""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print("Sent")