import { useQuery } from "@tanstack/react-query";
import { newsService } from "../../../services/news.service";

export const useNewsDetail = (id) => {
  const { data, isLoading } = useQuery({
    queryKey: [`news_${id || "0"}`],
    queryFn: () => newsService.getById(id),
  });

  return { news: data, isLoading };
};
