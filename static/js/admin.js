document.addEventListener('DOMContentLoaded', function () {
  // Toggle dark mode functionality
  const darkModeToggleBtn = document.getElementById('darkModeToggleBtn');
  darkModeToggleBtn.addEventListener('click', function() {
    document.body.classList.toggle('dark-mode');
    // Save the preference to localStorage
    if (document.body.classList.contains('dark-mode')) {
      localStorage.setItem('darkMode', 'enabled');
    } else {
      localStorage.removeItem('darkMode');
    }
  });

  // Apply dark mode on page load if previously enabled
  if (localStorage.getItem('darkMode') === 'enabled') {
    document.body.classList.add('dark-mode');
  }

  // Sidebar toggle functionality
  let sidebar = document.querySelector(".sidebar");
  let sidebarBtn = document.querySelector(".sidebarBtn");
  sidebarBtn.onclick = function() {
    sidebar.classList.toggle("active");
    if(sidebar.classList.contains("active")){
      sidebarBtn.classList.replace("bx-menu", "bx-menu-alt-right");
    } else {
      sidebarBtn.classList.replace("bx-menu-alt-right", "bx-menu");
    }
  };
});
