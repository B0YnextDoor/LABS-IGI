import { useNavigate, useParams } from "react-router-dom";
import { CONFIG } from "../../config/config";
import { useProfile } from "../../hooks/useProfile";
import { useNewsDetail } from "./hooks/useNewsDetail";
import { Loader } from "../../components/loader/Loader";
import { PAGES } from "../../config/routes";
import { useDeleteNews } from "./hooks/useDeleteNews";

export const NewsDetail = () => {
  const nav = useNavigate();
  const { id } = useParams();
  const { data } = useProfile();
  const { news, isLoading } = useNewsDetail(id);
  const { deleteNews, isDeleting } = useDeleteNews(id);
  return (
    <div className="news-page">
      {isLoading || !news ? (
        <Loader />
      ) : (
        <div>
          <h1>News Detail</h1>
          <div className="news-detail">
            <section className="info">
              <img
                src={`${CONFIG.BASE_URL}/${news.imagePath}`}
                alt="news img"
                width={320}
                height={320}
              />
              <section>
                <h2>{news.title}</h2>
                <h3>{news.text}</h3>
                <p>{new Date(news.created_at).toLocaleDateString()}</p>
              </section>
            </section>
            {data && data?.role === CONFIG.ROLES.ADMIN ? (
              <section className="news-controls">
                <button
                  className="btn btn-admin"
                  disabled={isDeleting}
                  onClick={() => nav(`${PAGES.NEWS_FORM}/${news._id}`)}
                >
                  Update
                </button>
                <button
                  className="btn btn-admin"
                  disabled={isDeleting}
                  onClick={() => deleteNews()}
                >
                  Delete
                </button>
              </section>
            ) : (
              <></>
            )}
          </div>
        </div>
      )}
    </div>
  );
};
