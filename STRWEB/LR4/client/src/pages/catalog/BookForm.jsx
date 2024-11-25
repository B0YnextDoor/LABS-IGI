import { Link } from "react-router-dom";
import { useForm } from "react-hook-form";
import "./Catalog.css";
import { PAGES } from "../../config/routes";
import { useBookAction } from "./hooks/useBookAction";
import { useBookInfo } from "./hooks/useBookInfo";

export const BookForm = () => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm({
    mode: "onChange",
  });

  const { authors, genres } = useBookInfo();

  const { isUpdate, action, isPending } = useBookAction(reset);

  const onSubmit = (data) => action(data);
  return (
    <div className="book_detail_page">
      <h1>{isUpdate ? "Update" : "Add"} Book</h1>
      <div className="back-url">
        <Link to={PAGES.CATALOG} className="animated-link">
          Back to Catalog
        </Link>
      </div>
      <form className="form book-form" onSubmit={handleSubmit(onSubmit)}>
        <div>
          <label>Title:</label>
          <input
            type="text"
            placeholder="Enter book title..."
            {...register("title", { required: "Book title is required!" })}
            style={errors?.title ? { border: "1px solid red" } : {}}
          />
        </div>
        {errors?.title?.type === "required" && (
          <span>{errors?.title.message}</span>
        )}
        <div>
          <label>Author:</label>
          <select
            {...register("author", {
              validate: (x) => (x && x.length) || "Choose the author!",
            })}
          >
            <option value={""}>--- Choose the author ---</option>
            {authors &&
              authors.map((v) => (
                <option key={v._id} value={v._id}>
                  {v.name} {v.surname}
                </option>
              ))}
          </select>
        </div>
        {errors?.author?.type === "validate" && (
          <span>{errors.author.message}</span>
        )}
        <div>
          <label>Genre:</label>
          <select
            {...register("genre", {
              validate: (x) => (x && x.length) || "Choose the genre!",
            })}
          >
            <option value={""}>--- Choose the genre ---</option>
            {genres &&
              genres.map((v) => (
                <option key={v._id} value={v._id}>
                  {v.name}
                </option>
              ))}
          </select>
        </div>
        {errors?.genre?.type === "validate" && (
          <span>{errors.genre.message}</span>
        )}
        <div>
          <label>Price:</label>
          <input
            type="text"
            placeholder="Enter book price..."
            {...register("price", {
              required: "Book price is required!",
              min: 10,
              pattern: /[0-9]*[.,]?[0-9]*/,
            })}
            style={errors?.price ? { border: "1px solid red" } : {}}
          />
        </div>
        {errors?.price?.type === "required" && (
          <span>{errors?.price.message}</span>
        )}
        {errors?.price?.type === "min" && (
          <span>Minimal book price is 10 BYN!</span>
        )}
        {errors?.price?.type === "pattern" && (
          <span>Book price must be a number!</span>
        )}
        <div>
          <label>Amount:</label>
          <input
            type="number"
            placeholder="Enter book amount..."
            {...register("amount", {
              required: "Book amount is required!",
              min: 0,
            })}
            style={errors?.amount ? { border: "1px solid red" } : {}}
          />
        </div>
        {errors?.amount?.type === "required" && (
          <span>{errors?.amount.message}</span>
        )}
        {errors?.amount?.type === "min" && (
          <span>Amount must be a positive number!</span>
        )}
        <button className="btn btn-admin" disabled={isPending}>
          {isUpdate ? "Save" : "Add"}
        </button>
      </form>
    </div>
  );
};
