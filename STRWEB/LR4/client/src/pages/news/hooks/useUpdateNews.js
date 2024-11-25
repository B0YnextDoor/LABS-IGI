import { useMutation, useQueryClient } from "@tanstack/react-query";
import { newsService } from "../../../services/news.service";
import { toast } from "sonner";

export const useUpdateNews = (id) => {
  const client = useQueryClient();
  const { mutate, isPending } = useMutation({
    mutationKey: [`upd_news_${id || "0"}`],
    mutationFn: (data) => newsService.update(id, data),
    onSuccess() {
      toast.success("News updated");
      client.invalidateQueries({ queryKey: [`news_${id || "0"}`] });
    },
    onError(e) {
      console.log(e);
      toast.error(e.response.data || "Updating news error!");
    },
  });

  return { update: mutate, isUpdating: isPending };
};
