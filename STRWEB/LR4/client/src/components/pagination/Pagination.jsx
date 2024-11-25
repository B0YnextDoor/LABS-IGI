import { useMemo } from "react";

import "./Pagination.css";
import { CONFIG } from "../../config/config";

export const Pagination = ({ total, current, setCurrent }) => {
  const totalPages = useMemo(() => Math.ceil(total / CONFIG.LIMIT), [total]);
  const pages = useMemo(() => new Array(totalPages).fill(0), [totalPages]);
  const next = () => {
    if (current == totalPages) return;
    setCurrent(current + 1);
  };
  const prev = () => {
    if (current > 1) setCurrent(current - 1);
  };
  const toPage = (i) => setCurrent(i);
  return (
    <div className="pagination">
      <button disabled={current === 1} onClick={() => prev()}>
        &laquo;
      </button>
      {pages.map((_, idx) => (
        <button
          key={idx}
          className={idx + 1 === current ? "active" : ""}
          onClick={() => toPage(idx + 1)}
        >
          {idx + 1}
        </button>
      ))}
      <button disabled={current === totalPages} onClick={() => next()}>
        &raquo;
      </button>
    </div>
  );
};
