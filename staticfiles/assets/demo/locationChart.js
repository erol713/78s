//Figure out the for loop for pointers
//size of circle matching the size of the deployment

var myConfig = {
  graphset: [
    {
      backgroundColor: "#fff",
      shapes: [
        {
          type: "zingchart.maps",
          options: {
            name: "espL2",
            scrolling: false,
            zoom: 1,
            style: {
              borderWidth: 1,
              borderColor: "#0073a3",
              borderAlpha: 0.1,
              backgroundColor: "#008aad",
              controls: {
                visible: true,
              },
              label: {
                visible: false,
              },
              hoverState: {
                visible: false,
              },
            },
          },
        },
        {
          type: "circle", // shapeid is OPTIONAL but smart if you are targeting events to this shape
          id: "sd",
          x: "-3.7037lon", // hook shape based on lon/lat
          y: "40.4167lat", // hook shape based on lon/lat
          map: "espL2", // assigning to map name or id is necessary
          size: 16,
          offsetY: -20,
          "background-color": "#4dd0e1",
          cursor: "pointer",
          target: "_blank", // just like HTMl we have target _blank
          tooltip: {
            backgroundColor: "rgba(44, 172, 201,0.5)",
            fontColor: "white",
            fonColor: "#fff",
            borderColor: "#2cacc9",
            borderRadius: 3,
            fontSize: 16,
            text: "6 instances",
          },
        },

        {
          type: "circle", // shapeid is OPTIONAL but smart if you are targeting events to this shape
          id: "sd2",
          x: "-0.887712lon", // hook shape based on lon/lat
          y: "41.649693lat", // hook shape based on lon/lat
          map: "espL2", // assigning to map name or id is necessary
          size: 5,
          "background-color": "#4dd0e1",
          cursor: "pointer",
          url:
            "https://en.wikipedia.org/wiki/Anchorman:_The_Legend_of_Ron_Burgundy", // is how you link url to shapes
          target: "_blank", // just like HTMl we have target _blank
          tooltip: {
            backgroundColor: "#2cacc9",
            fontColor: "white",
            borderColor: "#333",
            borderRadius: 3,
            fontSize: 16,
            text: "1 instance",
          },
        },

        {
          type: "circle", // shapeid is OPTIONAL but smart if you are targeting events to this shape
          id: "sd3",
          x: "2.154007lon", // hook shape based on lon/lat
          y: "41.390205lat", // hook shape based on lon/lat
          map: "espL2", // assigning to map name or id is necessary
          size: 9,
          "background-color": "#4dd0e1",
          cursor: "pointer",
          target: "_blank", // just like HTMl we have target _blank
          tooltip: {
            backgroundColor: "#2cacc9",
            fontColor: "white",
            borderColor: "#fff",
            borderRadius: 3,
            fontSize: 16,
            text: "3 instances",
          },
        },

        {
          type: "circle", // shapeid is OPTIONAL but smart if you are targeting events to this shape
          id: "sd4",
          x: "-5.994072lon", // hook shape based on lon/lat
          y: "37.392529lat", // hook shape based on lon/lat
          map: "espL2", // assigning to map name or id is necessary
          size: 4,
          "background-color": "#4dd0e1",
          cursor: "pointer",
          target: "_blank", // just like HTMl we have target _blank
          tooltip: {
            backgroundColor: "#2cacc9",
            fontColor: "white",
            borderColor: "#333",
            borderRadius: 3,
            fontSize: 16,
            text: "2 instances",
          },
        },
      ],
    },
  ],
  tooltip: {
    backgroundColor: "#fff",
    borderColor: "#333",
    borderRadius: 4,
    callout: true,
  },
};

// EVENTS
// -----------------------------
zingchart.bind(null, "shape_click", function (e) {
  if (e.shapeid === "sd") console.log(e);
});

// RENDER CHARTS
// -----------------------------
zingchart.loadModules("maps, maps-espL2", function () {
  zingchart.render({
    id: "locationChart",
    data: myConfig,
    output: "svg",
    height: "100%",
    width: "100%",
  });
});

/* 

code for loop:


aData = [['montauban', 1.352960, 44.022125, 'Montauban', '#F24131', imgO],
	['lemans', 0.209856, 48.008224, 'Le Mans', '#9BA64A', imgG],
	['cannes', 7.017369, 43.552849, 'Cannes', '#9E1C38', imgR],
	['laval', -0.766296, 48.101929, 'Laval', '#9E1C38', imgR],
	['bordeaux', -0.580816, 44.836151, 'Bordeaux', '#2D3E50', imgB],
  ['mulhouse', 7.335888, 47.750839, 'Mulhouse', '#2D3E50', imgB]]
  

for (var i=0;i<aData.length;i++) {
	var info = aData[i];

	g1.shapes.push({

		type : 'circle',
		backgroundImage : info[5],
		backgroundRepeat : 'no-repeat',
		size : 16,
		offsetY : -20,
		id : info[0],
		x : info[1] + 'lon',
		y : info[2] + 'lat',
		map : 'fraL2',
		cursor : 'pointer',
		target : '_blank',
		tooltip : {
			backgroundColor : info[4],
			fontColor : '#FFF',
			text : info[3]
		}
	});
}

*/
