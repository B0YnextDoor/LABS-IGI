import { useReviewAction } from "./hooks/useReviewAction";
import { useForm } from "react-hook-form";
import { Link } from "react-router-dom";
import { PAGES } from "../../config/routes";

export const Review = () => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm({
    mode: "onChange",
  });
  const { isUpdate, action, isPending } = useReviewAction(reset);

  const onSubmit = (data) => action(data);
  return (
    <div className="review-page rev-form-page">
      <h1>{isUpdate ? "Update" : "Create"} review</h1>
      <div className="ret-to-revs">
        <Link to={PAGES.REVIEWS} className="animated-link">
          Back to reviews
        </Link>
      </div>
      <form className="form rev-form" onSubmit={handleSubmit(onSubmit)}>
        <div>
          <label>Rate:</label>
          <input
            type="number"
            {...register("rate", {
              required: "Review rate is required!",
              min: 1,
              max: 5,
            })}
          />
        </div>
        {errors?.rate?.type === "required" && (
          <span>{errors?.rate?.message}</span>
        )}
        {errors?.rate?.type === "min" && <span>Minimal rate is 1!</span>}
        {errors?.rate?.type === "max" && <span>Maximal rate is 5!</span>}
        <div>
          <label>Review text:</label>
          <textarea
            {...register("text", { required: "Review text is required!" })}
          />
        </div>
        {errors?.text?.type === "required" && (
          <span>{errors?.text?.message}</span>
        )}
        <button className="btn" disabled={isPending} type="submit">
          {isUpdate ? "Save" : "Create"}
        </button>
      </form>
    </div>
  );
};
