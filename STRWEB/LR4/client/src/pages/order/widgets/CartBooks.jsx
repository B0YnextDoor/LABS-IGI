import "../Orders.css";

export const CartBooks = ({ cart }) => {
  return (
    <div className="order-items">
      {cart && cart.length ? (
        cart.map((item, idx) => (
          <div key={idx} className="order-item">
            <h3 style={{ maxWidth: "95%" }}>{item.book.title}</h3>
            <h4>
              Author: {item.book.author.surname} {item.book.author.name}
            </h4>
            <h4>Genre: {item.book.genre.name}</h4>
            <h4>Amount: {item.amount}</h4>
            <h3>Price: {item.book.price} BYN</h3>
          </div>
        ))
      ) : (
        <h1>No books in the order...</h1>
      )}
    </div>
  );
};
