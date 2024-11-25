import { useMutation, useQueryClient } from "@tanstack/react-query";
import { employeeService } from "../../../services/employee.service";
import { toast } from "sonner";

export const useUpdateContact = (id) => {
  const client = useQueryClient();

  const { mutate, isPending } = useMutation({
    mutationKey: [`upd_emp_${id || "0"}`],
    mutationFn: (data) => employeeService.update(id, data),
    onSuccess() {
      client.invalidateQueries({ queryKey: [`contact_${id || "0"}`] });
      toast.success("Employee updated");
    },
    onError(e) {
      console.log(e);
      toast.error(e.response.data || "Updating employee error!");
    },
  });

  return { update: mutate, isUpdating: isPending };
};
