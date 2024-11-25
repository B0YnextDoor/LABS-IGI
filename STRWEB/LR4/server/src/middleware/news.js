import { checkSchema } from "express-validator";

export const validateNewsBody = checkSchema({
  title: {
    isString: {
      errorMessage: "Title must be a string!",
      bail: true,
    },
    notEmpty: {
      errorMessage: "Title is required!",
      bail: true,
    },
    trim: true,
  },
  text: {
    isString: {
      errorMessage: "News text must be a string!",
      bail: true,
    },
    notEmpty: {
      errorMessage: "News text is required!",
      bail: true,
    },
    trim: true,
  },
}).run;
