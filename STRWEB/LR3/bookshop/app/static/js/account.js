function createElement(text) {
  const p = document.createElement("p");
  p.textContent = text;
  return p;
}

function showLocation(position) {
  const coords = position.coords;
  const info = document.getElementById("location-info");
  info.appendChild(
    createElement(`Geographic latitude: ${coords.latitude.toFixed(2)}`)
  );
  info.appendChild(
    createElement(`Geographic longitude: ${coords.longitude.toFixed(2)}`)
  );
  info.appendChild(
    createElement(`Location accuracy: ${coords.accuracy.toFixed(2)} (m)`)
  );
}

function locationError(error) {
  console.log(error);
  document
    .getElementById("location-info")
    .appendChild(
      createElement(
        `Error: ${
          error.code != 2 ? error.message : String(error.message).split(".")[0]
        }`
      )
    );
}

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

async function showBattery() {
  const battery = await window.navigator.getBattery();
  const info = document.getElementById("battery-info");
  if (battery.charging) {
    info.appendChild(createElement("Battery is charging"));
    info.appendChild(
      createElement(
        convertTime(battery.chargingTime, "before full charge", "full charged")
      )
    );
  } else if (battery.dischargingTime != Infinity) {
    info.appendChild(
      createElement(convertTime(battery.dischargingTime, "left", "discharged"))
    );
  }
  info.appendChild(
    createElement(`Charge level: ${Math.round(battery.level * 100)}%`)
  );
}

document.addEventListener("DOMContentLoaded", () => {
  window.navigator.geolocation.getCurrentPosition(showLocation, locationError);
  showBattery();
});
