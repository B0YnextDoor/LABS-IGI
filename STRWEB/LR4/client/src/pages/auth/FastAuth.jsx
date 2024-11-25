import { useFastAuth } from "./hooks/useFastAuth";

export const FastAuth = ({ disabled }) => {
  const auth = useFastAuth();
  return (
    <div className="auth-account">
      <button onClick={() => auth(true)} disabled={disabled}>
        <img src="images/google-auth.svg" alt="auth with google" />
        <p>Google</p>
      </button>
      <button onClick={() => auth()} disabled={disabled}>
        <img src="images/facebook-auth.svg" alt="auth with facebook" />
        <p>Facebook</p>
      </button>
    </div>
  );
};
