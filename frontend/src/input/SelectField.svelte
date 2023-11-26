<script>
  export let id = "";
  export let label = "";
  export let options = [];
  export let value;
  export let defaultValue = "";
</script>

<main>
  <div class="form-content">
    <div class="select-field">
      <div class="label">
        <label for={id}>{label}</label>
      </div>
      <div class="select-values">
        <select bind:value>
          <option value="">{defaultValue}</option>
          {#each options as option}
            <option value={option}>{option}</option>
          {/each}
        </select>
      </div>
    </div>
  </div>
</main>

<style>
  select option:first-child {
    display: none;
  }
  .select-field {
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
  .select-values {
    width: 80%;
    height: 43px;
  }
  select {
    width: 40%;
    height: 40px;
    padding-left: 5px;
    border: none;
    border-bottom: 2px inset teal;
    border-radius: 0px;
    margin: 0px;
    background-color: white;
  }
  select:focus {
    outline: none;
  }
</style>
