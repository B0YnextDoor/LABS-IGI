import { useNews } from "../../../hooks/news/useNews";
import { Loader } from "../../../components/loader/Loader";
import { NewsCard } from "../../../components/news/NewsCard";

export const LatestNews = () => {
  const { news, isLoading } = useNews();

  return (
    <div>
      <h2>Lates news</h2>
      {isLoading ? (
        <Loader />
      ) : news && news.length ? (
        <NewsCard news={news[0]} full />
      ) : (
        <h2>There are no news...</h2>
      )}
    </div>
  );
};
