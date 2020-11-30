EMAIL_ADDRESS="letellier.henry@gmail.com"
EMAIL_LIST=["henryletellier4e4z@gmail.com","marchandirina7@gmail.com","latalliard.hanra@gmail.com","irina.marchand@hotmail.fr"]
EMAIL_PASSWORD="whrcvpgfvwokgzpo"

import smtplib
import imghdr
from email.message import EmailMessage
body="""Salut Irina, comment ca va?\nCeci est un e-mail envoyé via un script python.\nJe cherche a savoir si tu l'as recus cela m'aiderais grandement.\nMerci d'avance."""
Subject="Si tu recois, merci de bien vouloiréééé m'en informer par WhatsApp"
content="Plain Text "#"Image attached ...."


msg = EmailMessage()
msg['Subject'] = Subject
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_LIST

msg.set_content(content)
images=["HPIM5838.JPG","old cell disposing.PNG","new cell.PNG","erreur_tkcalendar_size.PNG","dimention boite.PNG"]

#for i in range(len(images)):
#    with open(images[i],"rb") as f:
#        file_data=f.read()
#        file_type=imghdr.what(f.name)
#        file_name=f.name
#        print(file_type)
#
#    msg.add_attachment(file_data,maintype='image', subtype=file_type,filename=file_name)

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_ADDRESS)
    smtp.send_message(msg)
