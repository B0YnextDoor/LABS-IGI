import { useMemo, useRef, useEffect } from "react";
import { PAGES } from "../../../config/routes.js";
import { Link } from "react-router-dom";

export const BookCard = ({ book, role }) => {
  const hasAmount = useMemo(() => book.amount > 0, [book]);
  const cardWrapperRef = useRef(null);
  const cardRef = useRef(null);
  useEffect(() => {
    const cardWrapper = cardWrapperRef.current;
    const card = cardRef.current;

    const handleMouseMove = onMouseMove(cardWrapper, card);

    const handleMouseLeave = onMoseLeave(card);

    cardWrapper.addEventListener("mousemove", handleMouseMove);
    cardWrapper.addEventListener("mouseleave", handleMouseLeave);

    return () => {
      cardWrapper.removeEventListener("mousemove", handleMouseMove);
      cardWrapper.removeEventListener("mouseleave", handleMouseLeave);
    };
  }, []);
  return (
    <div className="card-wrapper" ref={cardWrapperRef}>
      <div className="book_card" ref={cardRef}>
        <Link to={role ? `${PAGES.CATALOG}/${book._id}` : ""}>
          {book.title}
        </Link>
        <p>
          Author: {book.author.surname} {book.author.name}
        </p>
        <p>Genre: {book.genre.name}</p>
        <p className={hasAmount ? "zero" : ""}>
          {hasAmount ? `Amount of books: ${book.amount}` : "Out of stock!"}
        </p>
        <span>Price: {book.price} BYN</span>
      </div>
    </div>
  );
};

const onMouseMove = (cardWrapper, card) =>
  function (event) {
    const [x, y] = [event.offsetX, event.offsetY];
    const rect = cardWrapper.getBoundingClientRect();
    const [width, height] = [rect.width, rect.height];
    const middleX = width / 2;
    const middleY = height / 2;
    const offsetX = ((x - middleX) / middleX) * 25;
    const offsetY = ((y - middleY) / middleY) * 25;
    const offX = 50 + ((x - middleX) / middleX) * 25;
    const offY = 50 - ((y - middleY) / middleY) * 20;
    card.style.setProperty("--rotateX", `${offsetX}deg`);
    card.style.setProperty("--rotateY", `${-offsetY}deg`);
    card.style.setProperty("--posx", `${offX}%`);
    card.style.setProperty("--posy", `${offY}%`);
  };

const onMoseLeave = (card) =>
  function () {
    card.style.animation = "reset-card 1s ease";
    card.addEventListener(
      "animationend",
      () => {
        card.style.animation = "unset";
        card.style.setProperty("--rotateX", "0deg");
        card.style.setProperty("--rotateY", "0deg");
        card.style.setProperty("--posx", "50%");
        card.style.setProperty("--posy", "50%");
      },
      { once: true }
    );
  };
