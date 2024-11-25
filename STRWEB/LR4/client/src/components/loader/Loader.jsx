import "./Loader.css";

export function Loader(props) {
  return (
    <div
      id={`preloader ${props.id ?? ""}`}
      className={`preloader ${props.class ?? ""}`}
    >
      <div className="square"></div>
      <div className="square square_rev"></div>
    </div>
  );
}
