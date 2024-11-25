import { useQuery } from "@tanstack/react-query";
import { newsService } from "../../services/news.service";

export const useNews = () => {
  const { data, isLoading } = useQuery({
    queryKey: ["news"],
    queryFn: () => newsService.getAll(),
    retry: 1,
  });

  return { news: data, isLoading };
};
