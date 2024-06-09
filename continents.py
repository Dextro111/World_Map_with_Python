import pygal
from pygal_maps_world.maps import SupranationalWorld

worldmap = SupranationalWorld()

worldmap.title = "Continents In the World"

worldmap.add("South_America", [('south_america')])
worldmap.add("North_AMerica", [('north_america')])
worldmap.add("Africa", [('africa')])
worldmap.add("Asia", [('asia')])
worldmap.add("Europe", [('europe')])
worldmap.add("Antartica", [('antartica')])
worldmap.add("Oceania", [('oceania')])
worldmap.render_to_file("Map_Continents.svg")