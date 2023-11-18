<script>   
    import Icon from "@iconify/svelte";
    // import addIcon from "@iconify/icons-mdi/add";
    import AllResumes from "./AllResumes.svelte";
  </script>
  <body>
  
  
    <h1 class="container">All Resumes</h1>
  
    <div class="search-container">
      <input
        type="text"
        placeholder="Search by name or email..."
        name="search"
        class="search-input"
      /><Icon icon="material-symbols:search" width="24"/>
      <div class="add-icon">
        <div class="title">
          <a href="#/CreateResume" class="newresume"> <span class="add">+</span> New Resume</a>
        </div>
  
      </div>
    </div>
    <div>
      <AllResumes />
    </div>
  
  </body>
  <style>
   body {
      background: white;
      height: 100%;
      width: 100%;
    }
  
    .container {
      display: flex;
      align-items: center;
      width: 98%;
      height: 60px;
      margin-left: auto;
      margin-right: auto;
      background-color: white;
      border-bottom: 2px solid black;
    }
  
    .search-container {
      display: flex;
      align-items: center;
      width: 100%;
      background-color: white;
      position: relative;
    }
  
    .search-input {
      margin-left: 15px;
      padding-left: 25px;
      border-radius: 5px;
      /* background: url("https://static.thenounproject.com/png/101791-200.png") no-repeat left; */
      background-size: 20px;
    }
     
    .add-icon {
      color: rgb(0, 80, 160);
      display: flex;
      align-items: center;
      margin-left: auto; 
    }
    .add{
      font-size: 20px;
    }
    .title {
      margin-right: 8px;
    }
    a{
      text-decoration: none;
    }
</style>