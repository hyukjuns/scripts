import smtplib
from email.mime.text import MIMEText

text = "Mail Content"
msg = MIMEText(text)

msg['Subject'] = "Mail Title" # Title
msg['From'] = 'Sender Email' # Sender email
msg['To'] = 'Receiver Email' # Receiver email
print(msg.as_string())

# Set SMTP Server
s = smtplib.SMTP('smtp.naver.com', 587) # smtp server address, port
s.starttls() # TLS Setting
s.login('ID', 'App PW') # Login (ID, Application PW)

# Sender, Receiver Email Address
s.sendmail('Sender Email', 'Receiver Email', msg.as_string())
s.close()