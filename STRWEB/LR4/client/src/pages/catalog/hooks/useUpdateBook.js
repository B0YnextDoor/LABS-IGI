import { useMutation, useQueryClient } from "@tanstack/react-query";
import { bookService } from "../../../services/book.service";
import { toast } from "sonner";

export const useUpdateBook = (id) => {
  const client = useQueryClient();

  const { mutate, isPending } = useMutation({
    mutationKey: [`update_book_${id || "0"}`],
    mutationFn: (data) => bookService.update(id, data),
    onSuccess() {
      toast.success("Book updated!");
      client.invalidateQueries({ queryKey: [`get_book_${id || "0"}`] });
    },
    onError(e) {
      console.log(e);
      toast.error(e.response.data || "Updating error!");
    },
  });

  return { update: mutate, isUpdating: isPending };
};
