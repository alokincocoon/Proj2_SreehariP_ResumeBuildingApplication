<script>
    import ApplicantDetails from "./ApplicantDetails.svelte";
    import AddressDetails from "./AddressDetails.svelte";
    import EducationDetails from "./EducationDetails.svelte";
    import ProjectDetails from "./ProjectDetails.svelte";
    import SkillDetails from "./SkillDetails.svelte";
    import SocialMediaDetails from "./SocialMediaDetails.svelte";
    import Button from "../input/Button.svelte";
    import WorkDetails from "./WorkDetails.svelte";
    // import axios from 'axios';
    // import { onMount } from "svelte";

    export let backward_link = "< Back to all Resume List";

    export let form_data = {};

    // export let [name,email,phone,image_url,summary] = ["","","","",""];
    export let full_name="";
    export let email_id="";
    export let phone_number="";
    export let image_url="";
    export let summary="";

    export let address_line="";
    export let street_name="";
    export let city="";
    export let zip_code="";
    export let country="";

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
        form_data = 
        {
        "applicant_details":{full_name, email_id, phone_number, image_url, summary},
        "address_details":{address_line,street_name, city,country, zip_code},
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
        } 
        catch (error) {
            console.error("Error:", error);
        }
        console.log(form_data);

    };
    
</script>

<main><div class="form-heading">
    <!-- <a href="">{backward_link}</a> -->
    <h2>Create Your Resume</h2>
</div>
<form on:submit|preventDefault={handleSubmit}>
    <ApplicantDetails
        bind:full_name
        bind:email_id
        bind:phone_number
        bind:image_url
        bind:summary
    />

    <AddressDetails
        bind:address_line
        bind:street_name
        bind:city
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
        <Button typeOfButton="cancel" buttonLabel="Cancel" />
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
        justify-content: end;
    }
    
</style>