import { useMutation, useQueryClient } from "@tanstack/react-query";
import { cartService } from "../../../services/cart.service";
import { toast } from "sonner";

export const useRemoveFromCart = (id) => {
  const client = useQueryClient();

  const { mutate, isPending } = useMutation({
    mutationKey: [`del_from_cart_${id || ""}`],
    mutationFn: () => cartService.delete(id),
    onSuccess() {
      toast.info("Book removed from cart");
      client.invalidateQueries({ queryKey: ["cart"] });
    },
    onError(e) {
      console.log(e);
      toast.error(e.response.data || "Removing book error!");
    },
  });

  return { remove: mutate, isRemoving: isPending };
};
