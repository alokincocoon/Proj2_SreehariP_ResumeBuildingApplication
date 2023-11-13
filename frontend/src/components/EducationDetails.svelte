<script>
    import TextField from '../input/TextField.svelte';
    import DateField from '../input/DateField.svelte';    
    
    import { slide } from 'svelte/transition';
	const handleClick = () => open = !open;
    export let open = false;
    export let education = [{ qualification:'', course_name:'', institute_name:'', location:'', academic_year_start:'', accademic_year_end:''}]
    // export let qualification='';
    // export let course_name = '';
    // export let institute_name = '';
    // export let location ='';
    // export let academic_year_start='';
    // export let accademic_year_end='';

    function addEducation() {
      education = [...education, { qualification:'', course_name:'', institute_name:'', location:'', academic_year_start:'', accademic_year_end:''}];
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
        <TextField placeholder = "Add Qualification" id = "qualification" label = "Qualification" bind:value={educationData.qualification}/>
        <TextField placeholder = "Add Course Name" id = "course-name" label = "Course Name" bind:value={educationData.course_name} />
        <TextField placeholder = "Add Institute" id = "institute" label = "Institute" bind:value={educationData.institute_name} />
        <TextField placeholder = "Add Location" id = "location" label = "Location" bind:value={educationData.location} />
        <DateField placeholder = "Add Accademic Year Start" id = "accademic_year_start" label = "Accademic Year Start" bind:value={educationData.academic_year_start} />
        <DateField placeholder = "Add Accademic Year End" id = "accademic_year_end" label = "Accademic Year End" bind:value={educationData.accademic_year_end} />	
    </div>
    <div class="extra-field">
        <button on:click|preventDefault={addEducation}><span class="add">+</span> Add Another</button>
        {#if i !== 0}
            <button on:click|preventDefault={() => removeEducation(i)}><span class="remove">-</span> Remove</button>
        {/if}
    </div>
    {/each}
    {/if}
</div>
<style>
    .add{
        font-size: 20px;
        color: green;
        font-weight: bold;
    }
    .remove{
        color: red;
        font-size: 20px;
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
   }
   .content-box{
        border: 1px solid white;
        margin-top: 10px;
        margin-bottom: 10px;
        box-shadow: 0 20px 10px -20px rgba(0,0,0,0.45) inset, 0 -20px 10px -20px rgba(0,0,0,0.45) inset;
    }
</style>