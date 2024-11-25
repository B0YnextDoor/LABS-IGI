import { useParams } from "react-router-dom";
import { UpdateOrder } from "./widgets/UpdateOrder";
import { CreateOrder } from "./widgets/CreateOrder";
import "./Orders.css";

export const Order = () => {
  const { id } = useParams();

  return id ? <UpdateOrder id={id} /> : <CreateOrder />;
};
