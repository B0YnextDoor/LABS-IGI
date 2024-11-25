import { Link } from "react-router-dom";
import { statusColors, statusText } from "../../../utils/order";
import { PAGES } from "../../../config/routes";

export const ListItem = ({ item, idx }) => {
  return (
    <div className="list-item">
      <Link to={`${PAGES.ORDER}/${item._id}`}>Order #{idx + 1}</Link>
      <p>Order date: {new Date(item.created_at).toLocaleDateString()}</p>
      <p>
        Delivery date: {new Date(item.orderInfo.deliveryDate).toLocaleString()}
      </p>
      <p>Delivery address: {item.orderInfo.deliveryAddress}</p>
      <p>Order price: {item.orderInfo.totalPrice["$numberDecimal"]} BYN</p>
      <p
        style={{ color: statusColors[item.orderInfo.status - 1] }}
        className="status"
      >
        Status: {statusText[item.orderInfo.status - 1]}
      </p>
    </div>
  );
};
