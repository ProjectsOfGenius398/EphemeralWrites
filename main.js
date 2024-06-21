let currentIndex = 0;

function showNextSlide() {
    const slides = document.querySelectorAll('.carousel .slide');
    const totalSlides = slides.length;

    currentIndex = (currentIndex + 1) % totalSlides;
    const carousel = document.querySelector('.carousel');
    carousel.style.transform = `translateX(-${currentIndex * 100}%)`;
}

// Auto-slide every 3 seconds
setInterval(showNextSlide, 3000)