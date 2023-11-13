<script>
    import TextField from '../input/TextField.svelte';
    import SelectField from '../input/SelectField.svelte';
    import { slide } from 'svelte/transition';

    export let skill_options = ['Beginner', 'Intermediate', 'Expert']
    export let open = false;
	const handleClick = () => open = !open;

    export let skills = [{ skill_name: '', level: ''}]
    // export let skill_name = '';
    // export let level = '';
    function addSkill() {
      skills = [...skills, {skill_name: '', level: ''}];
    }
    function removeSkill(index) {
      if (skills.length > 1) {
        skills = skills.filter((_, i) => i !== index);
      }
    }
</script>
<div class="content-box">
    <h3 class="sub-title" on:click={handleClick}>Skills</h3>
    {#if open}
    {#each skills as skill, i}
    <div class="Active" transition:slide>
        <TextField placeholder = "Add Skill Name" id = "skill-name" label = "Skill Name" bind:value={skill.skill_name} />
        <SelectField label="Level" options={skill_options} bind:value={skill.level} default_value="Select Skill Level" />
    </div>
    <div class="extra-fields">
    <button on:click|preventDefault={addSkill}>Add New Skill</button>
    {#if i !== 0}
        <button on:click|preventDefault={() => removeSkill(i)}>Remove Skill</button>
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
   .extra-fields{
        margin-top: 10px;
   }
   .extra-fields button{
        width: 123px;
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