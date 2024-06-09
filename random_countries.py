import pygal
from pygal_maps_world.maps import World

world_map = World()     #  Create the world map object

world_map.title = "A Map OF Random Countries"   #  Set the title

#   Add the Countries
world_map.add("Random Countries",{
    'aq':10, 'cd':20, 'de':30, 'eg':40,
    'ga':50, 'hk':60, 'in':70, 'jp':80,
    "ng":150, 'nz':90, 'kz':100, 'us':110
})

#   Save the File

world_map.render_to_file('rnd_countries.svg')