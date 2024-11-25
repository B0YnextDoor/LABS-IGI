import { Pagination } from "../../components/pagination/Pagination";
import { useProfile } from "../../hooks/useProfile";
import { useBooks } from "./hooks/useBooks";
import { Loader } from "../../components/loader/Loader";
import "./Catalog.css";
import { BookCard } from "./widgets/BookCard";
import { useState } from "react";
import { CONFIG } from "../../config/config";
import { useNavigate } from "react-router-dom";
import { PAGES } from "../../config/routes";

export const Catalog = () => {
  const nav = useNavigate();
  const { data } = useProfile();
  const { books, isLoading, page, setPage, setOrder, title, setTitle } =
    useBooks();
  const [search, setSearch] = useState("");
  return (
    <section className="book-page">
      <h1>Book Catalog</h1>
      <section className="search-books">
        <input
          type="text"
          placeholder="Book title"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        <button
          className="btn"
          onClick={() => setTitle(search)}
          disabled={isLoading}
        >
          Search
        </button>
      </section>
      {isLoading ? (
        <Loader />
      ) : books && books.books && books.books.length ? (
        <section id="book-list">
          <section>
            <section id="book-grid">
              {books.books.map((book, idx) => (
                <BookCard key={book._id || idx} book={book} role={data?.role} />
              ))}
            </section>
            <Pagination
              total={books.total}
              current={page}
              setCurrent={setPage}
            />
          </section>
          <section>
            <div>
              <h2>Filter by:</h2>
              <div className="sort_books">
                <button
                  className="btn btn-filter"
                  onClick={() => setOrder("price")}
                >
                  Price
                </button>
                <button
                  className="btn btn-filter"
                  onClick={() => setOrder("amount")}
                >
                  Ammount
                </button>
              </div>
            </div>
            {data?.role === CONFIG.ROLES.ADMIN && (
              <div className="add-book">
                <button
                  className="btn btn-admin"
                  onClick={() => nav(PAGES.BOOK_FORM)}
                >
                  Add Book
                </button>
              </div>
            )}
          </section>
        </section>
      ) : (
        <h1>
          {!title
            ? "Catalog is empty..."
            : `No books with the title '${title}' found...`}
        </h1>
      )}
    </section>
  );
};
