<script>
    import TextField from "../input/TextField.svelte";
    import DateField from "../input/DateField.svelte";

    import { slide } from "svelte/transition";
    const handleClick = () => (open = !open);
    export let open = false;

    export let work = [{ organisation: '', job_role: '', job_location: '', key_roles: '', start_date:'', end_date:'' }]
    // export let organisation = '';
    // export let job_role = '';
    // export let job_location = '';
    // export let key_roles = '';
    // export let start_date = '';
    // export let end_date = '';
    function addWork(){
        work = [...work, { organisation: '', job_role: '', job_location: '', key_roles: '', start_date:'', end_date:'' }]
    }
    function removeWork(index) {
      if (work.length > 1) {
        work = work.filter((_, i) => i !== index);
      }
    }

</script>

<div class="content-box">
    <h3 class="sub-title" on:click={handleClick}>Work</h3>
    {#if open}
    {#each work as work_data, i}
        <div class="Active" transition:slide>
            <TextField
                placeholder="Add Organisation"
                id="organisation"
                label="Organisation"
                bind:value="{work_data.organisation}"
            />
            <TextField
                placeholder="Add Job Role"
                id="job-role"
                label="Job Role"
                bind:value="{work_data.job_role}"
            />
            <TextField
                placeholder="Add Job Location"
                id="job-location"
                label="Job Location"
                bind:value="{work_data.job_location}"
            />
            <TextField
                placeholder="Add Key Roles "
                id="key-roles"
                label="Key Roles"
                bind:value="{work_data.key_roles}"
            />
            <DateField
                placeholder="Add Start Date"
                id="start-date"
                label="Start Date"
                bind:value="{work_data.start_date}"
            />
            <DateField
                placeholder="Add End Date"
                id="end-date"
                label="End Date"
                bind:value="{work_data.end_date}"
            />
        </div>
        <div class="work-buttons">
            <button on:click|preventDefault={addWork}>Add New Work</button>
            {#if i !== 0}
                <button on:click|preventDefault={() => removeWork(i)}>Remove Work</button>
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

    .sub-title::before {
        content: "+";
        position: absolute;
        right: 25px;
    }
    .work-buttons{
        margin-top: 10px;
   }
   .work-buttons button{
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