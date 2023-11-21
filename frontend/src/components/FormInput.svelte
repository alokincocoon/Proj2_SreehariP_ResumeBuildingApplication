<script>
    import ApplicantDetails from "./ApplicantDetails.svelte";
    import AddressDetails from "./AddressDetails.svelte";
    import EducationDetails from "./EducationDetails.svelte";
    import ProjectDetails from "./ProjectDetails.svelte";
    import SkillDetails from "./SkillDetails.svelte";
    import SocialMediaDetails from "./SocialMediaDetails.svelte";
    import Button from "../input/Button.svelte";
    import WorkDetails from "./WorkDetails.svelte";
    import {
        validateEmail,
        validateFullName,
        validatePhoneNumber,
        validateSummary,
        validateInput
    } from "../validation/Validation"
    // import axios from 'axios';
    // import { onMount } from "svelte";

    let UrlHome = "< Back To Home Page";
    let [singleEntry, multipleEntry] = [true, true];
    const formReset = document.getElementById("form");
    export let form_data = {};

    export let succesMessage="";
    export let errorMessage="";

    // export let [name,email,phone,image_url,summary] = ["","","","",""];
    export let full_name="";
    export let email_id="";
    export let phone_number="";
    export let image_url="";
    export let summary="";

    export let house_name="";
    export let city="";
    export let district="";
    export let state="";
    export let zip_code="";
    export let country= "";

    
    export let education = [{ degree:'', stream:'', institute_name:'', institute_location:'', academic_year_start_date:'', academic_year_end_date:''}];
    export let social_media = [{ media_name: "", url: "", user_name: "" }];
    export let work_experience = [
        {
            organization: "",
            job_role: "",
            job_location: "",
            key_roles: "",
            job_start_date: "",
            job_end_date: "",
        },
    ];
    export let skills = [{ skill_name: "", skill_level: "" }];
    export let projects = [{ project_title:'', tools_used:'', description:''}];
    

    async function handleSubmit() {
        if (
            validateFullName(full_name) &&
            validateEmail(email_id) &&
            validatePhoneNumber(phone_number) &&
            validateSummary(summary) &&
            validateInput(house_name) &&
            validateInput(district) &&
            validateInput(city) &&
            validateInput(state) &&
            validateInput(country) &&
            validateInput(zip_code)
        ){
            singleEntry = true;
        }
        else{
            singleEntry = false;
        }

        for(let item = 0;item < education.length ; item++){
            if (
                education[item].degree == null ||
                education[item].stream == null ||
                education[item].institute_name == null ||
                education[item].institute_location == null ||
                education[item].academic_year_start_date == null ||
                education[item].academic_year_end_date == null
            ) {
                multipleEntry = false;
            }
        }

        if (singleEntry && multipleEntry)
        {
        form_data = 
        {
        "applicant_details":{full_name, email_id, phone_number, image_url, summary},
        "address_details":{house_name, city, district, state, country, zip_code},
        education,
        social_media,
        work_experience,
        skills,
        projects
        };
        try{
        const response = await fetch("http://127.0.0.1:8000/new-resume",{
            method: "POST",
            mode: "cors",
            cache: "no-cache",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(form_data)
        });

        const result = await response.json();
        console.log("Success:", result);
        succesMessage = "Resume created successfully.";
        document.getElementById('form-data').reset();
        } 
        catch (error) {
            console.error("Error:", error);
            errorMessage = "Error! Could not create resume";
        }
        console.log(form_data);
        window.scrollTo(0,0);
    }
    else {
        errorMessage = "Please fill in the required fields";
        window.scrollTo(0,0);
    }
    };
    
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