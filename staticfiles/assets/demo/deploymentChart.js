zingchart.render({
  height: "100%",
  width: "100%",
  id: "deploymentChart",
  data: {
    type: "bar",

    plot: {
      animation: {
        effect: "ANIMATION_SLIDE_BOTTOM",
        sequence: "0",
        speed: "800",
        delay: "800",
      },
      "value-box": {
        text: "%vt ",
        visible: true,
        "font-color": "white",
        "font-size": "10px",
        decimals: 2,
        placement: "middle",
      },
      tooltip: {
        text: "%v",
      },
    },
    legend: {
      "toggle-action": "hide",
      header: {
        text: "Environment",
      },
      item: {
        cursor: "pointer",
      },
      draggable: true,
      "drag-handler": "icon",
    },
    "scale-x": {
      values: ["Barcelona", "Madrid", "Zaragoza", "Sevilla"],
    },
    series: [
      {
        values: [2, 4, 1, 1],
        text: "Production",
        "background-color": "#008aad",
      },
      {
        values: [1, 2, 1, 0],
        text: "Development",
        "background-color": "#2cacc9",
      },
    ],
  },
});
