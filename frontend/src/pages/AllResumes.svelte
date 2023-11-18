<script>
    import Icon from "@iconify/svelte";
    import dotsY from "@iconify/icons-pepicons-pop/dots-y";
    import { onMount } from "svelte";
  
    let showMenu = false;
    let selected = null;
    let deleteId = "";

    function toggleMenu(id) {
      if (selected === id){
        showMenu = !showMenu;
      } else{
        showMenu = true;
      }
      selected = id;
    }

    let data=[];
    let deletionWarning = false;

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
    }
  </script>
  
  <main>
    <table>
      <thead>
        <tr class="heading">
          <th>ID</th>
          <th>Full Name</th>
          <th>Phone Number</th>
          <th>Image URL</th>
          <th id="icon_heading"></th>
        </tr>
      </thead>
      {#if deletionWarning}
    
              <div class="delete-page" on:click={() => {deletionWarning = false;}}>
                <div class="container" >
                  <p class="title">Delete Resume</p>
                  <p class="message">Are you sure you want to delete?</p>
                  <div class="button-container">
                    <button class="btn-cancel" on:click={() => {deletionWarning = false;}}>Cancel</button>
                    <button class="btn-delete" on:click={deleteRecord}>Yes, Delete</button>
                  </div>
                </div>
              </div>

          {/if}
      <tbody>
        
        {#each Object.entries(data) as [key, value]}   
        <tr>
          <td>{value.id}</td>
          <td>{value.full_name}</td>
          <td>{value.phone_number}</td>
          <td>{value.image_url}</td>
          <td id="icon_column">
            <div class="IconContainer" on:click={() => toggleMenu(value.id)}>
              <Icon icon={dotsY} />
            </div>
            {#if showMenu && selected === value.id}
            <div class="dropdown-content">
              <button on:click={() => {showMenu = false;}}>Edit</button>
              <button on:click={() => {showMenu = false; deleteRecordModel(value.id)}}>Delete</button>
            </div>
          {/if}  
          </td>
          
          </tr>
          {/each}
          

      </tbody>
     
    </table>

  </main>
  
  <style>
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
      height: 78px;
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
    .dropdown-content a {
      margin-bottom: 7px;
    }

    /* delete model */
    .delete-page {
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    width: 100%;
    position: fixed;
  }
  .title {
    background-color: teal;
    color: white;
    padding: 10px;
    margin: 0px;
  }
  .container {
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

  </style>