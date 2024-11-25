import { Link, useParams } from "react-router-dom";
import { useForm } from "react-hook-form";
import "./Contacts.css";
import { PAGES } from "../../config/routes";
import { Form } from "./widgets/Form";
import { useContact } from "./hooks/useContact";

export const Contact = () => {
  const { id } = useParams();
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm({
    mode: "onChange",
  });
  const { currentFile, update } = useContact(id, reset);
  const onUpdate = (data) => {
    const formData = new FormData();
    formData.append("email", data.email);
    formData.append("name", data.name);
    formData.append("phone", data.phone);
    formData.append("description", data.description);
    formData.append("image", data.image[0]);
    update(formData);
  };
  return (
    <div className="contacts-page upd-emp-cont">
      <div className="back-to-emps">
        <Link to={PAGES.EMPLOYEES} className="animated-link">
          Back to Contacts
        </Link>
      </div>
      <Form
        register={register}
        handleSubmit={handleSubmit}
        errors={errors}
        onSubmit={onUpdate}
        currentImage={currentFile}
      />
    </div>
  );
};
