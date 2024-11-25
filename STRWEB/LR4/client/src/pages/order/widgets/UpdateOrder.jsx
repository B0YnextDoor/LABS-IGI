import { useOrderAction } from "../hooks/useOrderAction";
import { BookCatalog } from "./BookCatalog";
import { OrderBooks } from "./OrderBooks";
import { useForm } from "react-hook-form";
import { CONFIG } from "../../../config/config";
import { OrderForm } from "./OrderForm";
import { OrderInfo } from "./OrderInfo";
import { useUpdateOrder } from "../hooks/useUpdateOrder";
import { getBookIds } from "../../../utils/order";

export const UpdateOrder = ({ id }) => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm({
    mode: "onChange",
  });

  const { update, isUpdating } = useUpdateOrder(id);
  const { items, catalog, isLoading, orderInfo, addBook, removeBook } =
    useOrderAction(id, reset);

  const onSubmit = (data) =>
    update({
      ...data,
      status: CONFIG.ORDER_STATUS.PENDING,
      book_ids: getBookIds(items),
    });
  return (
    <div className="order-page update-order-page">
      <div>
        <h1>Order Info</h1>
        <OrderBooks items={items} add={addBook} remove={removeBook} />
        {orderInfo?.orderInfo?.status === CONFIG.ORDER_STATUS.PENDING ? (
          <div>
            <h2>Order is pending the delivery...</h2>
            <OrderForm
              register={register}
              handleSubmit={handleSubmit}
              errors={errors}
              onSubmit={onSubmit}
              isPending={isUpdating}
              items={items}
              type
            />
          </div>
        ) : (
          <OrderInfo order={orderInfo} />
        )}
      </div>
      <div>
        <h1>Catalog</h1>
        <BookCatalog catalog={catalog} isLoading={isLoading} add={addBook} />
      </div>
    </div>
  );
};
