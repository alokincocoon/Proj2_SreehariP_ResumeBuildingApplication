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
    export let house_name="";
    export let district="";
    export let city="";
    export let state="";
    export let zip_code="";
    export let country= "";
    
</script>

<main>
    <div class="content-box">
        <h3 class="sub-title" on:click={handleClick}>Address Details<span class="mandatory">*</span></h3>
        {#if open}
            <div class="Active" transition:slide>
                <TextField
                    placeholder="eg: House Name/Flat No./Building Name"
                    id="address"
                    label="House Name"
                    bind:value={house_name}
                />
                <TextField
                    placeholder="eg: City/Village/Municipality Name"
                    id="city"
                    label="Locality"
                    bind:value={city}
                />
                <TextField
                    placeholder="Enter District Name"
                    id="district"
                    label="District"
                    bind:value={district}
                />
                
                <TextField
                    placeholder="Enter State Name"
                    id="state"
                    label="State"
                    bind:value={state}
                />

                <SelectField
                    label="Country"
                    options={countryOptions}
                    bind:value={country}
                    default_value="Choose your Country"
                />
                <TextField
                    placeholder="Enter your pincode"
                    id="pincode"
                    label="Pincode"
                    bind:value={zip_code}
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