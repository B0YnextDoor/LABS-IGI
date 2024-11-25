import { Schema, model } from "mongoose";

const employeeSchema = new Schema(
  {
    email: {
      type: String,
      required: true,
      unique: true,
    },
    password: {
      type: String,
      required: true,
    },
    isAdmin: {
      type: Boolean,
      default: false,
    },
    info: {
      type: Schema.Types.ObjectId,
      ref: "EmployeeInfo",
    },
  },
  {
    timestamps: { createdAt: "createdAt", updatedAt: "updatedAt" },
    collection: "employees",
  }
);

employeeSchema.pre("findOneAndDelete", async function (next) {
  try {
    const employee = await this.model.findOne(this.getFilter());
    if (employee && employee.info) {
      await model("EmployeeInfo").findOneAndDelete({ _id: employee.info });
    }
    next();
  } catch (error) {
    next(error);
  }
});

const employeeInfoSchema = new Schema(
  {
    name: {
      type: String,
      required: true,
    },
    phone: {
      type: String,
      required: true,
      unique: true,
    },
    imagePath: {
      type: String,
    },
    description: {
      type: String,
      required: true,
    },
    employee: {
      type: Schema.Types.ObjectId,
      ref: "Employee",
      required: true,
      unique: true,
    },
  },
  {
    timestamps: { createdAt: "createdAt", updatedAt: "updatedAt" },
    collection: "employee_infos",
  }
);

export const Employee = model("Employee", employeeSchema);
export const EmployeeInfo = model("EmployeeInfo", employeeInfoSchema);
