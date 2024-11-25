import { useQuery } from "@tanstack/react-query";
import { cartService } from "../../services/cart.service";

export const useCart = () => {
  const { data, isLoading } = useQuery({
    queryKey: ["cart"],
    queryFn: () => cartService.get(),
  });

  return { cart: data, isLoading };
};
