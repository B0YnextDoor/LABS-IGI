import { useParams } from "react-router-dom";
import { useSessionStorage } from "../../../hooks/useSessionStorage";
import { CONFIG } from "../../../config/config";
import { useCreateBook } from "./useCreateBook";
import { useUpdateBook } from "./useUpdateBook";
import { useEffect, useState } from "react";
import { useBook } from "./useBook";

export const useBookAction = (reset) => {
  const { upd } = useParams();
  const [id, _, __] = useSessionStorage({
    defaultValue: "",
    key: CONFIG.BOOK_KEY,
  });
  const { create, isCreating } = useCreateBook();
  const { update, isUpdating } = useUpdateBook(id);
  const { book } = useBook(id, !!!upd);

  const [data, setData] = useState({
    action: create,
    isPending: isCreating,
  });

  useEffect(() => {
    if (id && book && upd) {
      setData({ isUpdate: true, action: update, isPending: isUpdating });
      reset({
        _id: book._id,
        title: book.title,
        price: book.price,
        amount: book.amount,
        genre: book.genre._id,
        author: book.author._id,
      });
    }
  }, [upd, id, book]);

  return { ...data };
};
