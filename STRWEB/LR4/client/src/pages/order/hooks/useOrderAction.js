import { toast } from "sonner";
import { addToOrder, getBookIds, removeFromOrder } from "../../../utils/order";
import { useOrder } from "./useOrder";
import { useEffect, useState } from "react";
import { useCatalog } from "./useCatalog";
import { CONFIG } from "../../../config/config";

export const useOrderAction = (id, reset) => {
  const { order } = useOrder(id);
  const { catalog, isLoading } = useCatalog();
  const [items, setItems] = useState([]);
  const [orderInfo, setInfo] = useState(order);

  const addBook = (book) => {
    const orderBooks = getBookIds(items);
    let isError = true;
    if (orderBooks.includes(book._id)) {
      const orderItems = addToOrder(items, book._id, book.amount);
      if (orderItems) {
        setItems([...orderItems]);
        isError = false;
      }
    } else if (book.amount > 0) {
      setItems((prev) => [...prev, { amount: 1, book: book }]);
      isError = false;
    }
    if (isError) toast.error("Not enough books in the catalog!");
    else toast.success("Book is added to the order.");
  };

  const removeBook = (book_id) => {
    setItems((prev) => removeFromOrder(prev, book_id));
    toast.info("Book is removed from the order.");
  };

  useEffect(() => {
    if (id && order && order.books) {
      const date = new Date(order.orderInfo.deliveryDate);
      date.setHours(date.getHours() + CONFIG.GMT);
      reset({
        deliveryDate: date.toISOString().slice(0, 16),
        deliveryAddress: order.orderInfo.deliveryAddress,
      });
      setItems(order.books);
      setInfo(order);
    }
  }, [id, order]);

  return { items, addBook, removeBook, catalog, isLoading, orderInfo };
};
