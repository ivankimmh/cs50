document.addEventListener("DOMContentLoaded", function () {
    const mobileMenu = document.querySelector(".mobile-menu");
    const nav = document.querySelector("header");
    const navListLarger = document.querySelector(".nav-list-larger");

    mobileMenu.addEventListener("click", function () {
      nav.classList.toggle("active");
      navListLarger.classList.toggle("active");
      mobileMenu.classList.toggle("active");
    });
  });
