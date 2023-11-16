<script>
    // export let type = "";
    export let id = "";
    export let placeHolder = "";
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
                <input {id} type="email" {placeHolder} bind:value />
                <!-- <input {id} type="text" {placeholder} /> -->
            </div>
        </div>
    </div>
</main>

<style>
    .email-field {
        display: flex;
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
        width: 100%;
        height: 43px;
        padding-left: 5px;
        border: none;
        border-radius: 0px;
        margin: 0px;
    }
 
</style>