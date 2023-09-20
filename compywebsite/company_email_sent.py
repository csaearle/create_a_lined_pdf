import smtplib, ssl


def send_company_email(message):
    username = "csaearle69@gmail.com"
    password = "awypykhzvkcoyxgp"
    receiver = "csaearle69@gmail.com"
    context = ssl.create_default_context()
    host = "smtp.gmail.com"
    port = 465
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


#send_company_email(message)