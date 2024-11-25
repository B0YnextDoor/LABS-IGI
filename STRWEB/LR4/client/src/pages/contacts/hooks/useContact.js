import { useQuery } from "@tanstack/react-query";
import { employeeService } from "../../../services/employee.service";
import { useEffect, useState } from "react";
import { useUpdateContact } from "./useUpdateContact";

export const useContact = (id, reset) => {
  const { data } = useQuery({
    queryKey: [`contact_${id || "0"}`],
    queryFn: () => employeeService.getById(id),
  });

  const [currentFile, setFile] = useState("");
  const { update, isUpdating } = useUpdateContact(id);

  useEffect(() => {
    if (id && data) {
      reset({
        email: data.email,
        name: data.info.name,
        phone: data.info.phone,
        description: data.info.description,
      });
      setFile(data.info.imagePath);
    }
  }, [id, data]);

  return { currentFile, update, isUpdating };
};
