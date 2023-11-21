from weasyprint import HTML
from datetime import date

def custom_template(*values):

    html_code = f"""
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{values[0].get("full_name")}</title>
        <style>
            /* Your external CSS styles go here */
        </style>
    </head>
    <body style="margin: 0; padding: 0; box-sizing: border-box; height: 100%; background: #eee; font-family: 'Lato', sans-serif; font-weight: 400; color: #222; font-size: 14px; line-height: 26px; padding-bottom: 50px;">

        <div style="max-width: 700px; background: #fff; margin: 0px auto 0px; box-shadow: 1px 1px 2px #DAD7D7; border-radius: 3px; padding: 40px; margin-top: 50px;">
        <div style="margin-bottom: 30px;">
            <div style="font-size: 40px; text-transform: uppercase; margin-bottom: 5px;">
                <span style="font-weight: 700;"><tt>{values[0].get("full_name")}</tt></span>
                <span></span>
            </div>
            <div style="margin-bottom: 20px;">
                <span>Email: </span>
                <span class="email-val"><tt>{values[0].get("email_id")}</tt></span>
                <span style="height: 10px; display: inline-block; border-left: 2px solid #999; margin: 0px 10px;"></span>
                <span>Phone: </span>
                <span class="phone-val"><tt>{values[0].get("phone_number")}</tt></span>
            </div>
            <div>
               <img src="{values[0].get("image_url")}" alt="person image" width="100" height="100">
               <!-- <img src="person.png" alt="person image" width="100" height="100"> -->
            </div>
            <div class="about">
                <span style="font-weight: bold; display: inline-block; margin-right: 10px; text-decoration: underline;">Front-End Developer </span>
                <span>
                    I am a front-end developer with more than 3 years of experience writing html, css, and js. I'm motivated, result-focused and seeking a successful team-oriented company with an opportunity to grow.
                </span>
            </div>
        </div>

        <div style="line-height: 20px;">
            <div style="margin-bottom: 40px;">
                <div style="letter-spacing: 2px; color: #54AFE4; font-weight: bold; margin-bottom: 10px; text-transform: uppercase;">Experience</div>
                <div>
                    Experience details go here
                </div>
            </div>

            <div style="margin-bottom: 40px;">
                <div style="letter-spacing: 2px; color: #54AFE4; font-weight: bold; margin-bottom: 10px; text-transform: uppercase;">Education</div>
                <div>
                    Education details go here 
                </div>
            </div>

            <div style="margin-bottom: 40px;">
                <div style="letter-spacing: 2px; color: #54AFE4; font-weight: bold; margin-bottom: 10px; text-transform: uppercase;">Projects</div>
                <div>
                   Projects details go here 
                </div>
            </div>

            <div style="margin-bottom: 40px;">
                <div style="letter-spacing: 2px; color: #54AFE4; font-weight: bold; margin-bottom: 10px; text-transform: uppercase;">Skills</div>
                <div>
                   Skills details go here 
                </div>
            </div>

            <div>
                <div style="letter-spacing: 2px; color: #54AFE4; font-weight: bold; margin-bottom: 10px; text-transform: uppercase;">Interests</div>
                <div>
                 Interests details go here
                    </div>
                </div>
            </div>
            </div>
        </body>
        </html>
        """

    
    file_loc = "templates/html_file"
    pdf_loc = "templates/pdf_file"
    # pdf_loc = "../../../Downloads"

    with open(f"{file_loc}/input.html", "w") as html_file:
        html_file.write(html_code)
    
    applicant_name = values[0].get("full_name")
    applicant_email = values[0].get("email_id")
    file_name = f"{applicant_name}_{date.today()}.pdf"

    HTML(f"{file_loc}/input.html").write_pdf(f"{pdf_loc}/{file_name}")
    details = {"email": applicant_email, "file": file_name}

    return  details
