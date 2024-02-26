#See the readme file for this repository on my github before using this code

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

#This part relates to the HTML file in the folder, file name is index.html
html = Template(Path('index.html').read_text())
email = EmailMessage()

#The part below is for the EmailMessage content imported above. Need to enter appropriate info.
email['from'] = 'YOUR NAME'
email['to'] = 'EMAIL RECIPIENT'
email['subject'] = 'EMAIL SUBJECT'

#This part links to the index.html file, can customoize the name
email.set_content(html.substitute(name= 'NAME OF RECIPIENT'), 'html')

#Connects to SMTP server (Gmail)
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    
    #enter the email address you want to log into here and the password in the second part. 
    smtp.login('YOUR EMAIL ADDRESS', 'YOUR PASSWORD')
    smtp.send_message(email)
    #add this message below so the user knows that the email was sent
    print('It worked the first time')