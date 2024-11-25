import { useQuery } from "@tanstack/react-query";
import { userService } from "../../../services/user.service";

export const useUserOrders = () => {
  const { data, isLoading } = useQuery({
    queryKey: ["user_orders"],
    queryFn: () => userService.orders(),
  });

  return { orders: data, isLoading };
};
