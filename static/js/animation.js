document.addEventListener("DOMContentLoaded", function () {
    let observer = new IntersectionObserver(
        function (entries, observer) {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("visible");
                    observer.unobserve(entry.target); // Agar animasi tidak diputar ulang
                }
            });
        },
        { threshold: 0.2 }
    );

    document.querySelectorAll(".animate-slide, .animate-fade").forEach((el) => {
        observer.observe(el);
    });

    // 🔥 GSAP Animation for Smooth Page Transition
    gsap.from("header", { y: -50, opacity: 0, duration: 1 });
    gsap.from("footer", { y: 50, opacity: 0, duration: 1 });
});
