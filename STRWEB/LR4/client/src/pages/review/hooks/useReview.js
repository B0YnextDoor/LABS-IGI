import { useQuery } from "@tanstack/react-query";
import { reviewService } from "../../../services/review.service";

export const useReview = (id) => {
  const { data, isLoading } = useQuery({
    queryKey: [`review_${id || "0"}`],
    queryFn: () => reviewService.getById(id),
  });

  return { review: data, isLoading };
};
