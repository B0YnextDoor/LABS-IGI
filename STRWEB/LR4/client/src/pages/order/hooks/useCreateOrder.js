import { useMutation, useQueryClient } from "@tanstack/react-query";
import { orderService } from "../../../services/order.service";
import { useNavigate } from "react-router-dom";
import { toast } from "sonner";
import { PAGES } from "../../../config/routes";

export const useCreateOrder = () => {
  const client = useQueryClient();
  const nav = useNavigate();
  const { mutate, isPending } = useMutation({
    mutationKey: ["create_order"],
    mutationFn: (data) => orderService.create(data),
    onSuccess() {
      toast.success("Order created");
      client.invalidateQueries({ queryKey: ["user_orders"] });
      nav(PAGES.ACCOUNT);
    },
    onError(e) {
      console.log(e);
      toast.error(e.response.data || "Creating order error!");
    },
  });

  return { create: mutate, isCreating: isPending };
};
