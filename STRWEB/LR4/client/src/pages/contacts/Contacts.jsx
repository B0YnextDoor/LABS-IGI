import { useProfile } from "../../hooks/useProfile";
import { useContacts } from "./hooks/useContacts";
import { Loader } from "../../components/loader/Loader";
import { TableHead } from "./widgets/TableHead";
import { TableBody } from "./widgets/TableBody";
import { Pagination } from "../../components/pagination/Pagination";
import { useState } from "react";
import { CONFIG } from "../../config/config";
import { useForm } from "react-hook-form";
import "./Contacts.css";
import { Form } from "./widgets/Form";
import { X } from "lucide-react";
import { useCreateContact } from "./hooks/useCreateContact";

export const Contacts = () => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm({
    mode: "onChange",
  });
  const { data } = useProfile();
  const {
    contacts,
    isLoading,
    page,
    setPage,
    filter,
    setFilter,
    order,
    setOrder,
    setIsDeleting,
  } = useContacts();
  const [search, setSearch] = useState("");
  const [isShow, setIsShow] = useState(false);
  const { create, isCreating } = useCreateContact(setIsShow, reset);
  const onAdd = (data) => {
    const formData = new FormData();
    formData.append("email", data.email);
    formData.append("name", data.name);
    formData.append("phone", data.phone);
    formData.append("description", data.description);
    formData.append("password", CONFIG.BASE_PWD);
    formData.append("image", data.image[0]);
    create(formData);
  };
  return (
    <div className="contacts-page">
      <h1>Our employees</h1>
      {data?.role === CONFIG.ROLES.ADMIN && !isShow && (
        <div className="add-emp">
          <button
            className="btn btn-admin"
            disabled={isCreating}
            onClick={() => setIsShow(true)}
          >
            Add Employee
          </button>
        </div>
      )}
      {isShow && (
        <div className="add-form-cont">
          <X
            size={30}
            className="close-form"
            onClick={() => setIsShow(false)}
          />
          <Form
            register={register}
            handleSubmit={handleSubmit}
            errors={errors}
            onSubmit={onAdd}
          />
        </div>
      )}
      <div className="search-emps">
        <input
          type="text"
          placeholder="Filter contacts..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        <button
          className="btn"
          onClick={() => setFilter(search)}
          disabled={isLoading}
        >
          Filter
        </button>
      </div>
      {isLoading ? (
        <Loader />
      ) : contacts && contacts.employees && contacts.employees.length ? (
        <div className="contacts-container">
          <table className="contacts-table">
            <TableHead order={order} setOrder={setOrder} role={data?.role} />
            <TableBody
              contacts={contacts.employees}
              role={data?.role}
              setIsDeleting={setIsDeleting}
            />
          </table>
          <Pagination
            total={contacts.total}
            current={page}
            setCurrent={setPage}
          />
        </div>
      ) : (
        <h1>
          {!search && !filter
            ? "No contacts yet..."
            : "No contacts match your filter..."}
        </h1>
      )}
    </div>
  );
};
