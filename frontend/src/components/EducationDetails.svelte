<script>
    import TextField from '../input/TextField.svelte';
    import DateField from '../input/DateField.svelte';    
    
    import { slide } from 'svelte/transition';
	const handleClick = () => open = !open;
    export let open = false;
    export let education = [{ degree:'', stream:'', institute_name:'', institute_location:'', academic_year_start_date:'', academic_year_end_date:''}]
    // export let qualification='';
    // export let course_name = '';
    // export let institute_name = '';
    // export let location ='';
    // export let academic_year_start='';
    // export let accademic_year_end='';

    function addEducation() {
      education = [...education, { degree:'', stream:'', institute_name:'', institute_location:'', academic_year_start_date:'', academic_year_end_date:''}];
    }
    function removeEducation(index) {
      if (education.length > 1) {
        education = education.filter((_, i) => i !== index);
      }
    }
</script>
<div class="content-box">
    <h3 class="sub-title" on:click={handleClick}>Education</h3>
    {#if open}
    {#each education as educationData, i}
    <div class="Active" transition:slide>
        <TextField placeholder = "Add Qualification" id = "qualification" label = "Qualification" bind:value={educationData.degree}/>
        <TextField placeholder = "Add Course Name" id = "course-name" label = "Course Name" bind:value={educationData.stream} />
        <TextField placeholder = "Add Institute" id = "institute" label = "Institute" bind:value={educationData.institute_name} />
        <TextField placeholder = "Add Location" id = "location" label = "Location" bind:value={educationData.institute_location} />
        <DateField placeholder = "Starting Year" id = "accademic_year_start" label = "Starting Year" bind:value={educationData.academic_year_start_date} />
        <DateField placeholder = "Ending Year" id = "accademic_year_end" label = "Ending Year" bind:value={educationData.academic_year_end_date} />	
    </div>
    <div class="extra-field">
        <button on:click|preventDefault={addEducation}><span class="add">+ Add Another</span></button>
        {#if i !== 0}
            <button on:click|preventDefault={() => removeEducation(i)}><span class="remove">- Remove</span></button>
        {/if}
    </div>
    {/each}
    {/if}
</div>
<style>
    .add{
        font-size: 15px;
        color: teal;
        font-weight: bold;
    }
    .remove{
        color: red;
        font-size: 15px;
        font-weight: bold;
    }
    h3{
       width: 100%;
   }
   h3:hover{
    cursor: pointer;
   }
  
   .sub-title::before{
       content: '+';
       position: absolute;
       right: 25px;
       
   }
   .extra-field{
        margin-top: 10px;
   }
   .extra-field button{
        width: 178px;
        background-color: white;
        color: black;
        border-radius: 5px;
        border: none;
   }
   .extra-field button:hover{
    cursor: pointer;
   }
   .content-box{
        border: 1px solid white;
        margin-top: 10px;
        margin-bottom: 10px;
        box-shadow: rgba(9, 30, 66, 0.25) 0px 4px 8px -2px, rgba(9, 30, 66, 0.08) 0px 0px 0px 1px;
        /* box-shadow: 0 20px 10px -20px rgba(0,0,0,0.45) inset, 0 -20px 10px -20px rgba(0,0,0,0.45) inset; */
    }
</style>