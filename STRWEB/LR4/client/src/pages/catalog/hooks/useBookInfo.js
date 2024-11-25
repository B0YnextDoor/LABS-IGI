import { useQuery } from "@tanstack/react-query";
import { bookService } from "../../../services/book.service";

export const useBookInfo = () => {
  const { data: authors } = useQuery({
    queryKey: ["authors"],
    queryFn: () => bookService.getAuthors(),
  });

  const { data: genres } = useQuery({
    queryKey: ["genres"],
    queryFn: () => bookService.getGenres(),
  });

  return { authors, genres };
};
