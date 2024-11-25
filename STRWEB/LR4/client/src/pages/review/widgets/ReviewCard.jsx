import { CONFIG } from "../../../config/config";
import { PAGES } from "../../../config/routes";
import { useDeleteReview } from "../hooks/useDeleteReview";

export const ReviewCard = ({ review, data, nav }) => {
  const { deleteRev, isDeleting } = useDeleteReview(review._id, nav);
  return (
    <div className="rev-card">
      <section>
        <h2>{review.customer.name}</h2>
        <h4>{review.rate}</h4>
        <pre>{review.text}</pre>
        <p>{new Date(review.updated_at).toLocaleDateString()}</p>
      </section>
      {data &&
        data?.role === CONFIG.ROLES.CUSTOMER &&
        data?._id === review.customer._id && (
          <section>
            <button
              className="btn"
              onClick={() => nav(`${PAGES.REVIEW}/${review._id}`)}
              disabled={isDeleting}
            >
              Update
            </button>
            <button
              className="btn"
              onClick={() => deleteRev()}
              disabled={isDeleting}
            >
              Delete
            </button>
          </section>
        )}
    </div>
  );
};
