<script>
  export let buttonLabel = "";
  export let typeOfButton = "";
  export let type = "";
</script>

<main>
  <button class={typeOfButton} {type}>{buttonLabel}</button>
</main>

<style>
  .save {
    width: 100px;
    background-color: teal;
    color: white;
    border-radius: 5px;
    margin: 10px 5px 10px 5px;
  }
  .cancel {
    width: 100px;
    background-color: white;
    color: black;
    border-radius: 5px;
    margin: 10px 5px 10px 5px;
  }
  button:hover {
    cursor: pointer;
  }
</style>
