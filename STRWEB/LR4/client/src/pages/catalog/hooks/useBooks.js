import { useQuery, useQueryClient } from "@tanstack/react-query";
import { useEffect, useState } from "react";
import { useSessionStorage } from "../../../hooks/useSessionStorage.js";
import { bookService } from "../../../services/book.service";
import { CONFIG } from "../../../config/config";

export const useBooks = () => {
  const [page, setPage, loading] = useSessionStorage({
    defaultValue: 1,
    key: CONFIG.CATALOG_PAGE_KEY,
  });
  const [title, setTitle] = useState();
  const [order, setOrder] = useState("amount");

  const client = useQueryClient();
  const { data, isLoading } = useQuery({
    queryKey: ["catalog"],
    queryFn: () => bookService.getAll(title, order, page, loading),
  });

  useEffect(() => {
    if (loading) return;
    client.invalidateQueries({ queryKey: ["catalog"] });
  }, [page, loading, title, order, isLoading]);

  return { books: data, isLoading, page, setPage, title, setTitle, setOrder };
};
