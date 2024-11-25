import multer from "multer";

const fileFilter = (_req, file, cb) => {
  if (file && ["image/png", "image/jpeg", "image/jpg"].includes(file.mimetype))
    return cb(null, true);
  return cb(null, false);
};

const limits = {
  fileSize: 1024 * 1024 * 3,
};

export const createFileLoader = (path, fieldName = "image") => {
  const storage = multer.diskStorage({
    destination(_, __, callback) {
      callback(null, `src/static/${path}`);
    },
    filename(_, file, callback) {
      const fileName =
        new Date()
          .toISOString()
          .slice(0, 19)
          .replace("T", "_")
          .replace(/:/g, "-") + `_${file.originalname}`;
      callback(null, fileName);
    },
  });
  return multer({
    storage: storage,
    fileFilter: fileFilter,
    limits: limits,
  }).single(fieldName);
};
