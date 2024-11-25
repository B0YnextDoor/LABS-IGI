import { checkSchema } from "express-validator";

export const validateAuthorBody = checkSchema({
  name: {
    errorMessage: "Author name is required!",
    isString: { bail: true },
    notEmpty: { bail: true },
    isAlpha: {
      errorMessage: "Name must contain only letters!",
      bail: true,
    },
    trim: true,
  },
  surname: {
    errorMessage: "Author surname is required!",
    isString: { bail: true },
    notEmpty: { bail: true },
    isAlpha: {
      bail: true,
      errorMessage: "Surname must contain only letters!",
    },
    trim: true,
  },
}).run;

export const validateGenreBody = checkSchema({
  name: {
    errorMessage: "Genre name is required!",
    isString: { bail: true },
    notEmpty: { bail: true },
    isAlpha: {
      bail: true,
      errorMessage: "Genre name must contain only letters!",
    },
    trim: true,
  },
}).run;

export const validateBookBody = checkSchema({
  title: {
    isString: {
      errorMessage: "Title must be a string",
    },
    notEmpty: {
      errorMessage: "Title is required",
    },
    trim: true,
  },
  price: {
    isNumeric: {
      errorMessage: "Price must be a number",
    },
    notEmpty: {
      errorMessage: "Price is required",
    },
    custom: {
      options: (value) => value >= 0,
      errorMessage: "Price must be a non-negative number",
    },
  },
  amount: {
    isNumeric: {
      errorMessage: "Amount must be a number",
    },
    notEmpty: {
      errorMessage: "Amount is required",
    },
    custom: {
      options: (value) => value >= 0,
      errorMessage: "Amount must be a non-negative number",
    },
  },
  genre: {
    isMongoId: {
      errorMessage: "Genre must be a valid MongoDB ObjectId",
    },
    notEmpty: {
      errorMessage: "Genre is required",
    },
  },
  author: {
    isMongoId: {
      errorMessage: "Author must be a valid MongoDB ObjectId",
    },
    notEmpty: {
      errorMessage: "Author is required",
    },
  },
}).run;
