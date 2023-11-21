import os
import json
from typing import Any
from database import session
from pyhtml2pdf import converter
from psycopg2.errors import InvalidDatetimeFormat
from litestar.config.cors import CORSConfig
from litestar import Litestar, get, post, put, delete, Request
from models import (
    ApplicantDetails,
    AddressDetails,
    Skills,
    Projects,
    Education,
    WorkExperience,
    SocialMedia,
)
from pathlib import Path
from litestar.response import Template
from litestar.template.config import TemplateConfig
from litestar.contrib.jinja import JinjaTemplateEngine
from create_pdf import custom_template
from send_email import send_email


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
            for key, value in record.items():
                new_record[key] = str(value)
            record_lis.append(new_record)
        return record_lis

    elif records.count() > 1:
        for record in records.all():
            record = cleaned_record(record.__dict__)
            for key, value in record.items():
                record[key] = str(value)
            record_lis.append(record)
        return record_lis


@get("/resumes/", name="get_all_resumes")
async def show_all_resumes() -> json:
    """This function will fetch all resumes from the DB
    to display in the listing page.
    """
    records = session.query(ApplicantDetails).all()
    if records:
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
async def show_resume_by_id(field_id: int) -> json:
    """This function will fetch records according to their id."""

    all_data = {}  # dictionary to store all records

    """The data in the corresponding tables are collected here to 
    their respective variables. After that the data is returned 
    in the form of a key-value pair using the 'all_data' dictionary.
    """
    try:
        # Collecting ApplicantDetails data
        applicant_record = (
            session.query(ApplicantDetails).filter_by(id=field_id).first().__dict__
        )
        applicant_record.pop("_sa_instance_state", None)
        all_data["applicant_details"] = applicant_record

        # Collecting AddressDetails data
        address_record = (
            session.query(AddressDetails)
            .filter_by(applicant_details_id=field_id)
            .first()
            .__dict__
        )
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
    except:
        return json.dumps("Record doesnt exist")


@get("/find-resume/{field_val: str}", name="find_resume_by_field")
async def show_resume_by_field(field_val: str) -> json:
    """This function will fetch records according to their email id."""
    record = session.query(ApplicantDetails).filter_by(email_id=field_val).first()
    data = record.__dict__
    data.pop("_sa_instance_state", None)
    json_data = json.dumps(data)
    return json_data


@get("/download/{field_id: int}")
async def download_resume(field_id: int) -> str:
    details = session.query(ApplicantDetails).filter_by(id=field_id).first().__dict__
    address = (
        session.query(AddressDetails)
        .filter_by(applicant_details_id=field_id)
        .first()
        .__dict__
    )
    email_data = custom_template(details, address)
    send_email(email_data)
    return "Downloaded"
    # return Template(template_name="resume_template.html.jinja2",  context={"records": records})


@post("/new-resume")
async def add_resume(request: Request, data: dict[str, Any]) -> json:
    """This function will save the incoming data to the DB, to their
    corresponding tables. 'applicant_details' is an object of ApplicantDetails
    model which is used to save the data to ApplicantDetails model.
    """
    commit_flag = False
    applicant_data = data.get("applicant_details")

    applicant_details = ApplicantDetails(
        full_name=applicant_data.get("full_name"),
        email_id=applicant_data.get("email_id"),
        phone_number=applicant_data.get("phone_number"),
        image_url=applicant_data.get("image_url"),
        summary=applicant_data.get("summary"),
    )
    if applicant_details:
        session.add(applicant_details)
        session.commit()
        commit_flag = True

    if commit_flag:
        records = session.query(ApplicantDetails).all()
        record_lis = [rec.__dict__ for rec in records]
        *_, applicant_record = record_lis

    #  address_details object which saves data to AddressDetails model
    address_data = data.get("address_details")

    address_details = AddressDetails(
        applicant_details_id=applicant_record["id"],
        house_name=address_data.get("house_name"),
        district=address_data.get("district"),
        city=address_data.get("city"),
        state=address_data.get("state"),
        country=address_data.get("country"),
        zip_code=address_data.get("zip_code"),
    )
    if address_details:
        session.add(address_details)

    # Here the values are retrieved from a nested dictionary
    # The input data resides in a list belonging to the parent dictionary.
    try:
        if data["education"]:
            levels_of_education = len(data["education"])
            for entry in range(levels_of_education):
                education_data = data.get("education")[entry]

                education = Education(
                    applicant_details_id=applicant_record["id"],
                    degree=education_data.get("degree"),
                    stream=education_data.get("stream"),
                    institute_name=education_data.get("institute_name"),
                    institute_location=education_data.get("institute_location"),
                    academic_year_start_date=education_data.get(
                        "academic_year_start_date"
                    ),
                    academic_year_end_date=education_data.get("academic_year_end_date"),
                )
                if education:
                    session.add(education)
    except InvalidDatetimeFormat as error:
        session.rollback()

    try:
        if data["work_experience"]:
            places_worked = len(data["work_experience"])
            for entry in range(places_worked):
                work_exp_data = data.get("work_experience")[entry]

                work_experience = WorkExperience(
                    applicant_details_id=applicant_record["id"],
                    organization=work_exp_data.get("organization"),
                    job_role=work_exp_data.get("job_role"),
                    job_location=work_exp_data.get("job_location"),
                    key_roles=work_exp_data.get("key_roles"),
                    job_start_date=work_exp_data.get("job_start_date"),
                    job_end_date=work_exp_data.get("job_end_date"),
                )
                if work_experience:
                    session.add(work_experience)
    except InvalidDatetimeFormat as error:
        session.rollback()

    if data["social_media"]:
        existing_accounts = len(data["social_media"])
        for entry in range(existing_accounts):
            social_media_data = data.get("social_media")[entry]

            social_media = SocialMedia(
                applicant_details_id=applicant_record["id"],
                media_name=social_media_data.get("media_name"),
                user_name=social_media_data.get("user_name"),
                url=social_media_data.get("url"),
            )
            if social_media:
                session.add(social_media)

    if data["skills"]:
        number_of_skills = len(data["skills"])
        for entry in range(number_of_skills):
            skills_data = data.get("skills")[entry]

            skills = Skills(
                applicant_details_id=applicant_record["id"],
                skill_name=skills_data.get("skill_name"),
                skill_level=skills_data.get("skill_level"),
            )
            if skills:
                session.add(skills)

    if data["projects"]:
        number_of_projects = len(data["projects"])
        for entry in range(number_of_projects):
            skills_data = data.get("projects")[entry]
            projects = Projects(
                applicant_details_id=applicant_record["id"],
                project_title=skills_data.get("project_title"),
                tools_used=skills_data.get("tools_used"),
                description=skills_data.get("description"),
            )
            if projects:
                session.add(projects)

    # The received data is commited to the database
    session.commit()
    session.close()
    return data


@put("/edit-resume/{applicant_id: int}")
async def edit_resume(applicant_id: int, data: dict[str, Any]) -> str:
    applicant_detail_record = (
        session.query(ApplicantDetails).filter_by(id=applicant_id).first()
    )
    if applicant_detail_record:
        record = applicant_detail_record

        # Fetching the dict applicant_details
        applicant_data = data.get("applicant_details")

        # Updating each field in the dict
        record.full_name = applicant_data.get("full_name")
        record.email_id = applicant_data.get("email_id")
        record.phone_number = applicant_data.get("phone_number")
        record.image_url = applicant_data.get("image_url")
        record.summary = applicant_data.get("summary")
        session.add(record)

    address_detail_record = (
        session.query(AddressDetails)
        .filter_by(applicant_details_id=applicant_id)
        .first()
    )
    if address_detail_record:
        record = address_detail_record
        address_data = data.get("address_details")

        record.house_name = address_data.get("house_name")
        record.city = address_data.get("city")
        record.district = address_data.get("district")
        record.state = address_data.get("state")
        record.country = address_data.get("country")
        record.zip_code = address_data.get("zip_code")
        session.add(address_detail_record)

    education_detail_record = (
        session.query(Education).filter_by(applicant_details_id=applicant_id).all()
    )
    if education_detail_record:
        item = 0
        for entry in education_detail_record:
            education_data = data.get("education")[item]

            entry.degree = education_data.get("degree")
            entry.stream = education_data.get("stream")
            entry.institute_name = education_data.get("institute_name")
            entry.institute_location = education_data.get("institute_location")
            entry.academic_year_start_date = education_data.get(
                "academic_year_start_date"
            )
            entry.academic_year_end_date = education_data.get("academic_year_end_date")
            session.add(entry)
            item += 1

    work_experience_record = (
        session.query(WorkExperience).filter_by(applicant_details_id=applicant_id).all()
    )
    if work_experience_record:
        item = 0
        for entry in work_experience_record:
            work_data = data.get("work_experience")[item]

            entry.organization = work_data.get("organization")
            entry.job_role = work_data.get("job_role")
            entry.job_location = work_data.get("job_location")
            entry.key_roles = work_data.get("key_roles")
            entry.job_start_date = work_data.get("job_start_date")
            entry.job_end_date = work_data.get("job_end_date")
            session.add(entry)
            item += 1

    social_media_record = (
        session.query(SocialMedia).filter_by(applicant_details_id=applicant_id).all()
    )
    if social_media_record:
        item = 0
        for entry in social_media_record:
            media_data = data.get("social_media")[item]

            entry.media_name = media_data.get("media_name")
            entry.user_name = media_data.get("user_name")
            entry.url = media_data.get("url")
            session.add(entry)
            item += 1

    skills_record = (
        session.query(Skills).filter_by(applicant_details_id=applicant_id).all()
    )
    if skills_record:
        item = 0
        for entry in skills_record:
            skills_data = data.get("skills")[item]

            entry.skill_name = skills_data.get("skill_name")
            entry.skill_level = skills_data.get("skill_level")
            session.add(entry)
            item += 1

    projects_record = (
        session.query(Projects).filter_by(applicant_details_id=applicant_id).all()
    )
    if projects_record:
        item = 0
        for entry in projects_record:
            projects_data = data.get("projects")[item]

            entry.project_title = projects_data.get("project_title")
            entry.tools_used = projects_data.get("tools_used")
            entry.description = projects_data.get("description")
            session.add(entry)
            item += 1

    session.commit()
    session.close()
    return "Record updated."


@delete("/delete-resume/{applicant_id: int}")
async def delete_resume(applicant_id: int) -> None:
    query = session.query(ApplicantDetails).filter_by(id=applicant_id).first()
    if query:
        session.delete(query)
        session.commit()
        session.close()
        return None


cors_config = CORSConfig(allow_origins=["*"])

template_config = TemplateConfig(
    directory=Path(__file__).parent / "templates",
    engine=JinjaTemplateEngine,
)

app = Litestar(
    route_handlers=[
        show_all_resumes,
        show_resume_by_id,
        show_resume_by_field,
        add_resume,
        edit_resume,
        delete_resume,
        download_resume,
    ],
    cors_config=cors_config,
    debug=True,
    template_config=template_config,
)
