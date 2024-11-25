import { statusColors, statusText } from "../../../utils/order";

export const OrderInfo = ({ order }) => {
  return (
    order && (
      <div className="order-item list-item">
        <h3>Order info</h3>
        <h4>Order date: {new Date(order.created_at).toLocaleDateString()}</h4>
        <h4>
          Delivery date:{" "}
          {new Date(order.orderInfo.deliveryDate).toLocaleString()}
        </h4>
        <h4>Delivery address: {order.orderInfo.deliveryAddress}</h4>
        <h4>Total price: {order.orderInfo.totalPrice["$numberDecimal"]} BYN</h4>
        <span style={{ color: statusColors[order.orderInfo.status - 1] }}>
          Status: {statusText[order.orderInfo.status - 1]}
        </span>
      </div>
    )
  );
};
