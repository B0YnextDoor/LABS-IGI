import { useMutation } from "@tanstack/react-query";
import { employeeService } from "../../../services/employee.service";
import { toast } from "sonner";

export const useDeleteContact = (setIsDeleting) => {
  const { mutate, isPending } = useMutation({
    mutationKey: [`delete_emp`],
    mutationFn: (id) => employeeService.delete(id),
    onSuccess() {
      setIsDeleting(true);
      toast.info("Employee deleted");
    },
    onError(e) {
      console.log(e);
      toast.error(e.response.data || "Deleting employee error!");
    },
  });

  return { deleteEmp: mutate, isDeleting: isPending };
};
