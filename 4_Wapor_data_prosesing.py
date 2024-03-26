import sys
import geopandas as gpd
import rasterio
import rasterio.mask

# user inputs ________________________________________________________________________________________________

Monthly_product_folder=r"C:\Users\h.jayasekara\Desktop\WaporData\Sri_lanka\L2_NPP_M\2021" #insert file path
ds_code='L2_NPP_M'    #ds code for file naming should insetr refering WaPOR docs
shapefile = r"C:\Users\h.jayasekara\Desktop\WaporData\Sri_lanka\final1.shp"     #path_to_shapefile.shp
# ____________________________________________________________________________________________________________

product_name = ds_code.split("_")
naming_product = product_name[1]

path_split = os.path.split(Monthly_product_folder)
naming_year = path_split[1]

#output folder name
output_folder=Monthly_product_folder.replace(naming_year,'Maha_{}'.format(naming_product)) 


if (naming_product == "NPP"):
    correction_factor = 0.001
    
elif (naming_product == "AET"):
    correction_factor = 0.1

else:
    print("error")
    sys.exit()
    
# create the sum image

input_fhs=glob.glob(os.path.join(Monthly_product_folder,'*.tif'))
input_fhs

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
driver, NDV, xsize, ysize, GeoT, Projection = gis.GetGeoInfo(input_fhs[0])


# Sum the data for the current season

SumArray = np.zeros((ysize, xsize), dtype=np.float32)
for fh in input_fhs:
    Array = gis.OpenAsArray(fh, nan_values=True)
    SumArray += Array

SumArray  =  correction_factor * SumArray
    
# Save the result as a GeoTIFF file

out_fh = os.path.join(output_folder, 'WaPOR_{}_{}.tif'.format(naming_product,naming_year))    
gis.CreateGeoTiff(out_fh, SumArray, driver, NDV, xsize, ysize, GeoT, Projection)


# rescaling if needed ___________________________________________________________________________________________


# clip the result _______________________________________________________________________________________________

output_folder_clip=Monthly_product_folder.replace(naming_year,'Maha_{}_Clipped'.format(naming_product))

if not os.path.exists(output_folder_clip):
    os.makedirs(output_folder_clip)
    
# read shp file
gdf = gpd.read_file(shapefile)

with rasterio.open(out_fh) as src:
    out_image, out_transform = rasterio.mask.mask(src, gdf.geometry, crop=True)
    out_meta = src.meta.copy()

out_meta.update({"driver": "GTiff",
                 "height": out_image.shape[1],
                 "width": out_image.shape[2],
                 "transform": out_transform})

with rasterio.open(os.path.join(output_folder_clip, 'WaPOR_{}_{}_clipped.tif'.format(naming_product,naming_year)), "w", **out_meta) as dest:
    dest.write(out_image)
