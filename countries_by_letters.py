import pygal
from pygal_maps_world.maps import World
from pygal.style import Style

custom_style = Style(colors = ('#FF0000', '#0000FF', '#00FF00', 
                               '#000000', '#FFD700'))

worldmap = World()
worldmap.title = "Countries Starting With Specific letters"

worldmap.add('"E" Countries', ['ec', 'ee', 'eg','er','es','et'])
worldmap.add('"F" Countries', ['fr', 'fi'])
worldmap.add('"P" Countries', 
        ['pa', 'pe', 'pg','ph','pk','pl','ps','pr','pt','py'])
worldmap.add('"Z" Countries', ['zm', 'zv'])
worldmap.add('"A" Countries', ['ad', 'ae', 'af','al','am',
                     'ao', 'aq','aq', 'ar', 'at', 'au', 'az'])
worldmap.add('"N" Countries', ['ng', 'ni', 'nz','na','no'])

worldmap.render_to_file("lettered_countries.svg")