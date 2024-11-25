import { useQuery } from "@tanstack/react-query";
import { reviewService } from "../../../services/review.service";

export const useReviews = () => {
  const { data, isLoading } = useQuery({
    queryKey: ["reviews"],
    queryFn: () => reviewService.getAll(),
  });

  return { reviews: data, isLoading };
};
