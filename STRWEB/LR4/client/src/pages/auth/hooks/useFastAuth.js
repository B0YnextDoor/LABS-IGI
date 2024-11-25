import { authService } from "../../../services/auth.service";
import { CONFIG } from "../../../config/config";

export const useFastAuth = () => {
  const handleLogin = (type) => {
    window.open(
      `${CONFIG.BASE_URL}${authService.BASE_URL}${
        type ? "google" : "facebook"
      }`,
      "_self"
    );
  };

  return handleLogin;
};
