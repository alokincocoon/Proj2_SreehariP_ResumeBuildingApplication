<script>
    // export let type = "";
    export let id = "";
    export let placeholder = "";
    export let label = "";
    export let value;
</script>

<main>
    <div class="form-content">
        <div class="email-field">
            <div class="label">
                <label for={id}>{label}</label>
            </div>
            <div class="email-input">
                <input {id} type="email" {placeholder} bind:value />
                <!-- <input {id} type="text" {placeholder} /> -->
            </div>
        </div>
    </div>
</main>

<style>
    .email-field {
        display: flex;
        /* border: none; */
        border: solid 0.1px gray;
        height: 43px;
    }
    .label {
        width: 20%;
        background-color: #f4f6f8;
        height: 43px;
    }
    label {
        padding-left: 12px;
        padding-top: 10px;
    }
    .email-input {
        width: 80%;
        height: 43px;
    }

    input[type="email"] {
        width: 40%;
        height: 40px;
        padding-left: 5px;
        border: none;
        border-bottom: 2px inset teal;
        border-radius: 5px;
        margin: 0px;
    }
 
</style>