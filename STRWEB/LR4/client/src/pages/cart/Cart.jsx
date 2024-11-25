import { useCart } from "../../hooks/cart/useCart";
import { Loader } from "../../components/loader/Loader";
import "./Cart.css";
import { CartItem } from "./widgets/CartItem";
import { useMemo } from "react";
import { useNavigate } from "react-router-dom";
import { PAGES } from "../../config/routes";

export const Cart = () => {
  const { cart, isLoading } = useCart();
  const nav = useNavigate();
  const hasCart = useMemo(() => !!(cart && cart.length), [cart, isLoading]);

  return (
    <section className="cart-page">
      {isLoading ? (
        <Loader />
      ) : (
        <div style={{ width: "100%" }}>
          <h1>Cart</h1>
          <div className={hasCart ? "cart" : ""}>
            {hasCart ? (
              cart.map((el, idx) => <CartItem key={idx} item={el} />)
            ) : (
              <h1>Cart is empty...</h1>
            )}
          </div>
          {hasCart && (
            <div className="go-to-order">
              <button className="btn" onClick={() => nav(PAGES.ORDER)}>
                Go to Checkout
              </button>
            </div>
          )}
        </div>
      )}
    </section>
  );
};
