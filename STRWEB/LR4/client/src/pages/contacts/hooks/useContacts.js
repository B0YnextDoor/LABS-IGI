import { CONFIG } from "../../../config/config";
import { useSessionStorage } from "../../../hooks/useSessionStorage.js";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { useState, useEffect } from "react";
import { employeeService } from "../../../services/employee.service.js";

export const useContacts = () => {
  const [page, setPage, loading] = useSessionStorage({
    defaultValue: 1,
    key: CONFIG.CONTACTS_PAGE_KEY,
  });
  const [filter, setFilter] = useState("");
  const [order, setOrder] = useState("name");
  const [isDeleting, setIsDeleting] = useState(false);

  const client = useQueryClient();
  const { data, isLoading } = useQuery({
    queryKey: ["contacts"],
    queryFn: () => employeeService.getAll(filter, order, page, loading),
  });

  useEffect(() => {
    if (isDeleting) {
      setIsDeleting(false);
      setPage(1);
      setFilter("");
      setOrder("name");
    } else client.invalidateQueries({ queryKey: ["contacts"] });
  }, [page, loading, filter, order, isDeleting, isLoading]);

  return {
    contacts: data,
    isLoading,
    page,
    setPage,
    filter,
    setFilter,
    order,
    setOrder,
    setIsDeleting,
  };
};
