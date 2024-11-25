import { Link } from "react-router-dom";
import { CONFIG } from "../../config/config";
import { PAGES } from "../../config/routes";
import "./NewsCard.css";

export const NewsCard = ({ news, full }) => {
  return (
    <div className="news-card" style={full && { maxWidth: "none" }}>
      <img
        src={`${CONFIG.BASE_URL}/${news.imagePath}`}
        alt="news img"
        width={150}
        height={150}
      />
      <section>
        <h2>{news.title}</h2>
        <h3 className="summary">{news.text}</h3>
        <p>{new Date(news.created_at).toLocaleDateString()}</p>
        <Link to={`${PAGES.NEWS}/${news._id}`}>Read more</Link>
      </section>
    </div>
  );
};
