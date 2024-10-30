class CubeClass {
  constructor(size, color) {
    this._size = size;
    this._color = color;
  }

  get size() {
    return this._size;
  }

  set size(size) {
    this._size = size;
  }

  get color() {
    return this._color;
  }

  set color(color) {
    this._color = color;
  }

  get volume() {
    return Math.pow(this._size, 3);
  }
}

let cubesClass = [];

class EnhancedCubeClass extends CubeClass {
  constructor(size, color, material) {
    super(size, color);
    this._material = material;
  }

  get material() {
    return this._material;
  }

  set material(material) {
    this._material = material;
  }

  displayCubes() {
    const output = document.getElementById("output-class");
    output.innerHTML = "";
    cubesClass.forEach((cube, idx) => {
      const li = document.createElement("li");
      li.className = "cube-list";
      li.style.color = cube.color;
      li.textContent = `Cube ${idx + 1}:  Side size = ${
        cube.size
      } (cm) --- Color = '${cube.color}' --- Material = '${cube.material}'`;
      output.appendChild(li);
    });
  }

  addCube() {
    const size = parseFloat(document.getElementById("size-class").value);
    const color = document.getElementById("color-class").value;
    const material = document.getElementById("material-class").value;
    cubesClass.push(new EnhancedCubeClass(size, color, material));
    this.displayCubes();
  }

  calculateResult() {
    const colors = ["red", "yellow", "blue", "green"];
    const materials = ["wood", "stone", "iron", "gold", "diamond", "netherite"];

    const resultColors = colors.reduce((acc, color) => {
      const filtered = cubesClass.filter((cube) => cube.color === color);
      acc[color] = {
        count: filtered.length,
        volume: filtered.reduce((sum, cube) => sum + cube.volume, 0),
      };
      return acc;
    }, {});

    const resultMaterials = materials.reduce((acc, material) => {
      const filtered = cubesClass.filter((cube) => cube.material === material);
      acc[material] = {
        count: filtered.length,
        volume: filtered.reduce((sum, cube) => sum + cube.volume, 0),
      };
      return acc;
    }, {});

    const resultOutput = document.getElementById("result-class");
    resultOutput.innerHTML = "";
    const resType = ["Color results", "Material results"];

    [resultColors, resultMaterials].forEach((res, idx) => {
      resultOutput.innerHTML += `<br/>${resType[idx]}:<br/><br/>`;
      for (let val in res) {
        resultOutput.innerHTML += `${
          val.charAt(0).toUpperCase() + val.substring(1)
        }: Count = ${res[val].count} --- Total Volume = ${
          res[val].volume
        } (cm<sup>3</sup>)<br/>`;
      }
      resultOutput.innerHTML += "<br/>***************<br/>";
    });
  }
}

document.addEventListener("DOMContentLoaded", () => {
  cubesClass = [];
  const cubeManager = new EnhancedCubeClass();
  document.getElementById("class-form").addEventListener("submit", (e) => {
    e.preventDefault();
    cubeManager.addCube();
    e.target.reset();
  });
  document.getElementById("class-res").addEventListener("click", (e) => {
    e.preventDefault();
    if (!cubesClass.length) return;
    cubeManager.calculateResult();
  });
});
