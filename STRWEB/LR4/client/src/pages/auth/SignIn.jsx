import { useForm } from "react-hook-form";
import "./Auth.css";
import { FastAuth } from "./FastAuth";
import { useAuth } from "./hooks/useAuth";

export const SignIn = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    mode: "onChange",
  });
  const { mutate, isPending } = useAuth(true);
  const onSubmit = (data) => mutate(data);
  return (
    <div className="auth-container">
      <h1>Sign In</h1>
      <form
        className="form auth-form"
        autoComplete="off"
        onSubmit={handleSubmit(onSubmit)}
      >
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
          <span className="self-start">{errors.email?.message}</span>
        )}
        {errors?.email?.type === "pattern" && (
          <span className="self-start">Wrong email pattern</span>
        )}
        <div>
          <label>Password:</label>
          <input
            type="password"
            placeholder="Enter password..."
            {...register("password", { required: "Password is required!" })}
            style={errors?.password ? { border: "1px solid red" } : {}}
          />
        </div>
        {errors?.password?.type === "required" && (
          <span className="self-start">{errors.password?.message}</span>
        )}
        <button className="btn" disabled={isPending}>
          Sign In
        </button>
      </form>
      <FastAuth disabled={isPending} />
    </div>
  );
};
