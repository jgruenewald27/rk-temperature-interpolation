import geopandas as gpd # from conda
import pandas as pd
from crate import client # Crate from: "pip install crate"
from shapely.geometry import shape
import datetime
import os

from pathlib import Path

current_working_dir = Path(__file__).parent
tempPath = current_working_dir / "temp_data/"

if not tempPath.exists():
    tempPath.mkdir()

# Create connection
connectionHeal = client.connect(servers="http://129.206.7.154:4200", username="crate", error_trace=True)

# open DB cursor
cursorHeal = connectionHeal.cursor()

# select last time window
dt_utc_now = datetime.datetime.now(datetime.timezone.utc)
dt_delta_timewindow = datetime.timedelta(hours=2)
dt_utc_timewindow = dt_utc_now - dt_delta_timewindow

'''
print(str(dt_utc_now) + " in UTC minus delta of " + str(dt_delta_timewindow) + " is " + str(dt_utc_timewindow))
print(dt_utc_timewindow.timestamp())
# roundet to zero digits in unit milliseconds and delete float format
print(int(round(dt_utc_timewindow.timestamp()*1000,0)))
'''

# create query with correct time epoch
query = "SELECT entity_id, dateobserved, stationname, description, location, temperature, relativehumidity, dewpoint, atmosphericpressure, solarradiation, precipitation, windspeed, winddirection FROM doc.etweatherobserved WHERE dateobserved >=" + str(int(round(dt_utc_timewindow.timestamp()*1000,0)))

# execute request
cursorHeal.execute(sql=query)

# create geodataframe
gdf_conn = gpd.GeoDataFrame(data=cursorHeal.fetchall(), columns=pd.DataFrame(data=cursorHeal.description)[0],)

# work on copied data when sth goes wrong
gdf_data = gdf_conn.copy(deep=True)

# convert geometry to data type
gdf_data.location = gdf_data.location[gdf_data.location.notna()].apply(shape)
gdf_data = gdf_data.set_geometry("location",crs="EPSG:4326")

# Set time to data type
gdf_data.dateobserved = pd.to_datetime(arg=gdf_data.dateobserved, origin="unix", unit="ms", utc=True)

# save gpkg
gdf_data.to_file(os.path.join(tempPath,"db_data.gpkg"), index=False, driver="GPKG")
