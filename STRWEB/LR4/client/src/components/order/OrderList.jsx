import { useUserOrders } from "./hooks/useUserOrders";
import { Loader } from "../loader/Loader";
import { ListItem } from "./widgets/ListItem";
import "./OrderList.css";

export const OrderList = () => {
  const { orders, isLoading } = useUserOrders();

  return (
    <section className="order-list-cont">
      <h1>Orders</h1>
      {isLoading ? (
        <Loader />
      ) : orders && orders.length ? (
        <div className="order-list">
          {orders.map((v, idx) => (
            <ListItem key={idx} item={v} idx={idx} />
          ))}
        </div>
      ) : (
        <h1>You have no orders yet...</h1>
      )}
    </section>
  );
};
