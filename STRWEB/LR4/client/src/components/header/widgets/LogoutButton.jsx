import { LogOut } from "lucide-react";
import styles from "./Logout.module.css";
import { useNavigate } from "react-router-dom";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { authService } from "../../../services/auth.service.js";
import { PAGES } from "../../../config/routes.js";

export const LogoutButton = () => {
  const navigate = useNavigate();
  const client = useQueryClient();
  const { mutate } = useMutation({
    mutationKey: ["logout"],
    mutationFn: () => authService.logOut(),
    onSuccess: () => {
      navigate(PAGES.HOME);
      client.invalidateQueries({ queryKey: ["profile"] });
    },
  });
  return (
    <div className={styles.logout}>
      <button onClick={() => mutate()}>
        <LogOut size={25} />
      </button>
    </div>
  );
};
