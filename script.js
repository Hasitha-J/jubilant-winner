// Add Raster Image (geo tiff)
  
var url_to_geotiff_file = "L2_LKA_GBWP_20s2.tif";

fetch(url_to_geotiff_file)
  .then(response => response.arrayBuffer())
  .then(arrayBuffer => {
    parseGeoraster(arrayBuffer).then(georaster => {
      console.log("georaster:", georaster);

      /*
          GeoRasterLayer is an extension of GridLayer,
          which means can use GridLayer options like opacity.
          Just make sure to include the georaster option!
          http://leafletjs.com/reference-1.2.0.html#gridlayer
      */
      var layer = new GeoRasterLayer({
          georaster: georaster,
          opacity:0.9,
          clip: undefined
      });
      layer.addTo(map);

      map.fitBounds(layer.getBounds());

  });
});

