<script>
    import TextField from "../input/TextField.svelte";
    import UrlField from "../input/UrlField.svelte";
    import EmailField from "../input/EmailField.svelte";
    import { slide } from "svelte/transition";
    export let open = false;
    const handleClick = () => (open = !open);
    
    export let full_name = "";
    export let email_id="";
    export let phone_number="";
    
    export let image_url="";
    export let summary="";
    // export {full_name,email_id,phone_number,image_url,summary};
    
</script>

<main>
    <div class="container">
        <h3 class="accordion-title" on:click={handleClick}>Applicant Details<span class="mandatory">*</span></h3>
        {#if open}
            <div class="active" transition:slide>
                <TextField
                    placeholder="Add Name"
                    id="name"
                    label="Name"
                   
                    bind:value = "{full_name}"
                />
                <EmailField 
                    placeholder="Add Email" 
                    id="email" 
                    label="Email"  
                    bind:value = "{email_id}"
                />

                <TextField
                    placeholder="Add Phone Number"
                    id="phone"
                    label="Phone"
                    
                    bind:value = "{phone_number}"
                />
                <UrlField
                    placeholder="Add Image URL"
                    id="image-url"
                    label="Image URL"
                    
                    bind:value = "{image_url}"
                />
                <TextField
                    placeholder="Add Summary"
                    id="summary"
                    label="Summary"
                    
                    bind:value = "{summary}"
                />
            </div>
        {/if}
    </div>
</main>

<style>
    h3 {
        width: 100%;
    }
    h3:hover {
        cursor: pointer;
    }

    .accordion-title::before {
        content: "\002B";
        position: absolute;
        right: 25px;
    }
    /* .active::after{
        content: "\2212";
        position: absolute;
        right: 25px;
    } */
    .container{
        border: 1px solid white;
        margin-top: 10px;
        margin-bottom: 10px;
        box-shadow: rgba(9, 30, 66, 0.25) 0px 4px 8px -2px, rgba(9, 30, 66, 0.08) 0px 0px 0px 1px;
        /* box-shadow: 0 20px 10px -20px rgba(0,0,0,0.45) inset, 0 -20px 10px -20px rgba(0,0,0,0.45) inset; */
    }
     
    .mandatory{
        color: red;
        size: 12px;
        font-weight: lighter;
        margin-left: 2px;
    }

</style>