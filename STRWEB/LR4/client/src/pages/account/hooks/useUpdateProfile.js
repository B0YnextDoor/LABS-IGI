import { useMutation, useQueryClient } from "@tanstack/react-query";
import { userService } from "../../../services/user.service.js";
import { toast } from "sonner";

export const useUpdateProfile = () => {
  const client = useQueryClient();
  const { mutate, isPending } = useMutation({
    mutationKey: ["update_profile"],
    mutationFn: (data) => userService.update(data),
    onSuccess() {
      client.invalidateQueries({ queryKey: ["profile"] });
      toast.success("Profile updated");
    },
    onError(e) {
      console.log(e);
      toast.error(e.response.data);
    },
  });

  return { update: mutate, isPending };
};
