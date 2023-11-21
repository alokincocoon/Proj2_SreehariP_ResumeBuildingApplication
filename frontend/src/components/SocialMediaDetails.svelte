<script>
  
  import TextField from "../input/TextField.svelte";
  import UrlField from "../input/UrlField.svelte";

    export let open = false;
    import { slide } from "svelte/transition";
    const handleClick = () => (open = !open);

    export let social_media = [{ media_name: "", url: "", user_name: "" }];
    function addSocialData() {
        social_media = [
            ...social_media,
            { media_name: "", url: "", user_name: "" },
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
        {#each social_media as mediaData, i}
            <div class="Active" transition:slide>
                <TextField
                    placeholder="eg: LinkedIn/Instagram/Facebook (can give GitHub too)"
                    id="network"
                    label="Media Name"
                    bind:value={mediaData.media_name}
                />
                <UrlField
                    placeholder="eg: www.medianame.com/username"
                    id="network-url"
                    label="Profile URL"
                    bind:value={mediaData.url}
                />
                <TextField
                    placeholder="eg: user_name@123"
                    id="user-name"
                    label="User Name"
                    bind:value={mediaData.user_name}
                />
            </div>
            <div class="extra-fields">
                <button on:click|preventDefault={addSocialData}>
                <span class="add">+ Add Another</span></button>
                {#if i !== 0}
                    <button on:click|preventDefault={() => removeSocialMedia(i)}>
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
    .subTitle::before {
        content: "+";
        position: absolute;
        right: 25px;
    }
    .extra-fields{
        margin-top: 10px;
   }
   .extra-fields button{
        width: 175px;
        background-color: white;
        color: black;
        border-radius: 5px;
        border: none;
   }
   .extra-fields button:hover{
    cursor: pointer;
   }
   .contentBox{
        border: 1px solid white;
        margin-top: 10px;
        margin-bottom: 10px;
        box-shadow: rgba(9, 30, 66, 0.25) 0px 4px 8px -2px, rgba(9, 30, 66, 0.08) 0px 0px 0px 1px;
        /* box-shadow: 0 20px 10px -20px rgba(0,0,0,0.45) inset, 0 -20px 10px -20px rgba(0,0,0,0.45) inset; */
    }
</style>