import { useRef } from "react";
import { useAnimation } from "../hooks/useAnimation";

export const MainInfo = () => {
  const infoTextRef = useRef(null);
  const logoRef = useRef(null);
  const action = useAnimation(infoTextRef, logoRef);
  return (
    <>
      <section className="about-main-sec">
        <section className="logo-anim-sec">
          <img
            src="/about/logo.jpg"
            alt="logo"
            width="150"
            className="logo"
            id="logo-img"
            ref={logoRef}
          />
        </section>
        <section className="info-control-sec">
          <h3 id="info-text" ref={infoTextRef}>
            BOOKY is a very cool bookshop with your favourite authors!
          </h3>
        </section>
      </section>
      <section className="anim-btns">
        <button id="slower" title="slower x2" onClick={action.slower}>
          <img src="/about/faster.svg" alt="" />
        </button>
        <button id="play" title="play" onClick={action.play}>
          <img src="/about/play.svg" alt="" />
        </button>
        <button id="pause" title="pause" onClick={action.pause}>
          <img src="/about/pause.svg" alt="" />
        </button>
        <button id="cancel" title="cancel" onClick={action.stop}>
          <img src="/about/stop.svg" alt="" />
        </button>
        <button id="faster" title="faster x2" onClick={action.faster}>
          <img src="/about/faster.svg" alt="" />
        </button>
      </section>
    </>
  );
};
