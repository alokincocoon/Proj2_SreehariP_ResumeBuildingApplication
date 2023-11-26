<script>
  import FormInput from "./components/FormInput.svelte";
  import EditData from "./pages/EditData.svelte";

  import HomePage from "./pages/HomePage.svelte";
  import Router from "svelte-spa-router";

  let routes = {
    "/": HomePage,
    "/CreateResume": FormInput,
    "/EditResume": EditData,
  };
</script>

<Router {routes} />

<style>
</style>
