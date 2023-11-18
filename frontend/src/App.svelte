<script>
    import FormInput from "./components/FormInput.svelte";
    import HomePage from "./pages/HomePage.svelte";
    // import InputPage from "./pages/InputPage.svelte";	
	
	import Router from "svelte-spa-router"

	let routes = {
		"/": HomePage,
		"/CreateResume": FormInput,
	}
</script>


	<Router {routes}/>


<style>
 
</style>
