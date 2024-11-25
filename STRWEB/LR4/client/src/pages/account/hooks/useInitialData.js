import { useEffect } from "react";
import { useProfile } from "../../../hooks/useProfile";

export const useInitialData = (reset) => {
  const { data, isLoading } = useProfile();

  useEffect(() => {
    if (data)
      reset({
        name: data.name,
        email: data.email,
        phone: data.phone,
        password: "",
      });
  }, [data, isLoading]);

  return { isLoading, role: data?.role };
};
