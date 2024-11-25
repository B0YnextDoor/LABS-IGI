import { useMutation, useQueryClient } from "@tanstack/react-query";
import { newsService } from "../../../services/news.service";
import { toast } from "sonner";
import { useNavigate } from "react-router-dom";
import { PAGES } from "../../../config/routes";

export const useDeleteNews = (id) => {
  const client = useQueryClient();
  const nav = useNavigate();
  const { mutate, isPending } = useMutation({
    mutationKey: [`del_news_${id || "0"}`],
    mutationFn: () => newsService.delete(id),
    onSuccess() {
      toast.info("News deleted");
      client.invalidateQueries({ queryKey: ["news"] });
      nav(PAGES.NEWS);
    },
    onError(e) {
      console.log(e);
      toast.error(e.response.data || "Deleting news error!");
    },
  });

  return { deleteNews: mutate, isDeleting: isPending };
};
