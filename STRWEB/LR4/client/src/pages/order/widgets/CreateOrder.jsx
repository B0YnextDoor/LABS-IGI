import "../Orders.css";
import { CartBooks } from "./CartBooks";
import { useCreateOrder } from "../hooks/useCreateOrder";
import { Link } from "react-router-dom";
import { PAGES } from "../../../config/routes";
import { useCart } from "../../../hooks/cart/useCart";
import { OrderForm } from "./OrderForm";
import { useForm } from "react-hook-form";
import { CONFIG } from "../../../config/config";
import { getDefaultDate } from "../../../utils/order";

export const CreateOrder = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    mode: "onChange",
    defaultValues: {
      deliveryDate: getDefaultDate(),
      deliveryAddress: CONFIG.DEFAULT_ADDRESS,
    },
  });

  const { create, isCreating } = useCreateOrder();
  const { cart } = useCart();
  const onSubmit = (data) => create(data);

  return (
    <div className="order-page">
      <div className="back-to-cart">
        <Link to={PAGES.CART} className="animated-link">
          Back to cart
        </Link>
      </div>
      <div className="create-order-content">
        <h1>Create order</h1>
        <h2 style={{ marginBlock: "2%" }}>Order Items</h2>
        <CartBooks cart={cart} />
        <OrderForm
          register={register}
          handleSubmit={handleSubmit}
          errors={errors}
          onSubmit={onSubmit}
          isPending={isCreating}
          items={cart}
        />
      </div>
    </div>
  );
};
