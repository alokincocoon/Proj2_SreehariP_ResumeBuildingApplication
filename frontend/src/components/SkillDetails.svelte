<script>
  import TextField from "../input/TextField.svelte";
  import SelectField from "../input/SelectField.svelte";
  import { slide } from "svelte/transition";

  export let skill_options = ["Beginner", "Intermediate", "Expert"];
  export let open = false;
  const handleClick = () => (open = !open);

  export let skills = [{ skill_name: "", skill_level: "" }];
  // export let skill_name = '';
  // export let level = '';
  function addSkill() {
    skills = [...skills, { skill_name: "", skill_level: "" }];
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
        <TextField
          placeholder="eg: Coding/Self learner/Time management etc."
          id="skill-name"
          label="Skill Name"
          bind:value={skill.skill_name}
        />
        <SelectField
          label="Skill Level"
          options={skill_options}
          bind:value={skill.skill_level}
          default_value="Select Skill Level"
        />
      </div>
      <div class="extra-fields">
        <button on:click|preventDefault={addSkill}>
          <span class="add">+ Add Another</span></button
        >
        {#if i !== 0}
          <button on:click|preventDefault={() => removeSkill(i)}>
            <span class="remove">- Remove</span></button
          >
        {/if}
      </div>
    {/each}
  {/if}
</div>

<style>
  h3 {
    width: 100%;
  }
  h3:hover {
    cursor: pointer;
  }

  .add {
    font-size: 15px;
    color: teal;
    font-weight: bold;
  }
  .remove {
    color: red;
    font-size: 15px;
    font-weight: bold;
  }
  .sub-title::before {
    content: "+";
    position: absolute;
    right: 25px;
  }
  .extra-fields {
    margin-top: 10px;
  }
  .extra-fields button {
    width: 123px;
    background-color: white;
    color: black;
    border: none;
    border-radius: 5px;
  }
  .extra-fields button:hover {
    cursor: pointer;
  }
  .content-box {
    border: 1px solid white;
    margin-top: 10px;
    margin-bottom: 10px;
    box-shadow: rgba(9, 30, 66, 0.25) 0px 4px 8px -2px,
      rgba(9, 30, 66, 0.08) 0px 0px 0px 1px;
    /* box-shadow: 0 20px 10px -20px rgba(0,0,0,0.45) inset, 0 -20px 10px -20px rgba(0,0,0,0.45) inset; */
  }
</style>
