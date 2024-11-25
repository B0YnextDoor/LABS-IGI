import { useMutation, useQueryClient } from "@tanstack/react-query";
import { orderService } from "../../../services/order.service";
import { toast } from "sonner";

export const useUpdateOrder = (id, isStatus = false) => {
  const client = useQueryClient();
  const { mutate, isPending } = useMutation({
    mutationKey: [`update_order_${id || "0"}`],
    mutationFn: (data) => orderService.update(id, data),
    onSuccess() {
      toast.success("Order updated");
      client.invalidateQueries({ queryKey: [`order_${id || "0"}`] });
      if (isStatus) client.invalidateQueries({ queryKey: ["all_orders"] });
    },
    onError(e) {
      console.log(e);
      toast.error(e.response.data || "Updating order error!");
    },
  });

  return { update: mutate, isUpdating: isPending };
};
