let myChart;

function countRow(x, y) {
  const eps = 0.000001;
  let n = -1;
  let tailorSum = 0;
  while (n + 1 < 1000) {
    n += 1;
    let idx = 2 * n + 1;
    tailorSum += 1 / (idx * Math.pow(x, idx));
    if (Math.abs(2 * tailorSum - y >= eps)) continue;
    break;
  }
  return 2 * tailorSum;
}

function getData() {
  const N = 100;
  const xValues = Array.from({ length: N }, () => {
    let x;
    do {
      x = Math.random() * 20 - 10;
    } while (Math.abs(x) <= 1);
    return parseFloat(x.toFixed(2));
  }).sort((a, b) => a - b);
  const yValues = xValues.map((x) =>
    parseFloat(Math.log((x + 1) / (x - 1)).toFixed(2))
  );
  let rowValues = [];
  for (let i = 0; i < 100; ++i) {
    rowValues.push(countRow(xValues[i], yValues[i]));
  }
  return [xValues, yValues, rowValues];
}

function newChart() {
  const ctx = document.getElementById("myChart").getContext("2d");
  const [xValues, yValues, rowValues] = getData();
  myChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: xValues,
      datasets: [
        {
          label: "Function Graph",
          data: yValues,
          fill: false,
          backgroundColor: "rgba(255, 99, 132, 0.2)",
          borderColor: "rgb(255, 99, 132)",
          borderWidth: 1,
          tension: 0.1,
        },
        {
          label: "Tailor's row Graph",
          data: rowValues,
          fill: false,
          backgroundColor: "rgba(54, 162, 235, 0.2)",
          borderColor: "rgb(54, 162, 235)",
          borderWidth: 1,
          tension: 0.1,
        },
      ],
    },
    options: {
      animation: {
        duration: 3000,
        easing: "easeInOutQuint",
      },
      scales: {
        y: {
          beginAtZero: true,
        },
        x: {
          beginAtZero: true,
        },
      },
    },
  });
}

newChart();

document.getElementById("myChart").addEventListener("click", function () {
  myChart.reset();
  myChart.update();
});
