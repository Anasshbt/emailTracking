from pathlib import Path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
import time


sender_email = ""
password = ""
subject = "Candidature Stage PFE 2025"
csv_path = Path("C:/Users/ANASS/Desktop/Trackemail/test.csv")
html_template_path = Path(
    "C:/Users/ANASS/Desktop/Trackemail/api/templates/template.html"
)
cv_path = Path("C:/Users/ANASS/Desktop/trackemail/RESUME ANASS EL HABTI.pdf")
cover_letter_dir = Path("C:/Users/ANASS/Desktop/trackemail/Lettres")

contacts = pd.read_csv(csv_path, sep=";")

with open(html_template_path, "r", encoding="utf-8") as file:
    html_template = file.read()



def customize_html(to_name, to_email):
    return html_template.replace("{entreprise}", to_name).replace("{email}", to_email)



def send_email(to_email, to_name):
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject

   
    html_content = customize_html(to_name, to_email)
    msg.attach(MIMEText(html_content, "html"))

   
    with open(cv_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment; filename=CV_Anass.pdf")
        msg.attach(part)

    
    name = to_name.replace(" ", "_")  # Replace spaces with underscores
    cover_letter_path = (
        cover_letter_dir / f"{name}_letter.pdf"
    ) 

   

    if cover_letter_path.is_file():
        print(f"Found cover letter for {to_name}")
        with open(cover_letter_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename=Cover_Letter_{name}.pdf",
            )
            msg.attach(part)
    else:
        print(f"Cover letter not found for {name}, skipping this email.")
        return  

    
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
    print(f"E-mail sent to {to_email}!")



for _, row in contacts.iterrows():
    send_email(row["EMAILS"], row["ENTREPRISE"])
    time.sleep(3)  
