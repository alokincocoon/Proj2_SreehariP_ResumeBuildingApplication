<script>
    import ApplicantDetails from "../components/ApplicantDetails.svelte";
    import AddressDetails from "../components/AddressDetails.svelte";
    import EducationDetails from "../components/EducationDetails.svelte";
    import ProjectDetails from "../components/ProjectDetails.svelte";
    import SkillDetails from "../components/SkillDetails.svelte";
    import SocialMediaDetails from "../components/SocialMediaDetails.svelte";
    import Button from "../input/Button.svelte";
    import WorkDetails from "../components/WorkDetails.svelte";
    import {
        validateEmail,
        validateFullName,
        validatePhoneNumber,
        validateSummary,
        validateInput
    } from "../validation/Validation";
    import { onMount } from "svelte";
    

    let recordId;
    let UrlHome = "< Back To Home Page";
    let [singleEntry, multipleEntry] = [true, true];
    const formReset = document.getElementById("form");

    export let succesMessage = "";
    export let errorMessage = "";

    export let full_name = "";
    export let email_id = "";
    export let phone_number = "";
    export let image_url = "";
    export let summary = "";

    export let house_name = "";
    export let city = "";
    export let district = "";
    export let state = "";
    export let zip_code = "";
    export let country = "";
    
  
    export let education = [];
    export let social_media = [];
    export let work_experience = [];
    export let skills = [];
    export let projects = [];
    
        onMount (async () => {
        recordId = window.history.state.recordId;

        try{
        const response = await fetch(`http://127.0.0.1:8000/resume/${recordId}`,{
            method: "GET",
            // body: JSON.stringify(form_data)
        });
        const result = await response.json();
        console.log("Success:", result);

        full_name = result.applicant_details.full_name;
        email_id = result.applicant_details.email_id;
        phone_number = result.applicant_details.phone_number;
        image_url = result.applicant_details.image_url;
        summary = result.applicant_details.summary;

        house_name = result.address_details.house_name;
        city = result.address_details.city;
        district = result.address_details.district;
        state = result.address_details.state;
        country = result.address_details.country;
        zip_code = result.address_details.zip_code;

        // console.log(result.education.length);
        for (let item = 0; item < result.education.length; item ++)
        {   
            let resultObj = result.education[item];

            let dict = { 
            institute_name : resultObj["institute_name"],
            institute_location : resultObj["institute_location"],
            stream : resultObj["stream"],
            degree : resultObj["degree"],
            academic_year_start_date : resultObj["academic_year_start_date"],
            academic_year_end_date : resultObj["academic_year_end_date"]
            }
            education.push(dict)
        }
        
        for (let item = 0; item < result.social_media.length; item ++)
        {   
            let resultObj = result.social_media[item];

            let dict = { 
            media_name : resultObj["media_name"],
            url : resultObj["url"],
            user_name : resultObj["user_name"],
            }
            social_media.push(dict)
        }

        for (let item = 0; item < result.work_experience.length; item ++)
        {   
            let resultObj = result.work_experience[item];

            let dict = { 
            organization : resultObj["organization"],
            job_location : resultObj["job_location"],
            job_start_date : resultObj["job_start_date"],
            job_role : resultObj["job_role"],
            job_end_date : resultObj["job_end_date"],
            key_roles : resultObj["key_roles"],
            }
            work_experience.push(dict)
        }
  

        for (let item = 0; item < result.skills.length; item ++)
        {   
            let resultObj = result.skills[item];

            let dict = { 
            skill_level : resultObj["skill_level"],
            skill_name : resultObj["skill_name"],
            }
            skills.push(dict)
        }

        for (let item = 0; item < result.projects.length; item ++)
        {   
            let resultObj = result.projects[item];

            let dict = { 
            description : resultObj["description"],
            project_title : resultObj["project_title"],
            tools_used : resultObj["tools_used"],
            }
            projects.push(dict)
        }


        } 
        catch (error) {
            console.error("Error:", error);
            errorMessage = "Error! Could not fetch resume";
        }
        // console.log(form_data);
        window.scrollTo(0,0);

    });

    async function handleSubmit() {

        let form_data = {
        "applicant_details":{full_name, email_id, phone_number, image_url, summary},
        "address_details":{house_name, city, district, state, country, zip_code},
        education,
        social_media,
        work_experience,
        skills,
        projects
        };

        try{
        const response = await fetch(`http://127.0.0.1:8000/edit-resume/${recordId}`,{
            method: "PUT",
            mode: "cors",
            cache: "no-cache",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(form_data)
        });

        const result = await response.json();
        console.log("Success:", result);
        succesMessage = "Resume successfully updated.";
        document.getElementById('form-data').reset();
        } 
        catch (error) {
            console.error("Error:", error);
            errorMessage = "Error! Could not update resume";
        }
        console.log(form_data);
        window.scrollTo(0,0);
        // if (
        //     validateFullName(full_name) &&
        //     validateEmail(email_id) &&
        //     validatePhoneNumber(phone_number) &&
        //     validateSummary(summary) &&
        //     validateInput(house_name) &&
        //     validateInput(district) &&
        //     validateInput(city) &&
        //     validateInput(state) &&
        //     validateInput(country) &&
        //     validateInput(zip_code)
        // ){
        //     singleEntry = true;
        // }
        // else{
        //     singleEntry = false;
        // }

        // for(let item = 0;item < education.length ; item++){
        //     if (
        //         education[item].degree == null ||
        //         education[item].stream == null ||
        //         education[item].institute_name == null ||
        //         education[item].institute_location == null ||
        //         education[item].academic_year_start_date == null ||
        //         education[item].academic_year_end_date == null
        //     ) {
        //         multipleEntry = false;
        //     }
        // }

        // if (singleEntry && multipleEntry)
        // {
        // form_data = 
        // {
        // "applicant_details":{full_name, email_id, phone_number, image_url, summary},
        // "address_details":{house_name, city, district, state, country, zip_code},
        // education,
        // social_media,
        // work_experience,
        // skills,
        // projects
        // }; 
    }  
    
</script>

<main>
    <div class="form-heading">
    {#if errorMessage}
    <div class="alert">
      <span class="closebtn" on:click={() => (errorMessage = "")}>&times;</span>
      <p>{errorMessage}</p>
    </div>
    {:else if succesMessage}
    <div class="success">
        <span class="closebtn" on:click={() => (succesMessage = "")}>&times;</span>
        <p>{succesMessage}</p>
      </div>
    {:else}
    <p></p>
  {/if}

    <a href="#/">{UrlHome}</a>
    <h2>Create Your Resume</h2>
</div>
<form on:submit|preventDefault={handleSubmit} id="form-data">
    <ApplicantDetails
        bind:full_name
        bind:email_id
        bind:phone_number
        bind:image_url
        bind:summary
    />

    <AddressDetails
        bind:house_name
        bind:city
        bind:district
        bind:state
        bind:country
        bind:zip_code
    />

    <EducationDetails
        bind:education
    />

    <SocialMediaDetails 
        bind:social_media 
    />

    <WorkDetails 
        bind:work_experience 
    />

    <SkillDetails 
        bind:skills 
    />

    <ProjectDetails
        bind:projects
    />

    <div class="button-group">
        <a href="#/">
        <Button typeOfButton="cancel" buttonLabel="Cancel" type="button"/></a>
        <Button typeOfButton="save" buttonLabel="Save" type="submit" />
    </div>
</form>

</main>

<style>
    /* @import url('https://fonts.googleapis.com/css?family=Muli&display=swap'); */
    h2{ 
        text-align: center;
        font-family: 'Muli', sans-serif;
    }
   .form-heading {
        width: 100%;
        height: auto;
        /* background-color: #f9fafb; */
    }
    .button-group {
        display: flex;
        justify-content: center;
    }
    .alert p, .success p {
    color: #252525;
    font-size: 20px;
    height: 13px;
    margin-left: 6px;
  }
  .alert {
    padding: 8px;
    background-color: rgb(235, 121, 109);
    color: rgb(0, 0, 0);
    margin-bottom: 15px;
    text-align: center;
    width: 98%;
    margin-top: 9px;
  }
  .success{
    padding: 8px;
    background-color: rgb(150, 247, 156);
    color: rgb(0, 0, 0);
    margin-bottom: 15px;
    text-align: center;
    width: 98%;
    margin-top: 9px;
  }
  /* The close button */
  .closebtn {
    margin-left: 15px;
    color: rgb(0, 0, 0);
    font-weight: bold;
    float: right;
    font-size: 22px;
    line-height: 20px;
    cursor: pointer;
    transition: 0.3s;
  }
</style>