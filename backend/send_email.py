import os
import yagmail
from dotenv import load_dotenv

def send_email(details):

    file = details.get("file")
    email_id = details.get("email")

    load_dotenv()

    sender_address = os.getenv("EMAIL_ID")
    sender_password = os.getenv("EMAIL_PASSWORD")
    receiver_address = email_id

    email_sub = "Congrats! Your Resume Has Been Created"
    email_body = """
        <p>Hello,<br>
        Kindly find the resume attached with this mail.<br>
        Thank You.</p>
        """
    file_name = f"templates/pdf_file/{file}" 

    email = yagmail.SMTP(sender_address, sender_password)
    email.send(
        to=receiver_address, 
        subject=email_sub, 
        contents=email_body,
        attachments=file_name
    )
    
print("Email has been sent.")
