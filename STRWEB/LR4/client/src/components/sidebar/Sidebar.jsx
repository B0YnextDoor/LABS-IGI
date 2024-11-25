import { Link } from "react-router-dom";
import { MENU } from "./sidebar.data";
import { MenuItem } from "./MenuItem";
import "./Sidebar.css";

export const Sidebar = () => {
  return (
    <nav className="router">
      <section>
        <Link to="/">
          <img src="/about/logo.jpg" width="100" height="100" alt="BOOKY" />
        </Link>
      </section>
      {MENU.map((item, idx) => (
        <MenuItem key={idx} item={item} />
      ))}
    </nav>
  );
};
