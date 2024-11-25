import { checkSchema } from "express-validator";
import { isValidObjectId } from "mongoose";

export const validateCreateOrderBody = checkSchema({
  sale: {
    isNumeric: {
      errorMessage: "Sale must be a number!",
      bail: true,
    },
    notEmpty: {
      errorMessage: "Sale is required",
      bail: true,
    },
    custom: {
      options: (value) => {
        if (value < 0) throw new Error("Sale must be a non-negative number!");
        if (value > 100) throw new Error("Max sale is 100%!");
        return true;
      },
      bail: true,
    },
  },
  deliveryDate: {
    isString: {
      errorMessage: "Delivery date must be a string!",
      bail: true,
    },
    notEmpty: {
      errorMessage: "Delivery date is required!",
      bail: true,
    },
    trim: true,
  },
  deliveryAddress: {
    isString: {
      errorMessage: "Delivery address must be a string!",
      bail: true,
    },
    notEmpty: {
      errorMessage: "Delivery address is required!",
      bail: true,
    },
    trim: true,
  },
}).run;

export const validateUpdateOrderBody = checkSchema({
  status: {
    isNumeric: {
      errorMessage: "Status Id must be a number!",
      bail: true,
    },
    notEmpty: {
      errorMessage: "Status Id is required",
      bail: true,
    },
    custom: {
      options: (value) => {
        if (value < 1)
          throw new Error("Status Id must be a non-negative number!");
        if (value > 4) throw new Error("Max status is 4");
        return true;
      },
      bail: true,
    },
  },
  book_ids: {
    isArray: {
      errorMessage: "Body must contain an array of bood ids!",
      bail: true,
    },
    notEmpty: {
      errorMessage: "Order must contain at least one book!",
      bail: true,
    },
    custom: {
      options: (value) => value.every((id) => isValidObjectId(id)),
      errorMessage: "Every book id must be a valid Object Id",
      bail: true,
    },
  },
}).run;
