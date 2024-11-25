import { useMutation } from "@tanstack/react-query";
import { reviewService } from "../../../services/review.service";
import { useNavigate } from "react-router-dom";
import { toast } from "sonner";
import { PAGES } from "../../../config/routes.js";

export const useCreateReview = () => {
  const nav = useNavigate();
  const { mutate, isPending } = useMutation({
    mutationKey: ["create_review"],
    mutationFn: (data) => reviewService.create(data),
    onSuccess() {
      toast.success("Review created");
      nav(PAGES.REVIEWS);
    },
    onError(e) {
      console.log(e);
      toast.error(e.response.data || "Creating review error!");
    },
  });

  return { create: mutate, isCreating: isPending };
};
