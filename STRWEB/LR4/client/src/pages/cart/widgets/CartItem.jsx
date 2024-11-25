import { PlusCircle, Trash } from "lucide-react";
import { useAddToCart } from "../../../hooks/cart/useAddToCart";
import { useRemoveFromCart } from "../hooks/useRemoveFromCart";

export const CartItem = ({ item }) => {
  const { add, isAdding } = useAddToCart(item.book._id);
  const { remove, isRemoving } = useRemoveFromCart(item.book._id);
  return (
    <div className="cart-item">
      <div>
        <h3 className="title">{item.book.title}</h3>
        <h4>
          Author: {item.book.author.surname} {item.book.author.name}
        </h4>
        <h4>Genre: {item.book.genre.name}</h4>
        <h4>Amount: {item.amount}</h4>
        <h3>Price: {item.book.price} BYN</h3>
      </div>
      <div className="item-control">
        <button disabled={isAdding || isRemoving} onClick={() => add()}>
          <PlusCircle size={20} />
        </button>
        <button disabled={isAdding || isRemoving} onClick={() => remove()}>
          <Trash size={20} />
        </button>
      </div>
    </div>
  );
};
