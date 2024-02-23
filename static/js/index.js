
let menubar=document.querySelector("#menu-bar");
let mynav=document.querySelector(".nav");
let searchbar=document.querySelector("#search-bar");
let search=document.querySelector(".search-form");
menubar.onclick=()=>{
  menubar.classList.toggle("fa-times")
  mynav.classList.toggle("active")
  
}
searchbar.onclick=()=>{
  searchbar.classList.toggle("fa-times")
  search.classList.toggle("active")
  
}


