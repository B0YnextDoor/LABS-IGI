import "./Account.css";
import { useForm } from "react-hook-form";
import { useInitialData } from "./hooks/useInitialData.js";
import { Loader } from "../../components/loader/Loader.jsx";
import { Form } from "./widgets/Form.jsx";
import { Info } from "./widgets/Info.jsx";
import { useUpdateProfile } from "./hooks/useUpdateProfile.js";
import { CONFIG } from "../../config/config.js";
import { OrderList } from "../../components/order/OrderList.jsx";

export const Account = () => {
  const {
    register,
    handleSubmit,
    watch,
    reset,
    formState: { errors },
  } = useForm({
    mode: "onChange",
  });

  const { role, isLoading } = useInitialData(reset);
  const { update, isPending } = useUpdateProfile();

  const onSubmit = (data) => update(data);

  return (
    <section className="account_page">
      <h1>User Info</h1>
      <section className="user_info">
        {isLoading ? (
          <Loader />
        ) : (
          <Form
            onSubmit={handleSubmit(onSubmit)}
            register={register}
            watch={watch}
            errors={errors}
            disabled={isPending}
          />
        )}
        <Info />
      </section>
      {role === CONFIG.ROLES.CUSTOMER && <OrderList />}
    </section>
  );
};
