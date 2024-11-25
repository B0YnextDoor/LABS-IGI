import { Link } from "react-router-dom";

export const MenuItem = ({ item }) => {
  return (
    <div>
      <Link to={item.link} className="menu-link">
        <item.icon />
        <span>{item.name}</span>
      </Link>
    </div>
  );
};
