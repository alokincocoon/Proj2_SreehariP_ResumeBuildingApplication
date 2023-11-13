<script>
    import TextField from "../input/TextField.svelte";
    import UrlField from "../input/UrlField.svelte";
    import EmailField from "../input/EmailField.svelte";
    import { slide } from "svelte/transition";
    export let open = false;
    const handleClick = () => (open = !open);
    
    export let [name,email,phone,image_url,summary] = ["","","","",""];
    
</script>

<main>
    <div class="container">
        <h3 class="accordion-title" on:click={handleClick}>Applicant Details</h3>
        {#if open}
            <div class="active" transition:slide>
                <TextField
                    placeholder="Add Name"
                    id="name"
                    label="Name"
                   
                    bind:value = "{name}"
                />
                <EmailField 
                    placeholder="Add Email" 
                    id="email" 
                    label="Email"  
                    bind:value = "{email}"
                />

                <TextField
                    placeholder="Add Phone Number"
                    id="phone"
                    label="Phone"
                    
                    bind:value = "{phone}"
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
        box-shadow: 0 20px 10px -20px rgba(0,0,0,0.45) inset, 0 -20px 10px -20px rgba(0,0,0,0.45) inset;
    }

</style>