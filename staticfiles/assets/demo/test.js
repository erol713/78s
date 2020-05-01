let chartConfig = {
  graphset: [
    {
      id: "years",
      x: "0%",
      y: "0%",
      width: "100%",
      height: "40%",
      type: "bar",
      title: {
        text: "Parent Child Drilldown",
      },
      plotarea: {
        "margin-top": 50,
        "margin-right": 30,
        "margin-bottom": 40,
        "margin-left": 50,
      },
      "scale-x": {
        values: "1994:2014",
        "max-items": 99,
        guide: {
          visible: false,
        },
      },
      plot: {
        "bars-overlap": "100%",
        rules: [],
      },
      "scale-y": {
        values: "0:150:25",
        "min-value": 0,
        guide: {
          visible: false,
        },
      },
      series: [
        {
          values: [81, 106, 110, 114, 133, 108, 101, 120, 120],
          // this url is the request for months and following filpath is the link to the second page used with data_months
          url:
            "https://us-central1-zingchart-com.cloudfunctions.net/public_pie_datamonths?year=%scale-key-value&filepath=https://us-central1-zingchart-com.cloudfunctions.net/public_pie_datadays",
          target: "graph=months", // the chart id to target the config returned from the url. So within data_months_php the target will be graph=days
          "z-index": 1,
        },
        {
          //just to make the background gray...
          values: [150, 150, 150, 150, 150, 150, 150, 150, 150],
          "background-color": "#E8E7E8",
          maxTrackers: 0,
          "z-index": 0,
        },
      ],
    },

    {
      id: "test",
      x: "0%",
      y: "70%",
      width: "100%",
      height: "30%",
      type: "null",
      "scale-x": {
        "max-labels": 16,
      },
    },
  ],
  "background-color": "white",
};

zingchart.render({
  id: "test",
  data: chartConfig,
  height: "100%",
  width: "100%",
  cachePolicy: "",
});
