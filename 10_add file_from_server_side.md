<!-- server side -->

const express = require("express");
const app = express();
const path = require("path");

app.get("/image", (req, res) => {
     res.sendFile(path.join(__dirname, "WaPOR_Maha_ET_2015.tif")); // file path/name on server side 
});

app.listen(3000, () => {
     console.log("Server started on port 3000");
});



<!-- client side -->


const map = L.map("map", {
     center: [7.877083, 80.697917],
     zoom: 8,
     doubleClickZoom: false,
     zoomControl: false,
});

const tiles = L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
     maxZoom: 19,
     attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);


const imageurl = "http://localhost:3000/image";

fetch(imageurl)
     .then((response) => response.arrayBuffer())
     .then((arrayBuffer) => {
          parseGeoraster(arrayBuffer).then((georaster) => {
               console.log("georaster:", georaster);

               /*
          GeoRasterLayer is an extension of GridLayer,
          which means can use GridLayer options like opacity.
          Just make sure to include the georaster option!
          http://leafletjs.com/reference-1.2.0.html#gridlayer
      */
               var layer = new GeoRasterLayer({
                    georaster: georaster,
                    opacity: 0.9,
                    clip: undefined,
               });
               layer.addTo(map);

               // map.fitBounds(layer.getBounds());
          });
     });

