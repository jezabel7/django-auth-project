document.addEventListener("DOMContentLoaded", function () {
    const themeToggleLink = document.getElementById("theme-toggle");
    const currentTheme = localStorage.getItem("theme");
    const taskCards = document.querySelectorAll(".task-card");
    const cardBodies = document.querySelectorAll(".card-body");
  
    // Aplica el tema guardado si existe
    if (currentTheme === "dark") {
      document.body.classList.add("bg-dark", "text-light");
      themeToggleLink.textContent = "Light Theme";
      updateNavbarTheme("dark");
      updateTaskCardsTheme("dark");
      updateCardBodiesTheme("dark");
    }
  
    // Cambia el tema al hacer clic en el enlace
    themeToggleLink.addEventListener("click", function (event) {
      event.preventDefault();
      document.body.classList.toggle("bg-dark");
      document.body.classList.toggle("text-light");
  
      const isDarkTheme = document.body.classList.contains("bg-dark");
      updateNavbarTheme(isDarkTheme ? "dark" : "light");
      updateTaskCardsTheme(isDarkTheme ? "dark" : "light");
      updateCardBodiesTheme(isDarkTheme ? "dark" : "light");
  
      if (isDarkTheme) {
        localStorage.setItem("theme", "dark");
        themeToggleLink.textContent = "Light Theme";
      } else {
        localStorage.setItem("theme", "light");
        themeToggleLink.textContent = "Dark Theme";
      }
    });
  
    function updateNavbarTheme(theme) {
      const navbar = document.querySelector(".navbar");
      if (theme === "dark") {
        navbar.classList.remove("navbar-light-custom");
        navbar.classList.add("navbar-dark-custom");
      } else {
        navbar.classList.remove("navbar-dark-custom");
        navbar.classList.add("navbar-light-custom");
      }
    }
  
    function updateTaskCardsTheme(theme) {
      taskCards.forEach(card => {
        if (theme === "dark") {
          card.classList.add("bg-secondary", "text-light");
        } else {
          card.classList.remove("bg-secondary", "text-light");
          card.classList.add("bg-light", "text-dark");
        }
      });
    }
  
    function updateCardBodiesTheme(theme) {
      cardBodies.forEach(cardBody => {
        if (theme === "dark") {
          cardBody.classList.add("card-body-dark");
          cardBody.classList.remove("card-body-light");
        } else {
          cardBody.classList.add("card-body-light");
          cardBody.classList.remove("card-body-dark");
        }
      });
    }
  });
  
  document.addEventListener("DOMContentLoaded", function () {
    // Maneja el botón para alternar la visibilidad de los comentarios
    const toggleButtons = document.querySelectorAll(".toggle-comments-btn");
  
    toggleButtons.forEach(button => {
      button.addEventListener("click", function () {
        const taskId = this.getAttribute("data-task-id");
        const commentsSection = document.getElementById(`comments-section-${taskId}`);
  
        if (commentsSection.style.display === "none" || commentsSection.style.display === "") {
          commentsSection.style.display = "block";  // Muestra los comentarios
          this.textContent = "Hide Comments";      // Cambia el texto del botón
        } else {
          commentsSection.style.display = "none";  // Oculta los comentarios
          this.textContent = "Show Comments";      // Cambia el texto del botón
        }
      });
    });
  });
  
  // Obtener el botón o link de cambio de tema
document.getElementById("theme-toggle").addEventListener("click", function () {
    const currentTheme = localStorage.getItem("theme");
  
    if (currentTheme === "light") {
      document.documentElement.setAttribute("data-bs-theme", "dark");
      localStorage.setItem("theme", "dark");
    } else {
      document.documentElement.setAttribute("data-bs-theme", "light");
      localStorage.setItem("theme", "light");
    }
  
    // Forzar el repintado de la página para aplicar el tema inmediatamente
    forceThemeUpdate();
  });
  
  // Función para forzar la actualización de la página al cambiar el tema
  function forceThemeUpdate() {
    // Forzar la recalculación del estilo y el repintado
    document.documentElement.style.display = 'none';
    document.documentElement.offsetHeight; // Forzar recalculación
    document.documentElement.style.display = '';
  }
  
  // Aplicar el tema al cargar la página según lo guardado en localStorage
  document.addEventListener("DOMContentLoaded", function () {
    const savedTheme = localStorage.getItem("theme") || "light";
    document.documentElement.setAttribute("data-bs-theme", savedTheme);
  });