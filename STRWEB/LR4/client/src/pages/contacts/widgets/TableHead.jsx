import { ChevronDown } from "lucide-react";
import { CONFIG } from "../../../config/config";

const updateOrder = (order, new_order) => {
  if (!order.includes(new_order)) return new_order;
  if (order[0] === "-") return order.slice(1);
  return "-" + order;
};

export const TableHead = ({ order, setOrder, role }) => {
  return (
    <thead>
      <tr>
        {head.map((v) => (
          <th
            key={v.name}
            onClick={() =>
              v.order ? setOrder((prev) => updateOrder(prev, v.order)) : {}
            }
          >
            {v.name}
            {v.order && order.includes(v.order) && (
              <ChevronDown
                size={20}
                className={`emp-order${order[0] === "-" ? " rotate" : ""}`}
              />
            )}
          </th>
        ))}
        {role === CONFIG.ROLES.ADMIN && <th>Control</th>}
      </tr>
    </thead>
  );
};

const head = [
  {
    name: "Full name",
    order: "name",
  },
  {
    name: "Email",
    order: "email",
  },
  {
    name: "Phone",
    order: "phone",
  },
  {
    name: "Photo",
  },
  {
    name: "Description",
    order: "description",
  },
];
