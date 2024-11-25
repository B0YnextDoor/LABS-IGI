import { useOrders } from "./hooks/useOrders";
import { Loader } from "../../components/loader/Loader";
import { ListItem } from "./widgets/ListItem";
import "./Orders.css";

export const Orders = () => {
  const { orders, isLoading } = useOrders();
  return (
    <div className="order-page">
      {isLoading ? (
        <Loader />
      ) : orders && orders.length ? (
        <div>
          <h1>Orders</h1>
          <div className="orders-list">
            {orders.map((ord, idx) => (
              <ListItem key={idx} order={ord} idx={idx + 1} />
            ))}
          </div>
        </div>
      ) : (
        <h1>There are no orders yet...</h1>
      )}
    </div>
  );
};
