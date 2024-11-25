import { checkSchema } from "express-validator";

export const validateUserBody = checkSchema({
  email: {
    isString: {
      errorMessage: "Email must be a string!",
      bail: true,
    },
    notEmpty: { bail: true, errorMessage: "Email is required!" },
    isEmail: {
      errorMessage: "Invalid email pattern!",
      bail: true,
    },
    trim: true,
  },
  password: {
    isString: {
      errorMessage: "Password must be a string!",
      bail: true,
    },
    notEmpty: { bail: true, errorMessage: "Password is required!" },
    trim: true,
  },
}).run;

export const validateInfoBody = checkSchema({
  name: {
    isString: { bail: true, errorMessage: "Name must be a string!" },
    notEmpty: { bail: true, errorMessage: "Name is required!" },
    trim: true,
  },
  phone: {
    isString: {
      errorMessage: "Phone number must be a string",
    },
    notEmpty: { bail: true, errorMessage: "Phone number is required!" },
    custom: {
      options: (value) => {
        const phonePattern =
          /^(?:\+375|8)(?:\s*\(?0?(?:25|29|33|44)\)?)(?:\s*|-?)\d{3}(?:\s*|-?)\d{2}(?:\s*|-?)\d{2}$/;
        if (!phonePattern.test(value))
          throw new Error("Invalid phone pattern!");
        return true;
      },
    },
  },
  password: {
    isString: {
      errorMessage: "Password must be a string!",
      bail: true,
    },
    notEmpty: { bail: true, errorMessage: "Password is required!" },
    isLength: {
      options: { min: 8 },
      errorMessage: "Password must have minimum 8 chars!",
    },
    custom: {
      options: (value) => {
        if (!/[a-z]+/.test(value)) {
          throw new Error(
            "Password must contain at least one lower case letter!"
          );
        }
        if (!/[A-Z]+/.test(value)) {
          throw new Error(
            "Password must contain at least one upper case letter!"
          );
        }
        if (!/\d+/.test(value)) {
          throw new Error("Password must contain at least one digit!");
        }
        return true;
      },
    },
    trim: true,
  },
}).run;
