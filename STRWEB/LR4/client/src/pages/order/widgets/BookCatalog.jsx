import { PlusCircle } from "lucide-react";
import { Loader } from "../../../components/loader/Loader";

export const BookCatalog = ({ catalog, isLoading, add }) => {
  if (isLoading) return <Loader />;
  return catalog && catalog.length ? (
    <div className="order-books">
      {catalog.map((book, idx) => (
        <div key={idx} className="order-item list-item">
          <h3 className="title">{book.title}</h3>
          <h4>
            Author: {book.author.surname} {book.author.name}
          </h4>
          <h4>Genre: {book.genre.name}</h4>
          <h4>Amount: {book.amount}</h4>
          <h4>Price: {book.price} BYN</h4>
          <div className="order-item-control">
            <button onClick={() => add(book)}>
              <PlusCircle size={20} />
            </button>
          </div>
        </div>
      ))}
    </div>
  ) : (
    <h1>Catalog is empty...</h1>
  );
};
