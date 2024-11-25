import { useRef } from "react";
import { useScroll } from "../hooks/useScroll";

export const AnimatedScroll = () => {
  const leftShelfRef = useRef(null);
  const rightSchelfRef = useRef(null);
  const lettersRef = useRef([]);
  useScroll(leftShelfRef, rightSchelfRef, lettersRef);
  return (
    <>
      <div className="scroll-container">
        <section className="book-section">
          <div className="book-shelf left" id="book1" ref={leftShelfRef}>
            <img src="/about/book1.jpg" alt="" />
          </div>
          <div className="book-shelf right" id="book2" ref={rightSchelfRef}>
            <img src="/about/book2.jpg" alt="" />
          </div>
        </section>
      </div>
      <div className="scroll-container-letters">
        <section className="letters-section">
          {letters.map((l, i) => (
            <div
              key={l}
              className="letter"
              ref={(el) => (lettersRef.current[i] = el)}
            >
              {l}
            </div>
          ))}
        </section>
      </div>
    </>
  );
};

const letters = [
  "A",
  "B",
  "C",
  "D",
  "E",
  "F",
  "G",
  "H",
  "I",
  "J",
  "K",
  "L",
  "M",
];
