import { PlusCircle, Trash } from "lucide-react";

export const BookItem = ({ item, idx, add, remove }) => {
  return (
    <div className="order-item list-item">
      <h3>Book #{idx + 1}</h3>
      <h4 className="title">Title: {item.book.title}</h4>
      <h4>
        Author: {item.book.author.surname} {item.book.author.name}
      </h4>
      <h4>Genre: {item.book.genre.name}</h4>
      <h4>Price: {item.book.price} BYN</h4>
      <h4>Amount: {item.amount}</h4>
      <div className="order-item-control">
        <button onClick={() => add(item.book)}>
          <PlusCircle size={20} />
        </button>
        <button onClick={() => remove(item.book._id)}>
          <Trash size={20} />
        </button>
      </div>
    </div>
  );
};
