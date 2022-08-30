let navbar = document.querySelector(".header .navbar");

document.querySelector("#menu-btn").onclick = () => {
    navbar.classList.add("active");
};

document.querySelector("#close-navbar").onclick = () => {
    navbar.classList.remove("active");
};

var swiper = new Swiper(".home-slider", {
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    loop: true,
    grabCursor: true,
});

var swiper = new Swiper(".home-courses-slider", {
    loop: true,
    grabCursor: true,
    spaceBetween: 5,
    breakpoints: {
        0: {
            slidesPerView: 1,
        },
        768: {
            slidesPerView: 2,
        },
    },
});
