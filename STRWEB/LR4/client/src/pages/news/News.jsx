import { useNews } from "../../hooks/news/useNews";
import { Loader } from "../../components/loader/Loader";
import "./News.css";
import { NewsCard } from "../../components/news/NewsCard";
import { useProfile } from "../../hooks/useProfile";
import { useNavigate } from "react-router-dom";
import { CONFIG } from "../../config/config";
import { PAGES } from "../../config/routes";

export const News = () => {
  const nav = useNavigate();
  const { data } = useProfile();
  const { news, isLoading } = useNews();
  return (
    <div className="news-page">
      <h1>Shop News</h1>
      {data && data?.role === CONFIG.ROLES.ADMIN && (
        <div className="add-news">
          <button
            className="btn btn-admin"
            onClick={() => nav(PAGES.NEWS_FORM)}
          >
            Add news
          </button>
        </div>
      )}
      {isLoading ? (
        <Loader />
      ) : news && news.length ? (
        news.map((n, idx) => <NewsCard news={n} key={idx} />)
      ) : (
        <h1>There are no news yet...</h1>
      )}
    </div>
  );
};
