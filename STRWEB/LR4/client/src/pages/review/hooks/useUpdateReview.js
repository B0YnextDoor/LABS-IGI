import { useMutation, useQueryClient } from "@tanstack/react-query";
import { reviewService } from "../../../services/review.service";
import { toast } from "sonner";

export const useUpdateReview = (id) => {
  const client = useQueryClient();
  const { mutate, isPending } = useMutation({
    mutationKey: [`upd_review_${id || "0"}`],
    mutationFn: (data) => reviewService.update(id, data),
    onSuccess() {
      toast.success("Review updated");
      client.invalidateQueries({ queryKey: [`review_${id || "0"}`] });
    },
    onError(e) {
      console.log(e);
      toast.error(e.response.data || "Updating review error!");
    },
  });

  return { update: mutate, isUpdating: isPending };
};
