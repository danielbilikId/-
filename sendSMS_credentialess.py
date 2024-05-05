from smtplib import SMTP 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendSMS(date, soldier_email):
    date = date
    email = 'email'
    pas = 'passowrd'
    sms_recipient = soldier_email 
    smtp = SMTP('smtp' , 587)
    smtp.starttls()
    smtp.ehlo()
    smtp.login(email, pas)
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = sms_recipient
    msg['Subject'] = "שובצת לתורנות מרפם!\n"
    body = '''<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        .header {
            background-color: #f4f4f4;
            padding: 10px;
            text-align: center;
        }
        .content {
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>!שובצת לתורנות מרפם</h1>
        </div>
        <div class="content">
            <p  style="text-align: right;">,מלשב יקר</p>
            <p  style="text-align: right;">אנו מצטערים להודיע לך כי שובצת לתפקיד קצינתו/דלפק בתאריך: ''' + date + '''<p  style="text-align: right;"> שיבוץ זה אינו ניתן לשינוי, בהצלחה</p>
            <p  style="text-align: right;">:לערעורים, פניות ובירורים יש לפנות במספר</p>
            <p  style="text-align: right;">9999999</p>
            <p  style="text-align: right;">בתודה, מיטב</p>
        </div>
    </div>
</body>
</html>'''
    # and then attach that body furthermore you can also send html content.
    msg.attach(MIMEText(body, 'html'))
    sms = msg.as_string()
    smtp.sendmail(email, sms_recipient ,sms)
    smtp.quit()
