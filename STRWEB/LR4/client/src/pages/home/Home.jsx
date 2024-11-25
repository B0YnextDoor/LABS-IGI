import { Link } from "react-router-dom";
import styles from "./Home.module.css";
import Banner from "../../components/banner/Banner.jsx";
import { Animation } from "../../components/animation/Amination.jsx";
import { LatestNews } from "./widgets/LatestNews.jsx";
import { ApiSection } from "./widgets/ApiSection.jsx";

export const Home = () => {
  return (
    <section className={styles.maincont}>
      <Animation />
      <section className={styles.main_section}>
        <img src="/about/logo.jpg" alt="logo" width="150" />
        <p>
          Welcome to <em>BOOKY</em>
          <br />
          A very cool bookshop with your favourite authors!
          <br />
          Check out our catalog{" "}
          <Link to="/books" className="animated-link">
            <em>right here</em>!
          </Link>
        </p>
      </section>
      <section className={styles.content_section}>
        <div className={styles.content}>
          <ApiSection />
          <LatestNews />
        </div>
        <aside>
          <Banner />
        </aside>
      </section>
    </section>
  );
};
