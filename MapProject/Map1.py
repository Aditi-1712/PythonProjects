import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
volName = list(data["NAME"])
elev = list(data["ELEV"])

def color_change(elevation):

    if int(elevation) <2000:
        return 'pink'
    elif 2000 <= int(elevation) < 3000:
        return 'green'
    else:
        return 'orange'


map = folium.Map(location = [38.58, -99.09], zoom_start = 6, tiles= "cartodb positron")     #map specifications

fgv= folium.FeatureGroup(name ="Volcanoes")                                                     

coordinateList = [[38.97, -98.1], [38.2,-99.1], [37.75, -99.34], [38.12, -97.90]]           #list of coordinates for the marker

for lt, ln, vn,el in zip(lat,lon, volName, elev):  
    fgv.add_child(folium.Marker(location=[lt,ln], popup = vn, icon= folium.Icon(color=color_change(el))))

fgp= folium.FeatureGroup(name ="Population")   

fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function = lambda x : {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 
else 'yellow' if 10000000<= x['properties']['POP2005']< 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
