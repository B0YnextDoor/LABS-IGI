function CubeProto(size, color) {
  this._size = size;
  this._color = color;
}

CubeProto.prototype.getSize = function () {
  return this._size;
};

CubeProto.prototype.setSize = function (size) {
  this._size = size;
};

CubeProto.prototype.getColor = function () {
  return this._color;
};

CubeProto.prototype.setColor = function (color) {
  this._color = color;
};

CubeProto.prototype.getVolume = function () {
  return Math.pow(this._size, 3);
};

function EnhancedCubeProto(size, color, material) {
  CubeProto.call(this, size, color);
  this._material = material;
}

EnhancedCubeProto.prototype = Object.create(CubeProto.prototype);
EnhancedCubeProto.prototype.constructor = EnhancedCubeProto;

EnhancedCubeProto.prototype.getMaterial = function () {
  return this._material;
};

EnhancedCubeProto.prototype.setMaterial = function (material) {
  this._material = material;
};

let cubesProto = [];

EnhancedCubeProto.prototype.displayCubes = function () {
  const output = document.getElementById("output-proto");
  output.innerHTML = "";
  cubesProto.forEach((cube, idx) => {
    const li = document.createElement("li");
    li.className = "cube-list";
    li.style.color = cube.getColor();
    li.textContent = `Cube ${
      idx + 1
    }:  Side size = ${cube.getSize()} (cm) --- Color = '${cube.getColor()}' --- Material = '${cube.getMaterial()}'`;
    output.appendChild(li);
  });
};

EnhancedCubeProto.prototype.addCube = function () {
  const size = parseFloat(document.getElementById("size-proto").value);
  const color = document.getElementById("color-proto").value;
  const material = document.getElementById("material-proto").value;
  cubesProto.push(new EnhancedCubeProto(size, color, material));
  this.displayCubes();
};

EnhancedCubeProto.prototype.calculateResult = function () {
  const colors = ["red", "yellow", "blue", "green"];
  const materials = ["wood", "stone", "iron", "gold", "diamond", "netherite"];

  const resultColors = colors.reduce((acc, color) => {
    const filtered = cubesProto.filter((cube) => cube.getColor() === color);
    acc[color] = {
      count: filtered.length,
      volume: filtered.reduce((sum, cube) => sum + cube.getVolume(), 0),
    };
    return acc;
  }, {});

  const resultMaterials = materials.reduce((acc, material) => {
    const filtered = cubesProto.filter(
      (cube) => cube.getMaterial() === material
    );
    acc[material] = {
      count: filtered.length,
      volume: filtered.reduce((sum, cube) => sum + cube.getVolume(), 0),
    };
    return acc;
  }, {});

  const resultOutput = document.getElementById("result-proto");
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
};

document.addEventListener("DOMContentLoaded", () => {
  cubesProto = [];
  const cubeManager = new EnhancedCubeProto();
  document.getElementById("proto-form").addEventListener("submit", (e) => {
    e.preventDefault();
    cubeManager.addCube();
    e.target.reset();
  });
  document.getElementById("proto-res").addEventListener("click", (e) => {
    e.preventDefault();
    if (!cubesProto.length) return;
    cubeManager.calculateResult();
  });
});
