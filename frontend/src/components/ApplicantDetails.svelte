<script>
  import TextField from "../input/TextField.svelte";
  import UrlField from "../input/UrlField.svelte";
  import EmailField from "../input/EmailField.svelte";
  import { slide } from "svelte/transition";

  export let open = true;
  const handleClick = () => (open = !open);

  export let full_name = "";
  export let email_id = "";
  export let phone_number = "";

  export let image_url = "";
  export let summary = "";
</script>

<main>
  <div class="container">
    <h3 class="accordion-title" on:click={handleClick}>
      Personal Information<span class="mandatory">*</span>
    </h3>
    {#if open}
      <div class="active" transition:slide>
        <TextField
          placeholder="eg: John Doe"
          id="name"
          label="Full Name"
          bind:value={full_name}
        />
        <EmailField
          placeholder="eg: abc@address.com"
          id="email"
          label="Email ID"
          bind:value={email_id}
        />

        <TextField
          placeholder="eg: 9876543210"
          id="phone"
          label="Phone Number"
          bind:value={phone_number}
        />
        <UrlField
          placeholder="A valid link of Google Drive/Dropbox/Onedrive"
          id="image-url"
          label="Image URL"
          bind:value={image_url}
        />
        <TextField
          placeholder="Enter your profile summary"
          id="summary"
          label="Summary"
          bind:value={summary}
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
  .container {
    border: 1px solid white;
    margin-top: 10px;
    margin-bottom: 10px;
    box-shadow: rgba(9, 30, 66, 0.25) 0px 4px 8px -2px,
      rgba(9, 30, 66, 0.08) 0px 0px 0px 1px;
    /* box-shadow: 0 20px 10px -20px rgba(0,0,0,0.45) inset, 0 -20px 10px -20px rgba(0,0,0,0.45) inset; */
  }

  .mandatory {
    color: red;
    size: 12px;
    font-weight: lighter;
    margin-left: 2px;
  }
</style>
