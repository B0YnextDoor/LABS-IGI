import { useForm } from "react-hook-form";
import "./Auth.css";
import { FastAuth } from "./FastAuth";
import { useAuth } from "./hooks/useAuth";

export const SignUp = () => {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm({
    mode: "onChange",
  });
  const { mutate, isPending } = useAuth();
  const onSubmit = (data) => mutate(data);

  return (
    <div className="auth-container">
      <h1>Sign Up</h1>
      <form
        className="form auth-form"
        autoComplete="off"
        onSubmit={handleSubmit(onSubmit)}
      >
        <div>
          <label>Name: </label>
          <input
            type="text"
            placeholder="Enter name..."
            {...register("name", {
              required: "Name is required!",
            })}
            style={errors?.name ? { border: "1px solid red" } : {}}
          />
        </div>
        {errors?.name?.type === "required" && (
          <span>{errors.name?.message}</span>
        )}
        <div>
          <label>Email:</label>
          <input
            type="email"
            placeholder="Enter email..."
            {...register("email", {
              required: "Email is required!",
              pattern: /\S+@\S+\.\S+/,
            })}
            style={errors?.email ? { border: "1px solid red" } : {}}
          />
        </div>
        {errors?.email?.type === "required" && (
          <span>{errors.email?.message}</span>
        )}
        {errors?.email?.type === "pattern" && <span>Wrong email pattern!</span>}
        <div>
          <label>Phone:</label>
          <input
            type="text"
            placeholder="Enter phone..."
            {...register("phone", {
              required: "Phone is required!",
              pattern:
                /^(?:\+375|8)(?:\s*\(?0?(?:25|29|33|44)\)?)(?:\s*|-?)\d{3}(?:\s*|-?)\d{2}(?:\s*|-?)\d{2}$/,
            })}
            style={errors?.phone ? { border: "1px solid red" } : {}}
          />
        </div>
        {errors?.phone?.type === "required" && (
          <span>{errors.phone?.message}</span>
        )}
        {errors?.phone?.type === "pattern" && <span>Wrong phone pattern!</span>}
        <div>
          <label>Password</label>
          <input
            type="password"
            placeholder="Enter password..."
            {...register("password", {
              required: "Password is required!",
              minLength: 8,
              pattern: /^(?=.*[A-Z])(?=.*\d).+$/,
            })}
            style={errors?.password ? { border: "1px solid red" } : {}}
          />
        </div>
        {errors?.password?.type === "required" && (
          <span>{errors.password?.message}</span>
        )}
        {errors?.password?.type === "minLength" && (
          <span>Min password length is 8!</span>
        )}
        {errors?.password?.type === "pattern" && (
          <div className="pswd">
            {!/\d/.test(watch("password")) && (
              <span>Password must contain at least 1 digit!</span>
            )}
            {!/[A-Z]/.test(watch("password")) && (
              <span>Password must contain at least 1 capital letter!</span>
            )}
          </div>
        )}
        <button className="btn" disabled={isPending}>
          Sign In
        </button>
      </form>
      <FastAuth disabled={isPending} />
    </div>
  );
};
