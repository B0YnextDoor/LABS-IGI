import { useEffect, useState } from "react";

function convertTime(time, type, msg) {
  let h;
  let m;
  let s;
  if (time > 60) {
    h = Math.floor(time / 3600);
    m = Math.floor((time % 3600) / 60);
    s = time % 60;
    return `${
      h > 0 ? `${h} hour(-s) ` : ""
    }${m} minute(-s) ${s} second(-s) ${type}`;
  }
  return time > 0 ? `${time} seconds ${type}` : `Battery is ${msg}`;
}

function getLocation(position, setLocation) {
  const coords = position.coords;

  setLocation({
    latitude: coords.latitude.toFixed(2),
    longitude: coords.longitude.toFixed(2),
    accuracy: `${coords.accuracy.toFixed(2)} (m)`,
  });
}

async function getBattery(setBattery) {
  const battery = await window.navigator.getBattery();
  if (battery.charging) {
    setBattery({
      isCharging: true,
      chargingTime: convertTime(
        convertTime(battery.chargingTime, "before full charge", "full charged")
      ),
    });
  } else if (battery.dischargingTime != Infinity) {
    setBattery({
      dischargingTime: convertTime(
        battery.dischargingTime,
        "left",
        "discharged"
      ),
    });
  }
  setBattery((prev) => {
    return { ...prev, level: Math.round(battery.level * 100) };
  });
}

function getTime(setTime) {
  setTime({
    local: new Date().toString(),
    utc: new Date().toUTCString(),
  });
}

export const useApiInfo = () => {
  const [location, setLocation] = useState(null);
  const [battery, setBattery] = useState(null);
  const [time, setTime] = useState(null);

  useEffect(() => {
    window.navigator.geolocation.getCurrentPosition((pos) =>
      getLocation(pos, setLocation)
    );
    getBattery(setBattery);
    getTime(setTime);
  }, []);

  return { location, battery, time };
};
