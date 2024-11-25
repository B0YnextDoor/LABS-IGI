import { Link } from "react-router-dom";
import { CONFIG } from "../../../config/config";

export const Form = ({
  register,
  handleSubmit,
  errors,
  onSubmit,
  currentImage,
}) => {
  return (
    <form className="form emp-form" onSubmit={handleSubmit(onSubmit)}>
      <h2>{currentImage ? "Update" : "Add"} employee</h2>
      <div>
        <label>Employee email:</label>
        <input
          type="email"
          {...register("email", { required: "Employee email is required!" })}
        />
      </div>
      {errors?.email?.type === "required" && (
        <span>{errors?.email?.message}</span>
      )}
      <div>
        <label>Employee name:</label>
        <input
          type="text"
          {...register("name", { required: "Employee name is required!" })}
        />
      </div>
      {errors?.name?.type === "required" && (
        <span>{errors?.name?.message}</span>
      )}
      <div>
        <label>Employee phone number:</label>
        <input
          type="text"
          {...register("phone", {
            required: "Employee phone number is required!",
            pattern:
              /^(?:\+375|8)(?:\s*\(?0?(?:25|29|33|44)\)?)(?:\s*|-?)\d{3}(?:\s*|-?)\d{2}(?:\s*|-?)\d{2}$/,
          })}
        />
      </div>
      {errors?.phone?.type === "required" && (
        <span>{errors?.phone?.message}</span>
      )}
      {errors?.phone?.type === "pattern" && <span>Wrong phone pattern!</span>}
      <div>
        <label>Employee image:</label>
        <div className="file-input">
          <input
            type="file"
            accept="image/*"
            {...register("image", {
              required: false,
              validate: {
                fileSize: (value) =>
                  !value[0] ||
                  (value && value[0]?.size < 5000000) ||
                  "File size must be less than 5MB",
                fileType: (value) =>
                  !value[0] ||
                  (value &&
                    ["image/jpeg", "image/png"].includes(value[0]?.type)) ||
                  "Only JPEG/PNG files are allowed",
              },
            })}
          />
          <p>Choose an Image</p>
        </div>
        {currentImage && (
          <Link
            to={`${CONFIG.BASE_URL}/${currentImage}`}
            target="_blank"
            className="animated-link"
            style={{ fontSize: 14, width: "max-content" }}
          >
            *Current Image
          </Link>
        )}
      </div>
      <div>
        <label>Job description</label>
        <textarea
          {...register("description", {
            required: "Job description required!",
          })}
        />
      </div>
      {errors?.description?.type === "required" && (
        <span>{errors?.description?.message}</span>
      )}
      <button className="btn btn-admin" type="submit">
        {currentImage ? "Save" : "Create"}
      </button>
    </form>
  );
};
