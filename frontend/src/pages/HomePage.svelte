<script>   
    import Icon from "@iconify/svelte";
    import dotsY from "@iconify/icons-pepicons-pop/dots-y";
    import { onMount } from "svelte";
    
    let showMenu = false;
    let selected = null;
    let deleteId = "";
    let downloadId = "";
    let downloadMessage = "";
    let emailId = null;
    let data = [];
    let searchData = "";
    let deletionWarning = false;

    function toggleMenu(id) {
      if (selected === id){
        showMenu = !showMenu;
      } else{
        showMenu = true;
      }
      selected = id;
    }

   
    // function to fetch all records from DB
    onMount(async () => {
        const response = await fetch("http://127.0.0.1:8000/resumes");
        const responseData = await response.json();
        data = responseData;
    })

    //  function to open and close model for delete operation
    function deleteRecordModel(id){
      deletionWarning = !deletionWarning;
      deleteId = id;
    }

    // function to delete record from DB
    async function deleteRecord(){
      await fetch(`http://127.0.0.1:8000/delete-resume/${deleteId}`,
      {
        method: "DELETE"
      });
      document.location.reload();
    }
    
    // function to download resume
    async function downloadResume(res_id){
      downloadId = res_id;
      await fetch(`http://127.0.0.1:8000/download/${downloadId}`,
      {
        method: "GET"
      });
      downloadMessage = "Resume downloaded successfully"
    }

    // function to search resume according to email
    async function searchEmail(){
      searchData = [];
      emailId = document.getElementById("search-item").value;
      if (emailId) {
      const response = await fetch(`http://127.0.0.1:8000/find-resume/${emailId}`,
      {
        method: "GET"
      });
      const responseData = await response.json();
      searchData = responseData;
    }
    else if (emailId == null){
      const response = await fetch("http://127.0.0.1:8000/resumes",
      {
        method: "GET"
      });
      const responseData = await response.json();
      data = responseData;
    }
    document.getElementById("search-item").value = "";
    }
    
  </script>
  <body>
  
  
    <h1 class="container">All Resumes</h1>
    
    <div class="search-container">
      <input
        type="text"
        placeholder="Search by name or email..."
        class="search-input"
        id="search-item"
        />
        <!-- bind:value={emailId} -->
     
      <button type="button" class="search-btn" on:click={searchEmail}>Find</button>
      <div class="add-icon">
        <div class="title">
          <a href="#/CreateResume" class="newresume"> <span class="add">+</span> New Resume</a>
        </div>
  
      </div>
    </div>
    {#if downloadMessage}
    <div class="success">
      <span class="closebtn" on:click={() => (downloadMessage = "")}>&times;</span>
      <p>{downloadMessage}</p>
    </div>
    {/if}
    <div>
      
      <table>
        <thead>
          <tr class="heading">
            <th>ID</th>
            <th>Full Name</th>
            <th>Phone Number</th>
            <th>Email ID</th>
            <th id="icon_heading"></th>
          </tr>
        </thead>
        {#if deletionWarning}
                <div class="delete-page" on:click={() => {deletionWarning = false;}}>
                  <div class="delete-container" >
                    <p class="delete-title">Delete Resume</p>
                    <p class="message">Are you sure you want to delete?</p>
                    <div class="button-container">
                      <button class="btn-cancel" on:click={() => {deletionWarning = false;}}>Cancel</button>
                      <button class="btn-delete" on:click={deleteRecord}>Yes, Delete</button>
                    </div>
                  </div>
                </div>
        {/if}
        <tbody>
        {#if searchData != ""}
        <tr>
          <td>{searchData.id}</td>
          <td>{searchData.full_name}</td>
          <td>{searchData.phone_number}</td>
          <td>{searchData.email_id}</td>
          
          <td id="icon_column">
            <div class="IconContainer" on:click={() => toggleMenu(value.id)}>
              <Icon icon={dotsY} />
            </div>
            {#if showMenu && selected === value.id}
            <div class="dropdown-content">             
              <button on:click={() => {showMenu = false; downloadResume(value.id) }}>Download</button>
              <button on:click={() => {showMenu = false;}}>Edit</button>
              <button on:click={() => {showMenu = false; deleteRecordModel(value.id) }}>Delete</button>
            </div>
          {/if}  
          </td>
          </tr>
      
          {:else}

          {#each Object.entries(data) as [key, value]}   
          <tr>
            <td>{value.id}</td>
            <td>{value.full_name}</td>
            <td>{value.phone_number}</td>
            <td>{value.email_id}</td>
            
            <td id="icon_column">
              <div class="IconContainer" on:click={() => toggleMenu(value.id)}>
                <Icon icon={dotsY} />
              </div>
              {#if showMenu && selected === value.id}
              <div class="dropdown-content">             
                <button on:click={() => {showMenu = false; downloadResume(value.id) }}>Download</button>
                <button on:click={() => {showMenu = false;}}>Edit</button>
                <button on:click={() => {showMenu = false; deleteRecordModel(value.id) }}>Delete</button>
              </div>
            {/if}  
            </td>  
            </tr>

            {/each}
            {/if}
        </tbody>
       
      </table>
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
      /* border-radius: 5px; */
      /* background: url("https://static.thenounproject.com/png/101791-200.png") no-repeat left; */
      background-size: 20px;
    }
    .search-btn{
      width: 60px;
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
   
    /* styles for listing table  */
    table {
      margin-top: 20px;
      width: 100%;
      border-collapse: collapse;
    }
  
    thead {
      background: lightgray;
    }
  
    tbody tr:nth-child(even) {
      background-color: #f2f2f2;
    }
  
    tbody tr:nth-child(odd) {
      background-color: #ffffff;
    }
  
    th,
    td {
      padding: 10px;
      text-align: left;
    }
    
    /* styles for additional options icon */
    .IconContainer {
      /* background-color: green; */
      height: auto;
      position: relative;
      cursor: pointer;
    }
    .dropdown-content {
      display: flex;
      flex-direction: column;
      position: absolute;
      /* width: 62px; */
      border: 1px;
      border-radius: 5px;
      /* background: none; */
      height: 110px;
      padding: 5px; 
      background-color: rgb(240, 235, 235);

      /* border-radius: 5px;
      
      /* box-shadow: rgba(0, 0, 0, 0.4) 0px 2px 4px,
        rgba(0, 0, 0, 0.3) 0px 7px 13px -3px,
        rgba(0, 0, 0, 0.2) 0px -3px 0px inset; */
    }
    .dropdown-content button{
        /* background: none; */
        width: 100%;
        border-radius: 5px;
        border: none;
        size: 1px;
    }
    #icon_column {
      width: 138px;
      height: 37px;
      text-align: center;
    }
    #icon_heading {
      width: 138px;
    }

     /* deletion model css */
     .delete-page {
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    width: 100%;
    position: fixed;
  }
  .delete-title {
    background-color: teal;
    color: white;
    padding: 10px;
    margin: 0px;
  }
  .delete-container {
    width: 50%;
    padding: 1px;
    left: 0;
    margin-left: 25%;
    border: 1px solid #ccc;
    border-radius: 10px;
    position: absolute;
    top: 15%;
    box-shadow: 5px 5px 5px #000;
    background-color: #fff;
    justify-content: center;
  }
  .btn-delete {
    background-color: teal;
    color: #fff;
    border: none;
    padding: 10px 20px;
    margin: 10px;
    border-radius: 5px;
    cursor: pointer;
  }
  /* Cancel button styles */
  .btn-cancel {
    background: none;
    border: hidden;
    color: teal;
  }
  .button-container {
    text-align: center;
    justify-content: center;
  }
  p {
    text-align: center;
  }

   /* download message css */
  .success p {
    color: #252525;
    font-size: 20px;
    height: 13px;
    margin-left: 6px;
  }
 
  .success{
    padding: 8px;
    background-color: rgb(150, 247, 156);
    color: rgb(0, 0, 0);
    margin-bottom: 15px;
    text-align: center;
    margin: 0 auto;
    width: 50%;
    margin-top: 9px;
  }
  /* The close button */
  .closebtn {
    margin-left: 15px;
    color: rgb(0, 0, 0);
    font-weight: bold;
    float: right;
    font-size: 22px;
    line-height: 20px;
    cursor: pointer;
    transition: 0.3s;
  }
</style>