import { useCallback, useEffect } from "react";

const handleScroll = (leftShelfRef, rightShelfRef) => () => {
  if (!leftShelfRef.current || !rightShelfRef.current) return;

  const maxOffset = 670;
  const section = document.querySelector(".book-section");
  const sectionTop = section.offsetTop;
  const sectionHeight = section.offsetHeight;
  const scrollY = window.scrollY;

  if (scrollY >= sectionTop && scrollY <= sectionTop + sectionHeight) {
    const scrollPercent = Math.min((scrollY - sectionTop) / sectionHeight, 1);
    const leftOffset = -maxOffset * scrollPercent;
    const rightOffset = maxOffset * scrollPercent;

    leftShelfRef.current.style.transform = `translateX(${leftOffset}px)`;
    rightShelfRef.current.style.transform = `translateX(${rightOffset}px)`;
  }
};

const handleScrollLetters = (lettersRef) => () => {
  const scrollY = window.scrollY;
  const windowHeight = window.innerHeight;
  const windowWidth = window.innerWidth;
  const letters = lettersRef.current;
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
};

export const useScroll = (leftShelfRef, rightShelfRef, lettersRef) => {
  const scroll = useCallback(handleScroll(leftShelfRef, rightShelfRef), [
    leftShelfRef.current,
    rightShelfRef.current,
  ]);
  const scrollLetters = useCallback(handleScrollLetters(lettersRef), [
    lettersRef.current,
  ]);
  useEffect(() => {
    window.addEventListener("scroll", scroll);
    window.addEventListener("scroll", scrollLetters);

    return () => {
      window.removeEventListener("scroll", scroll);
      window.removeEventListener("scroll", scrollLetters);
    };
  });
};
