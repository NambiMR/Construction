let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".sidebarBtn");
sidebarBtn.onclick = function() {
  sidebar.classList.toggle("active");
  if(sidebar.classList.contains("active")){
  sidebarBtn.classList.replace("bx-menu" ,"bx-menu-alt-right");
}else
  sidebarBtn.classList.replace("bx-menu-alt-right", "bx-menu");
}

/* function toggleMode(){
  document.body.classList.toggle("dark-mode")
} */
document.addEventListener('DOMContentLoaded', function () {
  const darkModeToggleBtn = document.getElementById('darkModeToggleBtn');
  const body = document.body;

  darkModeToggleBtn.addEventListener('click', function () {
      body.classList.toggle('dark-mode');
      const isDarkMode = body.classList.contains('dark-mode');
      localStorage.setItem('darkModeEnabled', isDarkMode);
  });

  // Check local storage for dark mode preference
  const darkModeEnabled = localStorage.getItem('darkModeEnabled');
  if (darkModeEnabled === 'true') {
      body.classList.add('dark-mode');
  }
});
