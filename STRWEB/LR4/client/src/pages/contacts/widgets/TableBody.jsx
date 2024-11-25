import { useNavigate } from "react-router-dom";
import { CONFIG } from "../../../config/config";
import { PAGES } from "../../../config/routes";
import { useDeleteContact } from "../hooks/useDeleteContact";

export const TableBody = ({ contacts, role, setIsDeleting }) => {
  const nav = useNavigate();
  const { deleteEmp, isDeleting } = useDeleteContact(setIsDeleting);
  return (
    <tbody>
      {contacts.map((emp, idx) => (
        <tr key={idx}>
          <td>{emp.info.name}</td>
          <td>{emp.email}</td>
          <td>{emp.info.phone}</td>
          <td>
            <img
              src={`${CONFIG.BASE_URL}/${emp.info.imagePath}`}
              width={150}
              height={150}
              alt="employee photo"
            />
          </td>
          <td>{emp.info.description}</td>
          {role === CONFIG.ROLES.ADMIN && (
            <td
              style={{
                display: "flex",
                flexDirection: "column",
                gap: 10,
                minWidth: 160,
              }}
            >
              <button
                className="btn btn-admin"
                disabled={isDeleting}
                onClick={() => nav(`${PAGES.EMPLOYEE_FORM}/${emp._id}`)}
              >
                Update
              </button>
              <button
                className="btn btn-admin"
                disabled={isDeleting}
                onClick={() => deleteEmp(emp._id)}
              >
                Delete
              </button>
            </td>
          )}
        </tr>
      ))}
    </tbody>
  );
};
