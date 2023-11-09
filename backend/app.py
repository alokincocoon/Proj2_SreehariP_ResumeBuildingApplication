import json
from typing import Any
from database import session
from litestar import Litestar, get, post, put, delete, Request
from models import ApplicantDetails, AddressDetails, Skills, Projects, Education, WorkExperience, SocialMedia

@get("/resumes/", name="get_all_resumes")
async def show_all_data() -> json:
    """This function will fetch all records from the DB
    to display in the listing page.
    """
    records = session.query(ApplicantDetails).all()
    all_records = {}
    for record in records:
        record_id = record.id
        data = record.__dict__
        data.pop("_sa_instance_state", None)
        key = f"record_{record_id}"
        value = data
        all_records[key] = value
        json_data = json.dumps(all_records)
    return json_data
    
@get("/resume/{field_id: int}", name="get_resume_by_id")
async def show_data_by_id(field_id: int) -> json:
    """This function will fetch records according to their id."""

    all_data = {}  # dict to store all records

    # for storing applicant details record
    applicant_record = session.query(ApplicantDetails).filter_by(id=field_id).first().__dict__
    applicant_record.pop("_sa_instance_state", None)
    # saving it in the dict
    all_data["applicant_details"] = applicant_record

    address_record = session.query(AddressDetails).filter_by(applicant_details_id=field_id).first().__dict__
    for key in ["_sa_instance_state", "applicant_details_id", "id"]:
        address_record.pop(key)
    all_data["address_details"] = address_record

    skills_record = session.query(Skills).filter_by(applicant_details_id=field_id).all()
    skills = []
    for item in skills_record:
        record = item.__dict__
        for key in ["_sa_instance_state", "applicant_details_id", "id"]:
            record.pop(key)
        skills.append(record)
    all_data["skills"] = skills

    projects_record = session.query(Projects).filter_by(applicant_details_id=field_id).all()
    projects = []
    for item in projects_record:
        record = item.__dict__
        for key in ["_sa_instance_state", "applicant_details_id", "id"]:
            record.pop(key)
        projects.append(record)
    all_data["projects"] = projects

    media_record = session.query(SocialMedia).filter_by(applicant_details_id=field_id).all()
    media = []
    for item in media_record:
        record = item.__dict__
        for key in ["_sa_instance_state", "applicant_details_id", "id"]:
            record.pop(key)
        media.append(record)
    all_data["social_media"] = media
   
    json_data = json.dumps(all_data)
    return json_data

@get("/find-resume/{field_val: str}", name="find_resume_by_field")
async def show_data_by_field(field_val: str) -> json:
    """This function will fetch records according to their email id."""
    record = session.query(ApplicantDetails).filter_by(email_id=field_val).first()
    data = record.__dict__
    data.pop("_sa_instance_state", None)
    json_data = json.dumps(data)
    return json_data

@post("/add-data")
async def add_data(request: Request, data:  dict[str, Any]) -> str:
    """This function will save the applicant's details 
    to the Database.
    'applicant_details' is a variable which saves data
    to ApplicantDetails model
    """
    applicant_details  = ApplicantDetails(
        id=data["applicant_details"]["id"], 
        full_name=data["applicant_details"]["full_name"], 
        email_id=data["applicant_details"]["email_id"], 
        phone_number=data["applicant_details"]["phone_number"], 
        image_url=data["applicant_details"]["image_url"], 
        summary=data["applicant_details"]["summary"]
    )
    if applicant_details:
        session.add(applicant_details)

    #  address_details variable saves data to AddressDetails model
    address_details = AddressDetails(
        applicant_details_id=data["applicant_details"]["id"],
        address_line=data["address_details"]["address_line"],
        street_name=data["address_details"]["street_name"],
        city=data["address_details"]["city"],
        country=data["address_details"]["country"],
        zip_code=data["address_details"]["zip_code"]
    )
    if address_details:
        session.add(address_details)
    
    # levels_of_education is a variable to check number of places studied
    levels_of_education = len(data["education"])
    for entry in range(levels_of_education):
        #  education variable saves data to Education model
        education = Education(
            applicant_details_id=data["applicant_details"]["id"],
            degree=data["education"]["degree"],
            stream=data["education"]["stream"],
            institute_name=data["education"]["institute_name"],
            institute_location=data["education"]["institute_location"],
            academic_year_start_date=data["education"]["academic_year_start_date"],
            academic_year_end_date=data["education"]["academic_year_end_date"]
        )
        if education:
            session.add(education)

    places_worked = len(data["work_experience"])
    for entry in range(places_worked):
        work_experience = WorkExperience(
            applicant_details_id=data["applicant_details"]["id"],
            organization=data["work_experience"][entry]["organization"],
            job_role=data["work_experience"][entry]["job_role"],
            job_location=data["work_experience"][entry]["job_location"],
            key_roles=data["work_experience"][entry]["key_roles"],
            job_start_date=data["work_experience"][entry]["job_start_date"],
            job_end_date=data["work_experience"][entry]["job_end_date"]
        )
        if work_experience:
            session.add(work_experience)

    existing_accounts = len(data["social_media"])
    for entry in range(existing_accounts):
        social_media = SocialMedia(
            applicant_details_id=data["applicant_details"]["id"],
            media_name=data["social_media"][entry]["media_name"],
            user_name=data["social_media"][entry]["user_name"],
            url=data["social_media"][entry]["url"]
        )
        if social_media:
            session.add(social_media)

    number_of_skills = len(data["skills"])
    for entry in range(number_of_skills):
        skills = Skills(
            applicant_details_id=data["applicant_details"]["id"],
            skill_name=data["skills"][entry]["skill_name"],
            skill_level=data["skills"][entry]["skill_level"]
        )
        if skills:
            session.add(skills)

    number_of_projects = len(data["projects"])
    for entry in range(number_of_projects):
        projects = Projects(
            applicant_details_id=data["applicant_details"]["id"],
            project_title=data["projects"][entry]["project_title"],
            tools_used=data["projects"][entry]["tools_used"],
            description=data["projects"][entry]["description"],     
        )
        if projects:
            session.add(projects)
      
    session.commit()
    session.close()
    return "Record added successfully."

@put("/edit-data/{applicant_id: int}")
async def edit_data(applicant_id: int, data: dict[str, Any]) -> str:
    applicant_detail_record = session.query(ApplicantDetails).filter_by(id=applicant_id).first()
   
    if applicant_detail_record:
        applicant_detail_record.full_name = data["full_name"]
        applicant_detail_record.email_id = data["email_id"]
        applicant_detail_record.phone_number = data["phone_number"]
        applicant_detail_record.image_url = data["image_url"]
        applicant_detail_record.summary = data["summary"]

    session.add(applicant_detail_record)
    session.commit()
    session.close()
    return "Updated"

@delete("/delete-data/{applicant_id: int}")
async def delete_data(applicant_id: int) -> None:
    query = session.query(ApplicantDetails).filter_by(id=applicant_id).first()
    if query:
        session.delete(query)
        session.commit()
        session.close()
        return None

app = Litestar([show_all_data, show_data_by_id, show_data_by_field, add_data, edit_data, delete_data])
