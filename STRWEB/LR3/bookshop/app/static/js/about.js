function bounce(timeFraction) {
  for (let a = 0, b = 1; 1; a += b, b /= 2) {
    if (timeFraction >= (7 - 4 * a) / 11) {
      return (
        -Math.pow((11 - 6 * a - 11 * timeFraction) / 4, 2) + Math.pow(b, 2)
      );
    }
  }
}

function animate({ timing, draw, duration, callback }) {
  let start = performance.now();
  requestAnimationFrame(function animate(time) {
    let timeFraction = (time - start) / duration;
    if (timeFraction > 1) timeFraction = 1;

    let progress = timing(timeFraction);

    draw(progress);

    if (timeFraction < 1) requestAnimationFrame(animate);
    else callback();
  });
}

function animateText(infoText) {
  let text = infoText.textContent;
  let to = text.length;
  let from = 0;
  animate({
    duration: 5000,
    timing: bounce,
    draw: function (progress) {
      let result = (to - from) * progress + from;
      infoText.textContent = text.slice(0, Math.ceil(result));
    },
    callback: function () {
      setTimeout(() => {
        animateText(infoText);
      }, 2000);
    },
  });
}

const frames = [
  {
    transform: "scale(1,1)",
    "box-shadow": "0 0 0 0 transparent",
  },
  {
    transform: "scale(1.2, 1.2)",
    "box-shadow": "0px 0px 7px 2px #d4a770",
  },
];

const config = {
  duration: 2000,
  delay: 1000,
  easing: "ease-in-out",
  iterations: Infinity,
  direction: "alternate",
  fill: "backwards",
};

const leftShelf = document.querySelector(".book-shelf.left");
const rightShelf = document.querySelector(".book-shelf.right");
const letters = document.querySelectorAll(".letter");

const maxOffset = 570;

function handleScroll() {
  const section = document.querySelector(".book-section");
  const sectionTop = section.offsetTop;
  const sectionHeight = section.offsetHeight;
  const scrollY = window.scrollY;

  if (scrollY >= sectionTop && scrollY <= sectionTop + sectionHeight) {
    const scrollPercent = Math.min((scrollY - sectionTop) / sectionHeight, 1);
    const leftOffset = -maxOffset * scrollPercent;
    const rightOffset = maxOffset * scrollPercent;

    leftShelf.style.transform = `translateX(${leftOffset}px)`;
    rightShelf.style.transform = `translateX(${rightOffset}px)`;
  }
}

function handleScrollLetters() {
  const scrollY = window.scrollY;
  const windowHeight = window.innerHeight;
  const windowWidth = window.innerWidth;
  const totalLetters = letters.length;

  letters.forEach((letter, index) => {
    const triggerPoint = index / totalLetters;

    if (scrollY > triggerPoint * windowHeight * 1.5) {
      letter.classList.add("visible");
      letter.style.marginLeft = `${(windowWidth * triggerPoint) / 1.5}px`;
    } else {
      letter.classList.remove("visible");
    }
  });
}

window.addEventListener("scroll", handleScroll);
window.addEventListener("scroll", handleScrollLetters);

document.addEventListener("DOMContentLoaded", () => {
  animateText(document.getElementById("info-text"));
  const logo = document.getElementById("logo-img");
  const animation = logo.animate(frames, config);

  document
    .getElementById("slower")
    .addEventListener("click", () => (animation.playbackRate /= 2));
  document.getElementById("play").addEventListener("click", () => {
    if (animation.playState != "running") animation.play();
  });
  document.getElementById("pause").addEventListener("click", () => {
    if (animation.playState != "paused") animation.pause();
  });
  document
    .getElementById("cancel")
    .addEventListener("click", () => animation.cancel());
  document
    .getElementById("faster")
    .addEventListener("click", () => (animation.playbackRate *= 2));
});
