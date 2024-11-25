import { useMutation, useQueryClient } from "@tanstack/react-query";
import { cartService } from "../../services/cart.service";
import { toast } from "sonner";

export const useAddToCart = (id) => {
  const client = useQueryClient();
  const { mutate, isPending } = useMutation({
    mutationKey: [`add_to_cart_${id || ""}`],
    mutationFn: () => cartService.add(id),
    onSuccess() {
      toast.success("Book is added to cart");
      client.invalidateQueries({ queryKey: ["cart"] });
    },
    onError(e) {
      console.log(e);
      toast.error(e.response.data || "Adding book error!");
    },
  });

  return { add: mutate, isAdding: isPending };
};
