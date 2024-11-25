import { checkSchema } from "express-validator";

export const validateReviewBody = checkSchema({
  rate: {
    isNumeric: {
      errorMessage: "Rate must be a number!",
      bail: true,
    },
    isInt: {
      errorMessage: "Rate must be an integer!",
      bail: true,
    },
    notEmpty: {
      errorMessage: "Rate is required!",
      bail: true,
    },
    custom: {
      options: (value) => value > 0 && value < 6,
      errorMessage: "Rate must be an integer from the range [1, 5]!",
    },
  },
  text: {
    isString: {
      errorMessage: "Review text must be a string!",
      bail: true,
    },
    notEmpty: {
      errorMessage: "Review text is required!",
      bail: true,
    },
    trim: true,
  },
}).run;
