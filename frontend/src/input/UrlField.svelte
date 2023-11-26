<script>
  export let id = "";
  export let placeholder = "";
  export let label = "";
  export let value;
</script>

<main>
  <div class="form-content">
    <div class="url-field">
      <div class="label">
        <label for={id}>{label}</label>
      </div>
      <div class="url-input">
        <input {id} type="url" {placeholder} bind:value />
      </div>
    </div>
  </div>
</main>

<style>
  .url-field {
    display: flex;
    border-left: none;
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
  .url-input {
    width: 80%;
    height: 43px;
  }
  input[type="url"] {
    width: 40%;
    height: 40px;
    padding-left: 5px;
    border: none;
    border-bottom: 2px inset teal;
    border-radius: 0px;
    margin: 0px;
  }
  input[type="url"] {
    outline: none;
  }
</style>
