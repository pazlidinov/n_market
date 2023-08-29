const salesChart = document.getElementById("salesChart");
const overdueChart = document.getElementById("overdueChart");

new Chart(salesChart, {
  type: "line",
  data: {
    labels: ["Du ", "Se", "Cho", "Pa", "Ju", "Sh", "Ya"],
    datasets: [
      {
        data: [1.0, 0.5, 0.0, -0.5, -1.0],
        borderWidth: 1,
      },
    ],
  },
});

new Chart(overdueChart, {
  type: "line",
  data: {
    labels: [
      "Yanvar",
      "Fevral",
      "Mart",
      "Aprel",
      "May",
      "Iyun",
      "Iyul",
      "Avgust",
      "Sentabr",
      "Octabr",
      "Noyabr",
      "Dekabr",
    ],
    datasets: [
      {
        data: [1.0, 0.5, 0.0, -0.5, -1.0],
        borderWidth: 1,
      },
    ],
  },
});
