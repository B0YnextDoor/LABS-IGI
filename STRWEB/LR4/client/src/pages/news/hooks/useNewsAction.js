import { useParams } from "react-router-dom";
import { useCreateNews } from "./useCreateNews";
import { useUpdateNews } from "./useUpdateNews";
import { useNewsDetail } from "./useNewsDetail";
import { useEffect, useState } from "react";

export const useNewsAction = (reset) => {
  const { id } = useParams();
  const { create, isCreating } = useCreateNews();
  const { update, isUpdating } = useUpdateNews(id);
  const { news } = useNewsDetail(id);

  const [data, setData] = useState({
    action: create,
    isPending: isCreating,
  });
  const [defaultFile, setFile] = useState("");

  useEffect(() => {
    if (id && news) {
      setData({ isUpdate: true, action: update, isPending: isUpdating });
      reset({
        title: news.title,
        text: news.text,
      });
      setFile(news.imagePath);
    }
  }, [id, news]);

  return { ...data, defaultFile };
};
