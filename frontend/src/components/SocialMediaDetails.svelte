<script>
  
  import TextField from "../input/TextField.svelte";
  import UrlField from "../input/UrlField.svelte";

    export let open = false;
    import { slide } from "svelte/transition";
    const handleClick = () => (open = !open);

    export let social_media = [{ network: "", url: "", user_name: "" }];
    function addSocialData() {
        social_media = [
            ...social_media,
            { network: "", url: "", user_name: "" },
        ];
    }
    function removeSocialMedia(index) {
        if (social_media.length > 1) {
            social_media = social_media.filter((_, i) => i !== index);
        }
    }

    // export let network = '';
    // export let url = '';
    // export let user_name = '';
</script>

<div class="contentBox">
    <h3 class="subTitle" on:click={handleClick}>Social Media</h3>
    {#if open}
        {#each social_media as social_media_data, i}
            <div class="Active" transition:slide>
                <TextField
                    placeholder="Add Network"
                    id="network"
                    label="Network"
                    bind:value={social_media_data.network}
                />
                <UrlField
                    placeholder="Add URL"
                    id="network-url"
                    label="URL"
                    bind:value={social_media_data.url}
                />
                <TextField
                    placeholder="Add User Name"
                    id="user-name"
                    label="User Name"
                    bind:value={social_media_data.user_name}
                />
            </div>
            <div class="SocialMediaButtons">
                <button on:click|preventDefault={addSocialData}
                    >Add New Social Media</button
                >
                {#if i !== 0}
                    <button on:click|preventDefault={() => removeSocialMedia(i)}
                        >Remove Social Media</button
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

    .subTitle::before {
        content: "+";
        position: absolute;
        right: 25px;
    }
    .SocialMediaButtons{
        margin-top: 10px;
   }
   .SocialMediaButtons button{
        width: 175px;
        background-color: white;
        color: black;
        border-radius: 5px;
   }
   .contentBox{
        border: 1px solid white;
        margin-top: 10px;
        margin-bottom: 10px;
        box-shadow: 0 20px 10px -20px rgba(0,0,0,0.45) inset, 0 -20px 10px -20px rgba(0,0,0,0.45) inset;
    }
</style>