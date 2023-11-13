<script>
    import TextField from "../input/TextField.svelte";  
    import SelectField from "../input/SelectField.svelte";  
    
    import { slide } from "svelte/transition";
    const handleClick = () => (open = !open);
    export let open = false;
    export let countryOptions = [
        "India",
        "Canada",
        "United Kingdom",
        "United States",
        "Australia",
        "China",
        "Qatar",
    ];
    export let address = "";
    export let street = "";
    export let city = "";
    export let pincode = "";
    export let country = "";
</script>

<main>
    <div class="content-box">
        <h3 class="sub-title" on:click={handleClick}>Address Details</h3>
        {#if open}
            <div class="Active" transition:slide>
                <TextField
                    placeholder="Add Address Line"
                    id="address"
                    label="Address"
                    bind:value={address}
                />
                <TextField
                    placeholder="Add Street Name"
                    id="street"
                    label="Street"
                    bind:value={street}
                />
                <TextField
                    placeholder="Add City Name"
                    id="city"
                    label="City"
                    bind:value={city}
                />
                <SelectField
                    label="Country"
                    options={countryOptions}
                    bind:value={country}
                    default_value="Choose your Country"
                />
                <TextField
                    placeholder="Add Pincode"
                    id="pincode"
                    label="Pincode"
                    bind:value={pincode}
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

    .sub-title::before {
        content: "+";
        position: absolute;
        right: 25px;
    }
    .content-box{
        border: 1px solid white;
        margin-top: 10px;
        margin-bottom: 10px;
        box-shadow: 0 20px 10px -20px rgba(0,0,0,0.45) inset, 0 -20px 10px -20px rgba(0,0,0,0.45) inset;
    }
</style>