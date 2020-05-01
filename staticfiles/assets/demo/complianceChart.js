var compliance = {
  type: "pie",
  plot: {
    borderColor: "#fff",
    borderWidth: 0,
    // slice: 90,
    valueBox: {
      placement: "out",
      text: "%t ",
      fontFamily: "Open Sans",
      fontSize: "9",
    },
    tooltip: {
      fontSize: "15",
      fontFamily: "Open Sans",
      padding: "5 10",
      text: "%v\n licensed, %data-usage used",
    },
    animation: {
      effect: 2,
      method: 5,
      speed: 900,
      sequence: 1,
      delay: 800,
    },
    title: {
      fontColor: "#343a40",
      text: "Compliance summary",
      align: "right",
      offsetX: 10,
      fontFamily: "Open Sans",
      fontSize: 16,
    },
  },
  plotarea: {
    margin: "0 0 0 0",
  },
  series: [
    {
      values: [1],
      text: "Cell manager for Unix",
      backgroundColor: "#2CACC9",
      dataUsage: [1],
    },
    {
      values: [1],
      text: "Manager of Managers ext for Unix",
      backgroundColor: "#1499B9",
      dataUsage: [1],
    },
    {
      values: [7],
      text: "Drive for Unix",
      backgroundColor: "red",
      dataUsage: [9],
      detached: true,
    },
    {
      text: "Drive for Windows/Linux",
      values: [4],
      backgroundColor: "#1DA1C0",
      dataUsage: [0],
    },
    {
      text: "Online backup for Unix",
      values: [6],
      backgroundColor: "#0A92B3",
      dataUsage: [5],
    },
    {
      text: "Online backup for Windows/Linux",
      values: [21],
      backgroundColor: "red",
      detached: true,
      dataUsage: [128],
    },
    {
      text: "Advanced backup to disk",
      values: [215],
      backgroundColor: "#2cacc9",
      detached: true,
      dataUsage: [125],
    },
    {
      text: "HPE DP Granular Recovery Extension",
      values: [5],
      backgroundColor: "#058EB0",
      dataUsage: [0],
    },
  ],
};

zingchart.render({
  id: "complianceChart",
  data: compliance,
  height: "100%",
  width: "100%",
});
