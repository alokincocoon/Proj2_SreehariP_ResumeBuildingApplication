<script>
    import ApplicantDetails from "./ApplicantDetails.svelte";
    import AddressDetails from "./AddressDetails.svelte";
    import EducationDetails from "./EducationDetails.svelte";
    import ProjectDetails from "./ProjectDetails.svelte";
    import SkillDetails from "./SkillDetails.svelte";
    import SocialMediaDetails from "./SocialMediaDetails.svelte";
    import Button from "../input/Button.svelte";
    import WorkDetails from "./WorkDetails.svelte";

    export let backward_link = "< Back to all Resume List";

    export let form_data = {};

    export let [name,email,phone,image_url,summary] = ["","","","",""];
    export let [address,street,city,pincode,country] = ["","","","",""];
    export let education = [{ qualification:'', course_name:'', institute_name:'', location:'', academic_year_start:'', accademic_year_end:''}] ;
    export let social_media = [{ network: "", url: "", user_name: "" }];
    export let work = [
        {
            organisation: "",
            job_role: "",
            job_location: "",
            key_roles: "",
            start_date: "",
            end_date: "",
        },
    ];
    export let skills = [{ skill_name: "", level: "" }];
    export let project = [{ project_title:'', skills_earned:'', description:''}];
    function handleSubmit() {
        form_data = {
                name,
                email,
                phone,
                image_url,
                summary,           
                address,
                street,
                city,
                pincode,
                country,
                education,
                social_media,
                work,
                skills,
                project
        };
        console.log(JSON.stringify(form_data, null, 2));
    }
</script>

<main><div class="formHeading">
    <a href="">{backward_link}</a>
    <h2>Add Resume Content</h2>
</div>
<form on:submit|preventDefault={handleSubmit}>
    <ApplicantDetails
        bind:name
        bind:email
        bind:phone
        bind:image_url
        bind:summary
    />

    <AddressDetails
        bind:address
        bind:street
        bind:city
        bind:pincode
        bind:country
    />

    <EducationDetails
        bind:education
    />

    <SocialMediaDetails 
        bind:social_media 
    />

    <WorkDetails 
        bind:work 
    />

    <SkillDetails 
        bind:skills 
    />

    <ProjectDetails
        bind:project
    />

    <div class="button-group">
        <Button typeOfButton="cancel" buttonLabel="Cancel" />
        <Button typeOfButton="save" buttonLabel="Save" type="submit" />
    </div>
</form>

</main>

<style>
   .formHeading {
        width: 100%;
        height: auto;
        background-color: #f9fafb;
    }
    .button-group {
        display: flex;
        justify-content: end;
    }
</style>