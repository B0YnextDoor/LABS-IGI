import { useForm } from "react-hook-form";
import { useNewsAction } from "./hooks/useNewsAction";
import { Link } from "react-router-dom";
import { PAGES } from "../../config/routes";
import { CONFIG } from "../../config/config";

export const NewsForm = () => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm({
    mode: "onChange",
  });
  const { isUpdate, action, isPending, defaultFile } = useNewsAction(reset);
  const onSubmit = (data) => {
    const { title, text, image } = data;
    const formData = new FormData();
    formData.append("title", title);
    formData.append("text", text);
    formData.append("image", image[0]);
    action(formData);
  };
  return (
    <div className="news-page news-form-page">
      <h1>{isUpdate ? "Update" : "Create"} news</h1>
      <div className="ret-to-news">
        <Link to={PAGES.NEWS} className="animated-link">
          Back to News
        </Link>
      </div>
      <form className="form news-form" onSubmit={handleSubmit(onSubmit)}>
        <div>
          <label>News title:</label>
          <input
            type="text"
            {...register("title", { required: "News title is required!" })}
          />
        </div>
        {errors?.title?.type === "required" && (
          <span>{errors?.title?.message}</span>
        )}
        <div>
          <label>News text:</label>
          <textarea
            {...register("text", { required: "News text is required!" })}
          />
        </div>
        {errors?.text?.type === "required" && (
          <span>{errors?.title?.message}</span>
        )}
        <div>
          <label>News image:</label>
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
          {defaultFile && (
            <Link
              to={`${CONFIG.BASE_URL}/${defaultFile}`}
              target="_blank"
              className="animated-link"
              style={{ fontSize: 14, width: "max-content" }}
            >
              *Current image
            </Link>
          )}
        </div>
        {errors?.image && <span>{errors?.image?.message}</span>}
        <button className="btn btn-admin" type="submit" disabled={isPending}>
          {isUpdate ? "Save" : "Create"}
        </button>
      </form>
    </div>
  );
};

{
  /* <input
type="file"
id="file"
{...register("file", {
  required: "File is required", // Обязательное поле
  validate: {
    // Кастомная валидация размера файла
    fileSize: (value) =>
      value && value[0]?.size < 5000000 || "File size must be less than 5MB",
    // Кастомная валидация типа файла
    fileType: (value) =>
      value && ["image/jpeg", "image/png"].includes(value[0]?.type) ||
      "Only JPEG/PNG files are allowed",
  },
})}
/>
{errors.file && <p>{errors.file.message}</p>} */
}
