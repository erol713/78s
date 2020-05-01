/*$("document").ready(function () {
  $.get("dpw", function (data) {
    for (var key in data) {
      var instl = [];
      var used = [];
      var lic = [];

      for (var k in data[key][0]) {
        instl.push(parseInt(data[key][0][k]));
      }
      for (var k in data[key][1]) {
        used.push(parseInt(data[key][1][k]));
      }
      for (var k in data[key][2]) {
        lic.push(data[key][2][k]);
      }

      console.log(lic);

      var myConfigXe = {
        type: "bar",

        plot: {
          "bars-overlap": "100%",
          animation: {
            effect: "ANIMATION_SLIDE_BOTTOM",
            sequence: "0",
            speed: "800",
            delay: "800",
          },
          tooltip: {
            fontSize: "15",
            fontFamily: "Open Sans",
            padding: "5 10",
            text: "%v",
          },
        },
        plotarea: {
          margin: "10px 10px 80px 20px",
        },

        legend: {
          "toggle-action": "hide",
          header: {
            text: "Licenses",
          },
          item: {
            cursor: "pointer",
          },
          draggable: true,
          "drag-handler": "icon",
        },
        "scale-x": {
          values: lic,
          "items-overlap": true,

          item: {
            "font-angle": -45,
            "wrap-text": true,
            fontSize: "9",
          },
        },
        "scale-y": {
          values: "0:50:10",
          "min-value": 0,
          progression: "lin",
          guide: {
            visible: false,
          },
        },
        series: [
          {
            //plot 1 values
            values: used,
            text: "Used",
            "background-color": "#008aad", //E78785
            alpha: 0.9,
            "bar-width": "40%",
            "hover-state": {
              visible: true,
            },
          },
          {
            //plot 0 values
            values: instl,
            text: "Installed",
            "background-color": "#2cacc9",
            alpha: 0.5,
            "hover-state": {
              visible: true,
            },
          },
        ],
      };

      $("#gapDetails").zingchart({
        id: "gapDetails",
        data: myConfigXe,
        height: "100%",
        width: "100%",
      });
    }
  });
});
*/
