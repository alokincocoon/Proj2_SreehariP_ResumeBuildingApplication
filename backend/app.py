import json
from typing import Any
from database import session
from litestar import Litestar, get, post, put, delete, Request
from models import ApplicantDetails, AddressDetails, Skills, Projects, Education, WorkExperience, SocialMedia

def cleaned_record(record):
    """This method will clean the incoming record by removing 
    the un-necessary keys and it's values.
    """
    for key in ["_sa_instance_state", "applicant_details_id", "id"]:
        record.pop(key)
    return record

def list_of_dict(records):
    """This method will return a list of dictionary if
    there are multiple records present in a table which 
    is related to a single id.
    """
    final_list = []
    for item in records:
        record = item.__dict__
        record = cleaned_record(record)
        final_list.append(record)
    return final_list

def final_data(record):
    """This method will return the data as a dictionary if
    only a single record exists in the table belonging to an id
    or else it will return a list of dictionary as data.
    """
    if record.count() == 1:
        record = cleaned_record(record.first().__dict__)
    else:
        record = list_of_dict(record.all())
    return record

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
    all_data["address_details"] = cleaned_record(address_record)

    skills_record = session.query(Skills).filter_by(applicant_details_id=field_id)
    all_data["skills"] = final_data(skills_record)

    projects_record = session.query(Projects).filter_by(applicant_details_id=field_id)
    all_data["projects"] = final_data(projects_record)

    media_record = session.query(SocialMedia).filter_by(applicant_details_id=field_id)
    all_data["social_media"] = final_data(media_record)
    
    education_record = session.query(Education).filter_by(applicant_details_id=field_id)
    # print(type(education_record))
    # print(final_data(education_record))
    # all_data["education"] = final_data(education_record)

    work_record = session.query(WorkExperience).filter_by(applicant_details_id=field_id)
    # all_data["work_experience"] = final_data(work_record)

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

@post("/new-resume")
async def add_data(request: Request, data:  dict[str, Any]) -> str:
    """This function will save the applicant's details 
    to the Database.
    'applicant_details' is a variable which saves data
    to ApplicantDetails model.
    """
    applicant_details  = ApplicantDetails(
        id=data["applicant_details"].get("id"), 
        full_name=data["applicant_details"].get("full_name"), 
        email_id=data["applicant_details"].get("email_id"), 
        phone_number=data["applicant_details"].get("phone_number"), 
        image_url=data["applicant_details"].get("image_url"), 
        summary=data["applicant_details"].get("summary")
    )
    if applicant_details:
        session.add(applicant_details)

    #  address_details variable saves data to AddressDetails model
    address_details = AddressDetails(
        applicant_details_id=data["applicant_details"].get("id"),
        address_line=data["address_details"].get("address_line"),
        street_name=data["address_details"].get("street_name"),
        city=data["address_details"].get("city"),
        country=data["address_details"].get("country"),
        zip_code=data["address_details"].get("zip_code")
    )
    if address_details:
        session.add(address_details)
    
    if type(data["education"]) is list:
        levels_of_education = len(data["education"])
        for entry in range(levels_of_education):
            education = Education(
                applicant_details_id=data["applicant_details"].get("id"),
                degree=data["education"][entry].get("degree"),
                stream=data["education"][entry].get("stream"),
                institute_name=data["education"][entry].get("institute_name"),
                institute_location=data["education"][entry].get("institute_location"),
                academic_year_start_date=data["education"][entry].get("academic_year_start_date"),
                academic_year_end_date=data["education"][entry].get("academic_year_end_date")
            )
            if education:
                session.add(education)
    else:
        education = Education(
            applicant_details_id=data["applicant_details"].get("id"),
            degree=data["education"].get("degree"),
            stream=data["education"].get("stream"),
            institute_name=data["education"].get("institute_name"),
            institute_location=data["education"].get("institute_location"),
            academic_year_start_date=data["education"].get("academic_year_start_date"),
            academic_year_end_date=data["education"].get("academic_year_end_date")
        )
        if education:
            session.add(education) 

    if type(data["work_experience"]) is list:
        places_worked = len(data["work_experience"])
        for entry in range(places_worked):
            work_experience = WorkExperience(
                applicant_details_id=data["applicant_details"].get("id"),
                organization=data["work_experience"][entry].get("organization"),
                job_role=data["work_experience"][entry].get("job_role"),
                job_location=data["work_experience"][entry].get("job_location"),
                key_roles=data["work_experience"][entry].get("key_roles"),
                job_start_date=data["work_experience"][entry].get("job_start_date"),
                job_end_date=data["work_experience"][entry].get("job_end_date")
            )
            if work_experience:
                session.add(work_experience)
    else:
        work_experience = WorkExperience(
                applicant_details_id=data["applicant_details"].get("id"),
                organization=data["work_experience"].get("organization"),
                job_role=data["work_experience"].get("job_role"),
                job_location=data["work_experience"].get("job_location"),
                key_roles=data["work_experience"].get("key_roles"),
                job_start_date=data["work_experience"].get("job_start_date"),
                job_end_date=data["work_experience"].get("job_end_date")
            )
        if work_experience:
            session.add(work_experience)
    
    if type(data["social_media"]) is list:
        existing_accounts = len(data["social_media"])
        for entry in range(existing_accounts):
            social_media = SocialMedia(
                applicant_details_id=data["applicant_details"].get("id"),
                media_name=data["social_media"][entry].get("media_name"),
                user_name=data["social_media"][entry].get("user_name"),
                url=data["social_media"][entry].get("url")
            )
            if social_media:
                session.add(social_media)
    else:
        social_media = SocialMedia(
                applicant_details_id=data["applicant_details"].get("id"),
                media_name=data["social_media"].get("media_name"),
                user_name=data["social_media"].get("user_name"),
                url=data["social_media"].get("url")
            )
        if social_media:
                session.add(social_media)
    
    if type(data["skills"]) is list:
        number_of_skills = len(data["skills"])
        for entry in range(number_of_skills):
            skills = Skills(
                applicant_details_id=data["applicant_details"].get("id"),
                skill_name=data["skills"][entry].get("skill_name"),
                skill_level=data["skills"][entry].get("skill_level")
            )
            if skills:
                session.add(skills)
    else:
        skills = Skills(
            applicant_details_id=data["applicant_details"].get("id"),
            skill_name=data["skills"].get("skill_name"),
            skill_level=data["skills"].get("skill_level")
        )
        if skills:
            session.add(skills)

    if type(data["projects"]) is list:
        number_of_projects = len(data["projects"])
        for entry in range(number_of_projects):
            projects = Projects(
                applicant_details_id=data["applicant_details"].get("id"),
                project_title=data["projects"][entry].get("project_title"),
                tools_used=data["projects"][entry].get("tools_used"),
                description=data["projects"][entry].get("description"),     
            )
            if projects:
                session.add(projects)
    else:
        projects = Projects(
                applicant_details_id=data["applicant_details"].get("id"),
                project_title=data["projects"].get("project_title"),
                tools_used=data["projects"].get("tools_used"),
                description=data["projects"].get("description"),     
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

@delete("/delete-resume/{applicant_id: int}")
async def delete_data(applicant_id: int) -> None:
    query = session.query(ApplicantDetails).filter_by(id=applicant_id).first()
    if query:
        session.delete(query)
        session.commit()
        session.close()
        return None

app = Litestar([show_all_data, show_data_by_id, show_data_by_field, add_data, edit_data, delete_data])
