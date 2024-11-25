import { useMutation, useQueryClient } from "@tanstack/react-query";
import { bookService } from "../../../services/book.service";
import { toast } from "sonner";
import { PAGES } from "../../../config/routes";

export const useDeleteBook = (id, nav) => {
  const client = useQueryClient();

  const { mutate, isPending } = useMutation({
    mutationKey: [`delete_book_${id}`],
    mutationFn: () => bookService.delete(id),
    onSuccess() {
      toast.info("Book deleted");
      client.invalidateQueries({ queryKey: ["catalog"] });
      nav(PAGES.CATALOG);
    },
    onError(e) {
      console.log(e);
      toast.error(e.response.data || "Deleting error");
    },
  });

  return { mutate, isDeleting: isPending };
};
