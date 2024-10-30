const controlsCont = document.getElementById("control-cont");
const content = document.getElementById("control-text");

function changeFontSize(value) {
  content.style.fontSize = `${value}px`;
}

function changeFontColor(value) {
  content.style.color = value;
}

function changeBgColor(value) {
  document.body.style.backgroundColor = value;
}

function createControlItem(text, type, event, value, min, max) {
  const controlInputCont = document.createElement("div");
  controlInputCont.className = "control-item";
  const label = document.createElement("label");
  label.innerText = text;
  const input = document.createElement("input");
  input.type = type;
  input.value = value;
  input.addEventListener("input", (e) => event(e.target.value));
  if (min && max) {
    input.min = min;
    input.max = max;
  }
  controlInputCont.appendChild(label);
  controlInputCont.appendChild(input);
  return controlInputCont;
}

function createControls() {
  const controls = document.createElement("section");
  controls.id = "controls";
  controls.appendChild(
    createControlItem("Размер шрифта:", "range", changeFontSize, 16, 10, 40)
  );
  controls.appendChild(
    createControlItem("Цвет текста:", "color", changeFontColor, "#000000")
  );
  controls.appendChild(
    createControlItem("Цвет фона:", "color", changeBgColor, "#ffffff")
  );
  controlsCont.appendChild(controls);
}

const toggleControls = document.getElementById("toggle-controls");

toggleControls.addEventListener("change", function () {
  const controls = document.getElementById("controls");
  if (!controls) {
    createControls();
  } else {
    controlsCont.removeChild(controls);
  }
});
