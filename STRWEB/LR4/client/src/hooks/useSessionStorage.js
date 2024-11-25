import { useEffect, useRef, useState } from "react";

export function useSessionStorage({ defaultValue, key, clear }) {
  const [isLoading, setIsLoading] = useState(true);
  const isMounted = useRef(false);
  const [value, setValue] = useState(defaultValue);

  useEffect(() => {
    try {
      const item = sessionStorage.getItem(key);
      if (item && !clear) {
        setValue(JSON.parse(item));
      }
    } catch (e) {
      console.log(e);
    } finally {
      setIsLoading(false);
    }
    return () => {
      isMounted.current = false;
    };
  }, [key]);

  useEffect(() => {
    if (isMounted.current || clear) {
      sessionStorage.setItem(key, JSON.stringify(value));
    } else {
      isMounted.current = true;
    }
  }, [key, value, isLoading]);

  return [value, setValue, isLoading];
}
