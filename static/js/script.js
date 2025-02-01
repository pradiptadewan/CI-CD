document.addEventListener("DOMContentLoaded", function () {
    // 🔥 Hero Slideshow dengan Efek Animasi yang Lebih Halus
    let slides = document.querySelectorAll(".hero-slide");
    let currentIndex = 0;

    function showNextSlide() {
        slides[currentIndex].classList.remove("active");
        slides[currentIndex].classList.add("fade-out");

        currentIndex = (currentIndex + 1) % slides.length;

        slides[currentIndex].classList.remove("fade-out");
        slides[currentIndex].classList.add("active");
    }

    slides[currentIndex].classList.add("active");
    setInterval(showNextSlide, 3000);

    // 🏆 Reveal Animation (Muncul saat Scroll) dengan transisi geser
    const revealElements = document.querySelectorAll(".reveal");

    function handleScroll() {
        revealElements.forEach((el) => {
            let position = el.getBoundingClientRect().top;
            let windowHeight = window.innerHeight;

            if (position < windowHeight - 100) {
                el.classList.add("visible");
            }
        });
    }

    window.addEventListener("scroll", handleScroll);
    handleScroll();

    // 🎥 Efek Parallax saat Scroll
    const parallaxSections = document.querySelectorAll(".parallax");

    function parallaxEffect() {
        parallaxSections.forEach((section) => {
            let speed = section.getAttribute("data-speed");
            let yOffset = window.scrollY * speed;
            section.style.transform = `translateY(${yOffset}px)`;
        });
    }

    window.addEventListener("scroll", parallaxEffect);

    // 🎮 Efek Mouse Parallax di Hero Section
    const hero = document.querySelector(".hero-overlay");

    hero.addEventListener("mousemove", (e) => {
        let x = (window.innerWidth - e.pageX * 2) / 90;
        let y = (window.innerHeight - e.pageY * 2) / 90;

        hero.style.transform = `translateX(${x}px) translateY(${y}px)`;
    });

    hero.addEventListener("mouseleave", () => {
        hero.style.transform = "translateX(0px) translateY(0px)";
    });

    // Fungsi untuk memeriksa apakah elemen berada di dalam viewport
    function checkVisibility() {
        const elements = document.querySelectorAll('.animate-slide-up'); // Memilih semua elemen dengan kelas animate-slide-up

        elements.forEach((element) => {
            const rect = element.getBoundingClientRect(); // Mendapatkan posisi elemen relatif terhadap viewport

            if (rect.top <= window.innerHeight && rect.bottom >= 0) {
                // Jika elemen masuk dalam viewport, tambahkan kelas visible
                element.classList.add('visible');
            }
        });
    }

    // Menjalankan fungsi checkVisibility saat halaman discroll
    window.addEventListener('scroll', checkVisibility);

    // Jalankan fungsi checkVisibility saat halaman dimuat pertama kali
    checkVisibility();
});
