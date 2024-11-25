import { useQuery } from "@tanstack/react-query";
import { userService } from "../services/user.service.js";
import { useEffect, useState } from "react";

export const useProfile = () => {
  const path = window.location.pathname;
  const { data, isLoading, isSuccess } = useQuery({
    queryKey: ["profile"],
    queryFn: () => userService.profile(path),
    retry: 1,
  });

  const [profile, setProfile] = useState(data);

  useEffect(() => {
    if (data && isSuccess) setProfile(data);
    else setProfile(null);
  }, [path, data, isSuccess, isLoading]);

  return { data: profile, isLoading };
};
