
// map

const satellite = L.tileLayer(
     "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw",
     {
          id: "mapbox/satellite-v9",
          tileSize: 512,
          zoomOffset: -1,
          attribution:
               'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>\
                contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
     }
);

var Esri_WorldGrayCanvas = L.tileLayer(
     "https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}",
     {
          attribution: "Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ",
          maxZoom: 16,
     }
);
var CartoDB_DarkMatterNoLabels = L.tileLayer(
     "https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png",
     {
          attribution:
               '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>\
                contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
          subdomains: "abcd",
          maxZoom: 20,
     }
);

var Stadia_AlidadeSmoothDark = L.tileLayer(
     "https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png",
     {
          maxZoom: 20,
          attribution:
               '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy;\
                <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; \
                <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
     }
);
var Stadia_AlidadeSmooth = L.tileLayer(
     "https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png",
     {
          maxZoom: 20,
          attribution:
               '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>,\
                &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> \
                &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
     }
);

const map = L.map("map", {
     center: [7.877083, 80.697917],
     zoom: 8,
     layers: [satellite],
     scrollWheelZoom: false,
     doubleClickZoom: false,
     zoomControl: false,
});

const baseLayers = {
     satellite: satellite,
     ESRIgray: Esri_WorldGrayCanvas,
     CartoDark: CartoDB_DarkMatterNoLabels,
     StadiaDark: Stadia_AlidadeSmoothDark,
     StadiaLight: Stadia_AlidadeSmooth,
};

// L.control.layers(null, baseLayers, { position: "bottomright" }).addTo(map);
L.control.layers(baseLayers).addTo(map);
L.control
     .zoom({
          position: "topright",
     })
     .addTo(map);

