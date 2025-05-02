document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.querySelector(".mobile-nav-toggle");
    const navList = document.querySelector(".navmenu ul");
  
    toggle.addEventListener("click", () => {
      navList.classList.toggle("active");
  
      // Optional: toggle between list and close icon if using icon fonts
      toggle.classList.toggle("bi-list");
      toggle.classList.toggle("bi-x");
    });
  });
  