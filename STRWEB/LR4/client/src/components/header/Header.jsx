import { Link } from "react-router-dom";
import "./Header.css";
import { useProfile } from "../../hooks/useProfile.js";
import { CONFIG } from "../../config/config.js";
import { PAGES } from "../../config/routes.js";
import { LogoutButton } from "./widgets/LogoutButton.jsx";
import { ShoppingCart } from "lucide-react";

export const Header = () => {
  const { data } = useProfile();
  return (
    <header>
      {!data ? (
        <nav>
          <Link to="/sign-in" className="animated-link">
            Sign In
          </Link>
          <Link to="/sign-up" className="animated-link">
            Sign Up
          </Link>
        </nav>
      ) : (
        <nav>
          {data.role == CONFIG.ROLES.CUSTOMER ? (
            <Link to={PAGES.CART} className="cart-link">
              <ShoppingCart size={20} className="cart-icon" />
              Cart
            </Link>
          ) : (
            <Link to={PAGES.ORDERS} className="animated-link">
              Orders
            </Link>
          )}
          <Link to={PAGES.ACCOUNT} className="animated-link">
            Account
          </Link>
          <LogoutButton />
        </nav>
      )}
    </header>
  );
};
