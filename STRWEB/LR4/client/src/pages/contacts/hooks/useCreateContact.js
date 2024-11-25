import { useMutation, useQueryClient } from "@tanstack/react-query";
import { employeeService } from "../../../services/employee.service";
import { toast } from "sonner";

export const useCreateContact = (cb, reset) => {
  const client = useQueryClient();

  const { mutate, isPending } = useMutation({
    mutationKey: ["create_emp"],
    mutationFn: (data) => employeeService.create(data),
    onSuccess() {
      client.invalidateQueries({ queryKey: ["contacts"] });
      toast.success("New employee created");
      cb(false);
      reset();
    },
    onError(e) {
      console.log(e);
      toast.error(e.response.data || "Creating employee error!");
    },
  });

  return { create: mutate, isCreating: isPending };
};
