import os
import yagmail
from dotenv import load_dotenv

def send_email(details):
    """ This function will send the resume along with
    an optional email body to the email ID recieved via
    the 'details' parameter.
    The variable details is a dictionary containing
    the email ID and file name of the PDF document.
    """

    # Fetching the file name and mail ID
    file = details.get("file")
    email_id = details.get("email")

    # Calling the dotenv function
    load_dotenv()

    # Fetching the mail ID and password from
    # .env file
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

    # Creating the email object
    email = yagmail.SMTP(sender_address, sender_password)

    # Sending the email along with content
    email.send(
        to=receiver_address, 
        subject=email_sub, 
        contents=email_body,
        attachments=file_name
    )
    
