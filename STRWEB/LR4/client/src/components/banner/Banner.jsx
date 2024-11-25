import { Component } from "react";
import styles from "./Banner.module.css";

const slides = [
  "https://skyeng.ru/",
  "https://bbminsk.by/",
  "https://vasilki.by/",
  "https://shop.cravt.by/",
];

class Banner extends Component {
  constructor(props) {
    super(props);
    this.state = {
      current: 0,
      total: slides.length,
      delay: 3500,
      interval: null,
    };
  }
  componentDidMount() {
    this.startAutoPlay();
  }
  next() {
    this.setState(
      (prev) => {
        const newCurrent =
          prev.current === prev.total - 1 ? 0 : prev.current + 1;
        return { current: newCurrent };
      },
      () => this.updateSlider()
    );
  }
  prev() {
    this.setState(
      (prev) => {
        const newCurrent =
          prev.current === 0 ? prev.total - 1 : prev.current - 1;
        return { current: newCurrent };
      },
      () => this.updateSlider()
    );
  }
  toSlide(i) {
    this.setState(
      () => {
        return { current: i };
      },
      () => this.updateSlider()
    );
  }
  updateSlider() {
    const offset = -this.state.current * 100;
    document.getElementById(
      "slides"
    ).style.transform = `translateX(${offset}%)`;
  }
  startAutoPlay() {
    if (!this.intervalID) {
      this.intervalID = setInterval(() => {
        this.next();
      }, this.state.delay);
    }
  }
  stopAutoPlay() {
    if (this.intervalID) {
      clearInterval(this.intervalID);
      this.intervalID = null;
    }
  }
  render() {
    return (
      <div className={styles.slider_container}>
        <div
          className={styles.slider}
          id="slider"
          onMouseOver={() => this.stopAutoPlay()}
          onMouseLeave={() => this.startAutoPlay()}
        >
          <div className={styles.slides} id="slides">
            {slides.map((link, idx) => (
              <div className={styles.slide} key={idx}>
                <a href={link} target="_blank">
                  <img
                    src={`/banner/banner${idx + 1}.png`}
                    alt={`Banner slide ${idx + 1}`}
                  />
                </a>
              </div>
            ))}
          </div>
          <div className={styles.slider_controls}>
            <button className={styles.prev_btn} onClick={() => this.prev()}>
              ←
            </button>
            <button className={styles.next_btn} onClick={() => this.next()}>
              →
            </button>
          </div>
          <div className={styles.pagination}>
            {slides.map((_, idx) => (
              <div
                key={idx}
                className={idx === this.state.current ? styles.active : {}}
                onClick={() => this.toSlide(idx)}
              />
            ))}
          </div>
          <div className={styles.slide_info}>
            <span className={styles.slide_counter}>
              {this.state.current + 1} / {this.state.total}
            </span>
            <span className={styles.slide_title}>{`Banner ${
              this.state.current + 1
            }`}</span>
          </div>
        </div>
      </div>
    );
  }
}

export default Banner;
