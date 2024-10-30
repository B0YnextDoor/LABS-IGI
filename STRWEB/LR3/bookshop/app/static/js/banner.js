class Slider {
  constructor(sliderElement, options = {}) {
    this.slider = sliderElement;
    this.slides = this.slider.querySelectorAll(".slide");
    this.totalSlides = this.slides.length;
    this.currentSlide = 0;
    this.loop = options.loop || false;
    this.auto = options.auto || false;
    this.delay = options.auto && options.delay ? options.delay * 1000 : 5000;
    this.navs = options.navs !== undefined ? options.navs : true;
    this.pags = options.pags !== undefined ? options.pags : true;
    this.stopMouseHover = options.stopMouseHover || false;

    this.isPlaying = this.auto;
    this.intervalID = null;
    this.slideContainer = this.slider.querySelector(".slides");
    this.pagination = this.slider.querySelector(".pagination");
    this.prevBtn = this.slider.querySelector(".prev-btn");
    this.nextBtn = this.slider.querySelector(".next-btn");
    this.slideCounter = this.slider.querySelector(".slide-counter");
    this.slideTitle = this.slider.querySelector(".slide-title");

    this.init();
  }

  init() {
    this.updateSlideInfo();
    this.createPagination();
    this.addEventListeners();
    if (this.auto) {
      this.startAutoPlay();
    }
  }

  updateSlideInfo() {
    this.slideCounter.textContent = `${this.currentSlide + 1}/${
      this.totalSlides
    }`;
    this.slideTitle.textContent = this.slides[this.currentSlide].dataset.title;
  }

  createPagination() {
    if (!this.pags) return;

    this.pagination.innerHTML = "";
    for (let i = 0; i < this.totalSlides; i++) {
      const dot = document.createElement("div");
      dot.classList.add("pagination-dot");
      if (i === this.currentSlide) dot.classList.add("active");
      dot.addEventListener("click", () => this.goToSlide(i));
      this.pagination.appendChild(dot);
    }
  }

  addEventListeners() {
    if (this.navs) {
      this.prevBtn.addEventListener("click", () => this.goToPreviousSlide());
      this.nextBtn.addEventListener("click", () => this.goToNextSlide());
    } else {
      this.prevBtn.style.display = "none";
      this.nextBtn.style.display = "none";
    }

    if (this.stopMouseHover) {
      this.slider.addEventListener("mouseover", () => this.stopAutoPlay());
      this.slider.addEventListener("mouseout", () => this.startAutoPlay());
    }
  }

  goToPreviousSlide() {
    if (this.currentSlide === 0) {
      this.currentSlide = this.loop ? this.totalSlides - 1 : 0;
    } else {
      this.currentSlide--;
    }
    this.updateSlider();
  }

  goToNextSlide() {
    if (this.currentSlide === this.totalSlides - 1) {
      this.currentSlide = this.loop ? 0 : this.totalSlides - 1;
    } else {
      this.currentSlide++;
    }
    this.updateSlider();
  }

  goToSlide(index) {
    this.currentSlide = index;
    this.updateSlider();
  }

  updateSlider() {
    const offset = -this.currentSlide * 100;
    this.slideContainer.style.transform = `translateX(${offset}%)`;
    this.updateSlideInfo();
    this.updatePagination();
  }

  updatePagination() {
    if (!this.pags) return;

    const dots = this.pagination.querySelectorAll(".pagination-dot");
    dots.forEach((dot, index) => {
      dot.classList.toggle("active", index === this.currentSlide);
    });
  }

  startAutoPlay() {
    if (this.auto && !this.intervalID) {
      this.intervalID = setInterval(() => {
        this.goToNextSlide();
      }, this.delay);
    }
  }

  stopAutoPlay() {
    if (this.intervalID) {
      clearInterval(this.intervalID);
      this.intervalID = null;
    }
  }
}

// Инициализация слайдера
document.addEventListener("DOMContentLoaded", async () => {
  const sliderElement = document.getElementById("slider");

  const url = new URL("banner/", window.location.origin);
  url.searchParams.append("settings", "");

  // Выполняем fetch запрос
  const options = await fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .catch((error) => {
      console.error("Error:", error);
    });
  const slider = new Slider(sliderElement, {
    loop: options["loop"] ?? true, // Зацикливание
    navs: options["navs"] ?? true, // Стрелочки вкл/выкл
    pags: options["pags"] ?? true, // Пагинация вкл/выкл
    auto: options["auto"] ?? true, // Автоплей
    stopMouseHover: options["stopMouseHover"] ?? true, // Остановка при наведении
    delay: options["delay"] ?? 3, // Задержка в секундах
  });
});
