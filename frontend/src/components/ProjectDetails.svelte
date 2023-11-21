<script>
    import TextField from '../input/TextField.svelte';
    
    import { slide } from 'svelte/transition';
	const handleClick = () => open = !open;
    export let open = false;
    export let projects = [{ project_title:'', tools_used:'', description:''}]
    // export let project_title = '';
    // export let skills_earned = '';
    // export let description = '';

    function addProject() {
      projects = [...projects, { project_title:'', tools_used:'', description:''}];
    }
    function removeProject(index) {
      if (projects.length > 1) {
        projects = projects.filter((_, i) => i !== index);
      }
    }

</script>
<div class="content-box">
    <h3 class="sub-title" on:click={handleClick}>Project Details</h3>
    {#if open}
    {#each projects as projectData, i}
    <div class="Active" transition:slide>
        <TextField placeholder = "Enter your project title" id = "project-title" label = "Project Title" bind:value={projectData.project_title} />
        <TextField placeholder = "Enter the skills/tools you learned/used for this project" id = "skills" label = "Skills" bind:value={projectData.tools_used}/>
        <TextField placeholder = "Enter a brief description of the project" id = "description" label = "Description" bind:value={projectData.description}/>
    </div>
    <div class="extra-field">
        <button on:click|preventDefault={addProject}>
            <span class="add">+ Add Another</span></button>
        {#if i !== 0}
            <button on:click|preventDefault={() => removeProject(i)}>
                <span class="remove">- Remove</span></button>
        {/if}
    </div>
    {/each}
    {/if}	
</div>
<style>
    h3{
       width: 100%;
   }
   h3:hover{
    cursor: pointer;
   }
  
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
   .sub-title::before{
       content: '+';
       position: absolute;
       right: 25px;
       
   }
   .extra-field{
        margin-top: 10px;
   }
   .extra-field button{
        width: 137px;
        background-color: white;
        color: black;
        border: none;
        border-radius: 5px;
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