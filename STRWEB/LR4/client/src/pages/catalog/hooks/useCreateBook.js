import { useMutation, useQueryClient } from "@tanstack/react-query";
import { bookService } from "../../../services/book.service";
import { useNavigate } from "react-router-dom";
import { toast } from "sonner";
import { PAGES } from "../../../config/routes";

export const useCreateBook = () => {
  const nav = useNavigate();
  const client = useQueryClient();
  const { mutate, isPending } = useMutation({
    mutationKey: ["create_book"],
    mutationFn: (data) => bookService.create(data),
    onSuccess() {
      toast.success("Book added");
      client.invalidateQueries({ queryKey: ["catalog"] });
      nav(PAGES.CATALOG);
    },
    onError(e) {
      console.log(e);
      toast.error(e.response.data || "Creating error!");
    },
  });

  return { create: mutate, isCreating: isPending };
};
