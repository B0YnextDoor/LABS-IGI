import { useMutation } from "@tanstack/react-query";
import { useNavigate } from "react-router-dom";
import { newsService } from "../../../services/news.service";
import { toast } from "sonner";
import { PAGES } from "../../../config/routes";

export const useCreateNews = () => {
  const nav = useNavigate();
  const { mutate, isPending } = useMutation({
    mutationKey: ["create_news"],
    mutationFn: (data) => newsService.create(data),
    onSuccess() {
      toast.success("News created");
      nav(PAGES.NEWS);
    },
    onError(e) {
      console.log(e);
      toast.error(e.response.data || "Creating news error!");
    },
  });

  return { create: mutate, isCreating: isPending };
};
