const map = L.map('map').setView([7.877083, 80.697917], 8);

function getColor(d) {
    return d > 13000 ? '#800026' :
           d > 12000  ? '#BD0026' :
           d > 11000  ? '#E31A1C' :
           d > 10000  ? '#FC4E2A' :
           d > 5000   ? '#FD8D3C' :
           d > 1000   ? '#FEB24C' :
           d > 10   ? '#FED976' :
                      '#FFEDA0';
}

function style(feature) {
    return {
        fillColor: getColor(feature.properties.OBJECTID),
        weight: 1,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 01
    };
}
L.geoJson(srilanka, {style: style}).addTo(map);

const osm = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var slData = L.geoJSON(srilanka , {
    
    onEachFeature: function(feature,layer){
    layer.bindPopup('<b>This is a </b>' + feature.properties.DISTRICT_N)
},
style:{
    "weight": 1,
}
}).addTo(map);
