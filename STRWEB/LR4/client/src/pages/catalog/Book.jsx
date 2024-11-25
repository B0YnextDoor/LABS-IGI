import { useBook } from "./hooks/useBook";
import { useProfile } from "../../hooks/useProfile";
import { Loader } from "../../components/loader/Loader";
import "./Catalog.css";
import { CONFIG } from "../../config/config";
import { ShoppingCart } from "lucide-react";
import { useParams, useNavigate } from "react-router-dom";
import { useDeleteBook } from "./hooks/useDeleteBook";
import { useAddToCart } from "../../hooks/cart/useAddToCart";
import { PAGES } from "../../config/routes";

export const Book = () => {
  const { id } = useParams();
  const { book, isLoading } = useBook(id);
  const { data } = useProfile();
  const nav = useNavigate();
  const { mutate, isDeleting } = useDeleteBook(id, nav);
  const { add, isAdding } = useAddToCart(id);
  return (
    <div className="book_detail_page">
      {isLoading || !book ? (
        <Loader />
      ) : (
        <div style={{ width: "60%", height: "100%" }}>
          <h1>Book details</h1>
          <div className="book_card_detail">
            <h2 style={{ marginBottom: "20px" }}>{book.title}</h2>
            <h3>
              Author: {book.author.surname} {book.author.name}
            </h3>
            <h3>Genre: {book.genre.name}</h3>
            <h2 className="amount">Price: {book.price} BYN</h2>
            {book.amount > 0 ? (
              <h2 className="amount">
                <strong>{book.amount}</strong> left!
              </h2>
            ) : (
              <h2 className="zero">Out of stock!</h2>
            )}
            {data?.role === CONFIG.ROLES.CUSTOMER && book.amount > 0 && (
              <div
                style={{
                  display: "flex",
                  width: "100%",
                  justifyContent: "end",
                }}
              >
                <button
                  className="add-to-cart"
                  disabled={isDeleting || isAdding}
                  onClick={() => add()}
                >
                  Add to Cart{" "}
                  <ShoppingCart
                    color="white"
                    size={30}
                    className="add-to-cart-img"
                  />
                </button>
              </div>
            )}
            {data?.role === CONFIG.ROLES.ADMIN && (
              <div className="admin_book_actions">
                <button
                  className="btn btn-admin"
                  onClick={() => nav(`${PAGES.BOOK_FORM}/upd`)}
                  disabled={isDeleting || isAdding}
                >
                  Edit
                </button>
                <button
                  className="btn btn-admin"
                  onClick={() => mutate()}
                  disabled={isDeleting || isAdding}
                >
                  Delete
                </button>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};
