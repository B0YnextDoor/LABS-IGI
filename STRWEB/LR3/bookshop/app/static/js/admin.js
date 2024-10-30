let cityChart;
let salesChart;
let incomesChart;
let trandChart;

function getData() {
  const url = new URL("admin-pannel/", window.location.origin);
  url.searchParams.append("data", "");
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      drawCityChart(data["cityList"], data["cityCount"]);
      drawSalesChart(data["month"], data["sales"]);
      drawIncomesChart(data["month"], data["incomes"]);
      drawTrandChart(data["month"], data["sales"]);
    })
    .catch((e) => console.log(`Error: ${e}`));
}

function getRandomColor(opacity = 0.2) {
  const r = Math.floor(Math.random() * 255);
  const g = Math.floor(Math.random() * 255);
  const b = Math.floor(Math.random() * 255);
  return `rgba(${r}, ${g}, ${b}, ${opacity})`;
}

function drawCityChart(cityList, cityCount) {
  if (!cityList || !cityCount) return;
  const ctx = document.getElementById("city_stats_chart").getContext("2d");
  const backgroundColors = cityList.map(() => getRandomColor());
  const borderColors = backgroundColors.map((color) =>
    color.replace("0.2", "1")
  );
  cityChart = new Chart(ctx, {
    type: "polarArea",
    data: {
      labels: cityList,
      datasets: [
        {
          data: cityCount,
          fill: false,
          backgroundColor: backgroundColors,
          borderColor: borderColors,
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

function drawSalesChart(month, sales) {
  if (!month || !sales) return;
  const ctx = document.getElementById("sales_stats_chart").getContext("2d");
  salesChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: month,
      datasets: [
        {
          label: "Sales statistics",
          data: sales,
          fill: false,
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(233, 30, 99, 0.2)",
            "rgba(255, 87, 34, 0.2)",
            "rgba(255, 159, 64, 0.2)",
            "rgba(139, 195, 74, 0.2)",
            "rgba(255, 205, 86, 0.2)",
            "rgba(0, 150, 136, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(121, 85, 72, 0.2)",
            "rgba(201, 203, 207, 0.2)",
          ],
          borderColor: [
            "rgba(255, 99, 132)",
            "rgba(233, 30, 99)",
            "rgba(255, 87, 34)",
            "rgba(255, 159, 64)",
            "rgba(139, 195, 74)",
            "rgba(255, 205, 86)",
            "rgba(0, 150, 136)",
            "rgba(75, 192, 192)",
            "rgba(54, 162, 235)",
            "rgba(153, 102, 255)",
            "rgba(121, 85, 72)",
            "rgba(201, 203, 207)",
          ],
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
          title: {
            display: true,
            text: "Sales",
            font: {
              size: 16,
            },
          },
        },
        x: {
          title: {
            display: true,
            text: "Months",
            font: {
              size: 16,
            },
          },
        },
      },
    },
  });
}

function drawIncomesChart(month, incomes) {
  if (!month || !incomes) return;
  const ctx = document.getElementById("incomes_stats_chart").getContext("2d");
  incomesChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: month,
      datasets: [
        {
          label: "Incomes statistics",
          data: incomes,
          fill: false,
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(233, 30, 99, 0.2)",
            "rgba(255, 87, 34, 0.2)",
            "rgba(255, 159, 64, 0.2)",
            "rgba(139, 195, 74, 0.2)",
            "rgba(255, 205, 86, 0.2)",
            "rgba(0, 150, 136, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(121, 85, 72, 0.2)",
            "rgba(201, 203, 207, 0.2)",
          ],
          borderColor: [
            "rgba(255, 99, 132)",
            "rgba(233, 30, 99)",
            "rgba(255, 87, 34)",
            "rgba(255, 159, 64)",
            "rgba(139, 195, 74)",
            "rgba(255, 205, 86)",
            "rgba(0, 150, 136)",
            "rgba(75, 192, 192)",
            "rgba(54, 162, 235)",
            "rgba(153, 102, 255)",
            "rgba(121, 85, 72)",
            "rgba(201, 203, 207)",
          ],
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
          title: {
            display: true,
            text: "Incomes",
            font: {
              size: 16,
            },
          },
          ticks: {
            callback: function (value, index, ticks) {
              return `${value} BYN`;
            },
          },
        },
        x: {
          title: {
            display: true,
            text: "Months",
            font: {
              size: 16,
            },
          },
        },
      },
    },
  });
}

function drawIncomesChart(month, incomes) {
  if (!month || !incomes) return;
  const ctx = document.getElementById("incomes_stats_chart").getContext("2d");
  incomesChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: month,
      datasets: [
        {
          label: "Incomes statistics",
          data: incomes,
          fill: false,
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(233, 30, 99, 0.2)",
            "rgba(255, 87, 34, 0.2)",
            "rgba(255, 159, 64, 0.2)",
            "rgba(139, 195, 74, 0.2)",
            "rgba(255, 205, 86, 0.2)",
            "rgba(0, 150, 136, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(121, 85, 72, 0.2)",
            "rgba(201, 203, 207, 0.2)",
          ],
          borderColor: [
            "rgba(255, 99, 132)",
            "rgba(233, 30, 99)",
            "rgba(255, 87, 34)",
            "rgba(255, 159, 64)",
            "rgba(139, 195, 74)",
            "rgba(255, 205, 86)",
            "rgba(0, 150, 136)",
            "rgba(75, 192, 192)",
            "rgba(54, 162, 235)",
            "rgba(153, 102, 255)",
            "rgba(121, 85, 72)",
            "rgba(201, 203, 207)",
          ],
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
          title: {
            display: true,
            text: "Incomes",
            font: {
              size: 16,
            },
          },
          ticks: {
            callback: function (value, index, ticks) {
              return `${value} BYN`;
            },
          },
        },
        x: {
          title: {
            display: true,
            text: "Months",
            font: {
              size: 16,
            },
          },
        },
      },
    },
  });
}

function drawTrandChart(month, sales) {
  if (!month || !sales) return;
  const ctx = document.getElementById("trand_stats_chart").getContext("2d");
  trandChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: month,
      datasets: [
        {
          label: "Sales trand",
          data: sales,
          fill: false,
          backgroundColor: "rgba(54, 162, 235, 0.2)",
          borderColor: "rgba(54, 162, 235)",
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
          title: {
            display: true,
            text: "Sales amount",
            font: {
              size: 16,
            },
          },
        },
        x: {
          title: {
            display: true,
            text: "Months",
            font: {
              size: 16,
            },
          },
        },
      },
    },
  });
}

function updateChart(chart) {
  if (!chart) return;
  chart.reset();
  chart.update();
}

function saveChart(chart) {
  const canvas = document.getElementById(chart);

  const tempCanvas = document.createElement("canvas");
  const tempCtx = tempCanvas.getContext("2d");
  tempCanvas.width = canvas.width;
  tempCanvas.height = canvas.height;
  tempCtx.fillStyle = "#ffffff";
  tempCtx.fillRect(0, 0, canvas.width, canvas.height);
  tempCtx.drawImage(canvas, 0, 0);

  const link = document.createElement("a");
  link.href = tempCanvas.toDataURL("image/png");
  link.download = `${chart}.png`;
  link.click();
}

document.addEventListener("DOMContentLoaded", () => {
  document
    .getElementById("city_stats_chart")
    .addEventListener("click", () => updateChart(cityChart));
  document
    .getElementById("city_chart_btn")
    .addEventListener("click", () => saveChart("city_stats_chart"));

  document
    .getElementById("sales_stats_chart")
    .addEventListener("click", () => updateChart(salesChart));
  document
    .getElementById("sales_chart_btn")
    .addEventListener("click", () => saveChart("sales_stats_chart"));

  document
    .getElementById("incomes_stats_chart")
    .addEventListener("click", () => updateChart(incomesChart));
  document
    .getElementById("incomes_chart_btn")
    .addEventListener("click", () => saveChart("incomes_stats_chart"));

  document
    .getElementById("trand_stats_chart")
    .addEventListener("click", () => updateChart(trandChart));
  document
    .getElementById("trand_chart_btn")
    .addEventListener("click", () => saveChart("trand_stats_chart"));

  getData();
});

// document.getElementById('city_chart_btn').addEventListener('click', function() {
// 	const link = document.createElement('a');
// 	link.href = document.getElementById('myChart').toDataURL('image/png');
// 	link.download = 'chart.png';
// 	link.click();
// });
