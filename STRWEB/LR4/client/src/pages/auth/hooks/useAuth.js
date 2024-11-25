import { useMutation, useQueryClient } from "@tanstack/react-query";
import { authService } from "../../../services/auth.service";
import { toast } from "sonner";
import { useNavigate } from "react-router-dom";
import { PAGES } from "../../../config/routes";

export const useAuth = (type) => {
  const nav = useNavigate();
  const client = useQueryClient();
  const { mutate, isPending } = useMutation({
    mutationKey: ["auth"],
    mutationFn: (data) => authService.auth(data, type),
    onSuccess() {
      toast.success("Successfully log in!");
      nav(PAGES.HOME);
      client.invalidateQueries({ queryKey: ["profile"] });
    },
    onError(e) {
      console.log(e);
      toast.error(e.response.data.message);
    },
  });

  return { mutate, isPending };
};
