from weasyprint import HTML
from datetime import date

def create_pdf(values):
    """ This function is used to generate a PDF
    according to the data recieved from the the 
    parameter of create_pdf function.
    The 'values' parameter is a dictionary containing
    the data required to display in the resume.
    """

    name = values.get("details").get("full_name")
    email_id = values.get("details").get("email_id")
    phone_number = values.get("details").get("phone_number")
    image_url = values.get("details").get("image_url")
    summary = values.get("details").get("summary")

    house_name = values.get("address").get("house_name")
    city = values.get("address").get("city")
    district = values.get("address").get("district")
    state = values.get("address").get("state")
    country = values.get("address").get("country")
    pin_code = values.get("address").get("zip_code")

    work = values.get("work")[0]
    education = values.get("education")[0]
    projects = values.get("projects")[0]
    skills = values.get("skills")[0]

    # The HTML code in the form of a formatted
    # string which will be used to generate
    # the HTML file of the resume.
    html_code = f"""
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{name}</title>
        <style>
            /* Your external CSS styles go here */
        </style>
    </head>
    <body style="margin: 0; padding: 0; box-sizing: border-box; height: 100%; background: #eee; font-family: 'Lato', sans-serif; font-weight: 400; color: #222; font-size: 14px; line-height: 26px; padding-bottom: 50px;">

        <div style="max-width: 700px; background: #fff; margin: 0px auto 0px; box-shadow: 1px 1px 2px #DAD7D7; border-radius: 3px; padding: 40px; margin-top: 50px;">
        <div style="margin-bottom: 30px;">
            <div style="font-size: 40px; text-transform: uppercase; margin-bottom: 5px;">
                <span style="font-weight: 700;"><tt>{name}</tt></span>
                <span></span>
        </div>

        <div style="margin-bottom: 20px;">
                <span>Email: </span>
                <span class="email-val"><tt>{email_id}</tt></span>
                <span style="height: 10px; display: inline-block; border-left: 2px solid #999; margin: 0px 10px;"></span>
                <span>Phone: </span>
                <span class="phone-val"><tt>{phone_number}</tt></span>
        </div>
        
        
        <div style="margin-bottom: 20px;">
        <a href="{image_url}">
               <img src="{image_url}" alt="Profile Picture" width="100" height="100">
               <!-- <img src="person.png" alt="person image" width="100" height="100"> -->
        </a>
        </div>

            
        <div style="line-height: 20px;">
            <div style="margin-bottom: 20px;">
                <div style="letter-spacing: 2px; color: #54AFE4; font-weight: bold; margin-bottom: 10px; text-transform: uppercase;">Address</div>
                <div>
                    <tt>{house_name}</tt><br>
                    <tt>{city}</tt>,&nbsp;
                    <tt>{district}</tt><br>
                    <tt>{state}</tt><br>
                    <tt>{country}</tt><br>
                    <tt>PIN: {pin_code}</tt><br>
                </div>
        </div>
        
        <div style="line-height: 20px;">
            <div style="margin-bottom: 20px;">
                <div style="letter-spacing: 2px; color: #54AFE4; font-weight: bold; margin-bottom: 10px; text-transform: uppercase;">Summary</div>
                <div>
                    {summary}
                </div>
        </div>

        <div style="margin-bottom: 20px;">
                <div style="letter-spacing: 2px; color: #54AFE4; font-weight: bold; margin-bottom: 10px; text-transform: uppercase;">Education</div>
                <div>
                    <tt>{education.get("degree")}</tt>&nbsp;
                    <tt>{education.get("stream")}</tt><br>
                    <tt>{education.get("institute_name")}</tt><br>
                    <tt>{education.get("institute_location")}</tt><br>
                    <tt>From: {education.get("academic_year_start_date")}</tt><br>
                    <tt>To: {education.get("academic_year_end_date")}</tt>
                </div>
            </div>

        <div style="line-height: 20px;">
            <div style="margin-bottom: 20px;">
                <div style="letter-spacing: 2px; color: #54AFE4; font-weight: bold; margin-bottom: 10px; text-transform: uppercase;">Experience</div>
                <div>
                    <tt>Organization: {work.get("organization")}</tt><br>
                    <tt>Job Role: {work.get("job_role")}</tt><br>
                    <tt>Location: {work.get("job_location")}</tt><br>
                    <tt>Key Roles: {work.get("key_roles")}</tt><br>
                    <tt>From: {work.get("job_start_date")}</tt><br>
                    <tt>To: {work.get("job_end_date")}</tt><br>
                </div>
            </div>

            <div style="margin-bottom: 20px;">
                <div style="letter-spacing: 2px; color: #54AFE4; font-weight: bold; margin-bottom: 10px; text-transform: uppercase;">Projects</div>
                <div>
                   <tt>Title: {projects.get("project_title")}</tt><br>
                   <tt>SKills Earned: {projects.get("tools_used")}</tt><br>
                   <tt>Description: {projects.get("description")}</tt><br>
                </div>
            </div>

            <div style="margin-bottom: 20px;">
                <div style="letter-spacing: 2px; color: #54AFE4; font-weight: bold; margin-bottom: 10px; text-transform: uppercase;">Skills</div>
                <div>
                   <tt>Skill: {skills.get("skill_name")}</tt><br>
                   <tt>Level: {skills.get("skill_level")}</tt><br>
                </div>
            </div>

           
            </div>
            </div>
        </body>
        </html>
        """

    # The location where HTML and PDF file is to
    # be generated
    file_loc = "templates/html_file"
    pdf_loc = "templates/pdf_file"
    # pdf_loc = "../../../Downloads"

    # Generating the HTML file using the above mentioned code
    with open(f"{file_loc}/input.html", "w") as html_file:
        html_file.write(html_code)
    
    # File name for PDF document
    file_name = f"{name}_{date.today()}.pdf"
    
    # Generating the PDF document
    HTML(f"{file_loc}/input.html").write_pdf(f"{pdf_loc}/{file_name}")

    # Returning the email id and file name as a dict
    details = {"email": email_id, "file": file_name}
    return  details
