<script>
    // export let type = "";
    export let id = "";
    export let placeholder = "";
    export let label = "";
    export let value;
</script>

<main>
    <div class="form-content">
        <div class="text-field">
            <div class="label">
                <label for={id}>{label}</label>
            </div>
            <div class="text-input">
                <input {id} type="text" placeholder={placeholder} bind:value />
                <!-- <input {id} type="text" {placeholder} /> -->
            </div>
        </div>
    </div>
</main>

<style>
    .text-field {
        display: flex;
        border-top: solid 0.1px gray;
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
    .text-input {
        width: 80%;
        height: 43px;
    }
    input[type="text"] {
        /* width: 40%;
        height: 43px;
        padding-left: 5px;
        border: none;
        border-bottom: 2px black solid;
        border-radius: 0px;
        margin: 0px; */
        width: 40%;
        height: 40px;
        padding-left: 5px;
        border: none;
        border-bottom: 2px inset teal;
        border-radius: 5px;
        margin: 0px;
    }

</style>