import { useQuery } from "@tanstack/react-query";
import { bookService } from "../../../services/book.service";
import { useEffect, useState } from "react";
import { CONFIG } from "../../../config/config";
import { useSessionStorage } from "../../../hooks/useSessionStorage";

export const useBook = (id, clear = true) => {
  const [_, setValue, __] = useSessionStorage({
    defaultValue: id,
    key: CONFIG.BOOK_KEY,
    clear: clear,
  });

  const { data, isLoading, isSuccess } = useQuery({
    queryKey: [`get-book_${id || "0"}`],
    queryFn: () => bookService.getById(id),
    retry: 0,
  });

  const [book, setBook] = useState(data);

  useEffect(() => {
    if (id && data && isSuccess) {
      setBook(data);
      setValue(id);
    } else setBook(null);
  }, [id, data, isLoading, isSuccess]);

  return { book, isLoading };
};
