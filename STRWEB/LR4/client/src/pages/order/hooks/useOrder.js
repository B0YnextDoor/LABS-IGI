import { useQuery } from "@tanstack/react-query";
import { orderService } from "../../../services/order.service";

export const useOrder = (id) => {
  const { data, isLoading } = useQuery({
    queryKey: [`order_${id || "0"}`],
    queryFn: () => orderService.getById(id),
  });

  return { order: data, isLoading };
};
