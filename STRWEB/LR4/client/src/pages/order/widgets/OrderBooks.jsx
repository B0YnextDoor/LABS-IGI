import { BookItem } from "./BookItem";

export const OrderBooks = ({ items, add, remove }) => {
  return items && items.length ? (
    <div className="order-books">
      {items.map((item, idx) => (
        <BookItem
          key={`${item._id}_${item.amount}`}
          item={item}
          idx={idx}
          add={add}
          remove={remove}
        />
      ))}
    </div>
  ) : (
    <h1>No books in the order...</h1>
  );
};
