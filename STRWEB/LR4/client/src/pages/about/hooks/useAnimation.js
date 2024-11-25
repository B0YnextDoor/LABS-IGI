import { useCallback, useEffect } from "react";

const bounce = (timeFraction) => {
  for (let a = 0, b = 1; 1; a += b, b /= 2) {
    if (timeFraction >= (7 - 4 * a) / 11) {
      return (
        -Math.pow((11 - 6 * a - 11 * timeFraction) / 4, 2) + Math.pow(b, 2)
      );
    }
  }
};

const animate = ({ timing, draw, duration, callback }) => {
  let start = performance.now();
  const animateFrame = (time) => {
    let timeFraction = (time - start) / duration;
    if (timeFraction > 1) timeFraction = 1;

    let progress = timing(timeFraction);
    draw(progress);

    if (timeFraction < 1) {
      requestAnimationFrame(animateFrame);
    } else {
      callback();
    }
  };
  requestAnimationFrame(animateFrame);
};

const frames = [
  {
    transform: "scale(1,1)",
    boxShadow: "0 0 0 0 transparent",
  },
  {
    transform: "scale(1.2, 1.2)",
    boxShadow: "0px 0px 7px 2px #d4a770",
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

const animateText = (element) => {
  if (!element) return;

  const text = element.textContent;
  const to = text.length;
  const from = 0;

  animate({
    duration: 5000,
    timing: bounce,
    draw: (progress) => {
      const result = (to - from) * progress + from;
      element.textContent = text.slice(0, Math.ceil(result));
    },
    callback: () => {
      setTimeout(() => animateText(element), 2000);
    },
  });
};

export const useAnimation = (infoTextRef, logoRef) => {
  const handleSlower = useCallback(() => {
    if (logoRef.current?.animation) logoRef.current.animation.playbackRate /= 2;
  }, [logoRef.current]);

  const handleFaster = useCallback(() => {
    if (logoRef.current?.animation) logoRef.current.animation.playbackRate *= 2;
  }, [logoRef.current]);

  const handlePlay = useCallback(() => {
    if (
      logoRef.current?.animation &&
      logoRef.current.animation.playState !== "running"
    )
      logoRef.current.animation.play();
  }, [logoRef.current]);

  const handlePause = useCallback(() => {
    if (
      logoRef.current?.animation &&
      logoRef.current.animation.playState !== "paused"
    )
      logoRef.current.animation.pause();
  }, [logoRef.current]);

  const handleCancel = useCallback(() => {
    if (logoRef.current?.animation) {
      logoRef.current.animation.playbackRate = 1;
      logoRef.current.animation.cancel();
    }
  }, [logoRef.current]);

  useEffect(() => {
    if (infoTextRef.current) animateText(infoTextRef.current);

    if (logoRef.current) {
      const animation = logoRef.current.animate(frames, config);
      logoRef.current.animation = animation;
    }
  }, [infoTextRef.current, logoRef.current]);

  return {
    play: handlePlay,
    pause: handlePause,
    stop: handleCancel,
    slower: handleSlower,
    faster: handleFaster,
  };
};
