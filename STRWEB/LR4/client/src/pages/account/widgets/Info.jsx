import { useApiInfo } from "../hooks/useApiInfo.js";

export const Info = () => {
  const { location, battery, time } = useApiInfo();
  return (
    <section className="acc-info-section">
      {time ? (
        <div>
          <h4>Time Info</h4>
          {Object.keys(time).map((key) => (
            <p key={key}>
              <span>{key}</span>: {time[key]}
            </p>
          ))}
        </div>
      ) : (
        <h4>Can't display time info...</h4>
      )}
      <div className="acc-api-info">
        {location ? (
          <div>
            <h4>Location info</h4>
            {Object.keys(location).map((key) => (
              <p key={key}>
                <span>{key}</span>: {location[key]}
              </p>
            ))}
          </div>
        ) : (
          <h4>Can't fetch location info...</h4>
        )}
        {battery ? (
          <div>
            <h4>Battery Info</h4>
            {battery.isCharging ? (
              <p>Charging time: {battery.chargingTime}</p>
            ) : (
              <p>Time left: {battery.dischargingTime}</p>
            )}
            <p>Battery level: {battery.level}%</p>
          </div>
        ) : (
          <h4>Can't fetch battery info...</h4>
        )}
      </div>
    </section>
  );
};
