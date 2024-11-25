import { useQuery } from "@tanstack/react-query";
import { bookService } from "../../../services/book.service";

export const useCatalog = () => {
  const { data, isLoading } = useQuery({
    queryKey: ["get_all_books"],
    queryFn: () => bookService.getCatalog(),
  });

  return { catalog: data, isLoading };
};
