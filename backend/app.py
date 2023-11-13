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

def final_data(records):
    """This method is used to return data as a list of dictionaries 
    for those fields where mutiple entries are possible in the input 
    page.
    Whether it have a single data or more than one data, the final
    result will always be a list of dictionaries.
    """
    record_lis = []
    if records.count() == 1:
        record = records.first().__dict__
        record = cleaned_record(record)
        new_record = {}
        if record:
            for key,value in record.items():
                new_record[key] = str(value)
            record_lis.append(new_record)
        return record_lis
    
    elif records.count() > 1:
        for record in records.all():
            record = cleaned_record(record.__dict__)
            for key,value in record.items():
                record[key] = str(value)
            record_lis.append(record)
        return record_lis

@get("/resumes/", name="get_all_resumes")
async def show_all_data() -> json:
    """This function will fetch all resumes from the DB
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

    all_data = {}  # dictionary to store all records

    """The data in the corresponding tables are collected here to 
    their respective variables. After that the data is returned 
    in the form of a key-value pair using the 'all_data' dictionary.
    """

    # Collecting ApplicantDetails data
    applicant_record = session.query(ApplicantDetails).filter_by(id=field_id).first().__dict__
    applicant_record.pop("_sa_instance_state", None)
    all_data["applicant_details"] = applicant_record

    # Collecting AddressDetails data    
    address_record = session.query(AddressDetails).filter_by(applicant_details_id=field_id).first().__dict__
    all_data["address_details"] = cleaned_record(address_record)

    # Collecting Skills data    
    skills_record = session.query(Skills).filter_by(applicant_details_id=field_id)
    all_data["skills"] = final_data(skills_record)

    # Collecting Projects data    
    projects_record = session.query(Projects).filter_by(applicant_details_id=field_id)
    all_data["projects"] = final_data(projects_record)

    # Collecting SocialMedia data        
    media_record = session.query(SocialMedia).filter_by(applicant_details_id=field_id)
    all_data["social_media"] = final_data(media_record)
    
    # Collecting Education data       
    education_record = session.query(Education).filter_by(applicant_details_id=field_id)
    all_data["education"] = final_data(education_record)
    
    # Collecting WorkExperience data      
    work_record = session.query(WorkExperience).filter_by(applicant_details_id=field_id)
    all_data["work_experience"] = final_data(work_record)
 
    # Returning the collected data in the form of JSON
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
    """This function will save the incoming data to the DB, to their
    corresponding tables. 'applicant_details' is an object of ApplicantDetails 
    model which is used to save the data to ApplicantDetails model.
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

    #  address_details object which saves data to AddressDetails model
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
    
    # Here the values are retrieved from a nested dictionary
    # The input data resides in a list belonging to the parent dictionary.
    if data["education"]:
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

    if data["work_experience"]:
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
    
    if data["social_media"]:
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
    
    if data["skills"]:
        number_of_skills = len(data["skills"])
        for entry in range(number_of_skills):
            skills = Skills(
                applicant_details_id=data["applicant_details"].get("id"),
                skill_name=data["skills"][entry].get("skill_name"),
                skill_level=data["skills"][entry].get("skill_level")
            )
            if skills:
                session.add(skills)

    if data["projects"]:
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
                
    # The received data is commited to the database
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
