import { useParams } from "react-router-dom";
import { useCreateReview } from "./useCreateReview";
import { useUpdateReview } from "./useUpdateReview";
import { useReview } from "./useReview";
import { useEffect, useState } from "react";

export const useReviewAction = (reset) => {
  const { id } = useParams();
  const { create, isCreating } = useCreateReview();
  const { update, isUpdating } = useUpdateReview(id);
  const { review } = useReview(id);

  const [data, setData] = useState({
    action: create,
    isPending: isCreating,
  });

  useEffect(() => {
    if (id && review) {
      setData({ isUpdate: true, action: update, isPending: isUpdating });
      reset({
        rate: review.rate,
        text: review.text,
      });
    }
  }, [id, review]);

  return { ...data };
};
