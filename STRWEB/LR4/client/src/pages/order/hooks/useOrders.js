import { useQuery } from "@tanstack/react-query";
import { orderService } from "../../../services/order.service";

export const useOrders = () => {
  const { data, isLoading } = useQuery({
    queryKey: ["all_orders"],
    queryFn: () => orderService.getAll(),
  });

  return { orders: data, isLoading };
};
