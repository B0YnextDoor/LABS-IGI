import { validateDate, countPrice } from "../../../utils/order";

export const OrderForm = ({
  register,
  handleSubmit,
  errors,
  onSubmit,
  isPending,
  type,
  items,
}) => {
  return (
    <form
      className={`form ${!type ? "create" : "update"}-order-form`}
      onSubmit={handleSubmit(onSubmit)}
    >
      <div>
        <label>Delivery date:</label>
        <input
          type="datetime-local"
          placeholder="Enter delivery date..."
          {...register("deliveryDate", {
            required: "Delivery date is required",
            validate: (date) => validateDate(date),
          })}
        />
      </div>
      {errors?.deliveryDate?.type === "required" && (
        <span>{errors?.deliveryDate.message}</span>
      )}
      {errors?.deliveryDate?.type === "validate" && (
        <span>{errors?.deliveryDate.message}</span>
      )}
      <div>
        <label>Delivery address:</label>
        <input
          type="text"
          placeholder="Enter delivery address..."
          {...register("deliveryAddress", {
            required: "Delivery address is required",
            pattern: /^[A-Za-z]+[,]\s.+\s\d+.*$/,
          })}
        />
      </div>
      {errors?.deliveryDate?.type === "required" && (
        <span>{errors?.deliveryDate.message}</span>
      )}
      {errors?.deliveryDate?.type === "pattern" && (
        <span>
          Wrong address! Address must be in the format: [city], [street] [house
          number] [other info]
        </span>
      )}
      <h2 className="order-price">Order: price {countPrice(items)} BYN</h2>
      <button className="btn" type="submit" disabled={isPending}>
        {!type ? "Create" : "Update"} Order
      </button>
    </form>
  );
};
