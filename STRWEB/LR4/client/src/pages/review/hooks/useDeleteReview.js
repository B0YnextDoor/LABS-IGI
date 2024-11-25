import { useMutation, useQueryClient } from "@tanstack/react-query";
import { reviewService } from "../../../services/review.service";
import { toast } from "sonner";

export const useDeleteReview = (id) => {
  const client = useQueryClient();
  const { mutate, isPending } = useMutation({
    mutationKey: [`del_review_${id || "0"}`],
    mutationFn: () => reviewService.delete(id),
    onSuccess() {
      toast.info("Review deleted");
      client.invalidateQueries({ queryKey: ["reviews"] });
    },
    onError(e) {
      console.log(e);
      toast.error(e.response.data || "Deleting review error!");
    },
  });

  return { deleteRev: mutate, isDeleting: isPending };
};
