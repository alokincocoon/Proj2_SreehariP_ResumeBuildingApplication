<script>
  // export let type = "";
  export let id = "";
  export let placeHolder = "";
  export let label = "";
  export let value;
</script>

<main>
  <div class="formContent">
    <div class="date-field">
      <div class="label">
        <label for={id}>{label}</label>
      </div>
      <div class="date-input">
        <input {id} type="date" {placeHolder} bind:value />
        <!-- <input {id} type="text" {placeholder} /> -->
      </div>
    </div>
  </div>
</main>

<style>
  .date-field {
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
  .date-input {
    width: 80%;
    height: 43px;
  }

  input[type="date"] {
    width: 40%;
    height: 40px;
    padding-left: 5px;
    border: none;
    border-bottom: 2px inset teal;
    border-radius: 0px;
    margin: 0px;
  }
  input[type="date"] {
    outline: none;
  }
</style>
