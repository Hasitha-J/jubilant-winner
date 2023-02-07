# user inputs ________________________________________________________________________________________________

Monthly_product_folder=r"C:\Users\h.jayasekara\Desktop\WaporData\L2_NPP_M" #insert file path
ds_code='L2_NPP_M'    #ds code for file naming should insetr refering WaPOR docs
shapefile = r"C:\Users\h.jayasekara\Desktop\WaporData\Sri_lanka\final1.shp"     #path_to_shapefile.shp
start_date='2015-01-01'
end_date='2022-12-31'
# season = "Maha"  # select the season  -->  "Maha"  "Yala"
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

# ____________________________________________________________________________________________________________
    
    
input_fhs=glob.glob(os.path.join(Monthly_product_folder,'*.tif'))
input_fhs

#Get year to array
year_dates=pd.date_range(start_date,end_date,freq='Y')

#Get df avail 
WaPOR.API.version=2
df_avail=WaPOR.API.getAvailData(ds_code,time_range='{0},{1}'.format(start_date,end_date))


if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
    
driver, NDV, xsize, ysize, GeoT, Projection = gis.GetGeoInfo(input_fhs[0])

sumArrays_Jan_Mar_ = {}
sumArrays_Nov_Dec_ = {}

# # create the sum image _____________________________________________________________________________________

# for creating sumArray for Jan to Mar


for date in year_dates:   
    year_fhs=[]
    
    for fh in input_fhs:
        raster_id=os.path.split(fh)[-1].split('.tif')[0][-7:]
        year=int(raster_id[0:4])
        month=int(raster_id[5:7])
        if (year == date.year) &  (month == 1 or month == 2 or month == 3):
            year_fhs.append(fh)
            
    SumArray=np.zeros((ysize,xsize),dtype=np.float32)
    for f in year_fhs:
        Array=gis.OpenAsArray(f,nan_values=True)
        SumArray+=Array
        
    sumArrays_Jan_Mar_[date.year] = SumArray
     

# for creating sumArray for Nov to Dec  

for date in year_dates:
    year_fhs=[]
    
    for fh in input_fhs:
        raster_id=os.path.split(fh)[-1].split('.tif')[0][-7:]
        year=int(raster_id[0:4])
        month=int(raster_id[5:7])
        if (year == date.year) &  (month == 11 or month == 12):
            year_fhs.append(fh)
            
    SumArray=np.zeros((ysize,xsize),dtype=np.float32)
    for f in year_fhs:
        Array=gis.OpenAsArray(f,nan_values=True)
        SumArray+=Array
        
    sumArrays_Nov_Dec_[date.year] = SumArray
    
# create the final array & save it ___________________________________________________________________________      
for date in year_dates:

    if date.year not in sumArrays_Nov_Dec_:
        print("Array for year {} not found in sumArrays_Nov_Dec_".format(date.year))
        continue
        
    if (date.year+1) not in sumArrays_Jan_Mar_:
        print("Array for year {} not found in sumArrays_Jan_Mar_".format(date.year+1))
        continue
        
    Maha_sumArray = sumArrays_Jan_Mar_[date.year+1] + sumArrays_Nov_Dec_[date.year]
    Maha_sumArray_c = correction_factor * Maha_sumArray
    
    # Save the result as a GeoTIFF file
    out_fh = os.path.join(output_folder, 'WaPOR_{}_{}.tif'.format(naming_product,date.year))  
    gis.CreateGeoTiff(out_fh, Maha_sumArray_c, driver, NDV, xsize, ysize, GeoT, Projection)
    

    
# ____________________________________________________________________________________________________________
# if it is for a year summation
# for date in year_dates:
        
#     year_fhs=[]
# #     SumArray = np.zeros((ysize, xsize), dtype=np.float32)
#     for fh in input_fhs:
#         raster_id=os.path.split(fh)[-1].split('.tif')[0][-7:]
#         year=int(raster_id[0:4])
#         month=int(raster_id[5:7])
#         if (year == date.year):
#             year_fhs.append(fh)
         
#     SumArray=np.zeros((ysize,xsize),dtype=np.float32)
#     for f in year_fhs:
#         Array=gis.OpenAsArray(f,nan_values=True)
#         SumArray+=Array
        
    
#     SumArray = correction_factor * SumArray

#     # Save the result as a GeoTIFF file
#     out_fh = os.path.join(output_folder, 'WaPOR_{}_{}.tif'.format(naming_product,date.year))  
#     gis.CreateGeoTiff(out_fh, SumArray, driver, NDV, xsize, ysize, GeoT, Projection)
