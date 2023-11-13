<script>
    import TextField from '../input/TextField.svelte';
    
    import { slide } from 'svelte/transition';
	const handleClick = () => open = !open;
    export let open = false;
    export let project = [{ project_title:'', skills_earned:'', description:''}]
    // export let project_title = '';
    // export let skills_earned = '';
    // export let description = '';

    function addProject() {
      project = [...project, { project_title:'', skills_earned:'', description:''}];
    }
    function removeProject(index) {
      if (project.length > 1) {
        project = project.filter((_, i) => i !== index);
      }
    }

</script>
<div class="content-box">
    <h3 class="sub-title" on:click={handleClick}>Project Details</h3>
    {#if open}
    {#each project as projectData, i}
    <div class="Active" transition:slide>
        <TextField placeholder = "Add Project Title" id = "project-title" label = "Project Title" bind:value={projectData.project_title} />
        <TextField placeholder = "Add Skills" id = "skills" label = "Skills" bind:value={projectData.skills_earned}/>
        <TextField placeholder = "Add Description" id = "description" label = "Description" bind:value={projectData.description}/>
    </div>
    <div class="extra-field">
        <button on:click|preventDefault={addProject}>+ Project</button>
        {#if i !== 0}
            <button on:click|preventDefault={() => removeProject(i)}>- Project</button>
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
        border-radius: 5px;
   }
   .content-box{
        border: 1px solid white;
        margin-top: 10px;
        margin-bottom: 10px;
        box-shadow: 0 20px 10px -20px rgba(0,0,0,0.45) inset, 0 -20px 10px -20px rgba(0,0,0,0.45) inset;
    }
</style>