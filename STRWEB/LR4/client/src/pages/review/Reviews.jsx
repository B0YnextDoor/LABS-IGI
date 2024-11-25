import { useNavigate } from "react-router-dom";
import { useProfile } from "../../hooks/useProfile";
import { useReviews } from "./hooks/useReviews";
import { Loader } from "../../components/loader/Loader";
import "./Reviews.css";
import { ReviewCard } from "./widgets/ReviewCard";
import { PAGES } from "../../config/routes";
import { CONFIG } from "../../config/config";

export const Reviews = () => {
  const nav = useNavigate();
  const { data } = useProfile();
  const { reviews, isLoading } = useReviews();

  return (
    <div className="review-page">
      {isLoading ? (
        <Loader />
      ) : reviews && reviews.length ? (
        <div className="rev-list">
          <h1>Our client's reviews</h1>
          {data && data?.role === CONFIG.ROLES.CUSTOMER && (
            <div className="add-rev">
              <button className="btn" onClick={() => nav(PAGES.REVIEW)}>
                Add Review
              </button>
            </div>
          )}
          {reviews.map((r, idx) => (
            <ReviewCard key={idx} review={r} data={data} nav={nav} />
          ))}
        </div>
      ) : (
        <h1>There are no reviews yet...</h1>
      )}
    </div>
  );
};
