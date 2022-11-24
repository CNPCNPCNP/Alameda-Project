#CONSTANTS. Use all capitals to define global constants please
import re
from betfairlightweight import filters

URL = 'https://betr.com.au/racebook#/racing/home/upcoming'
CLICK = "arguments[0].click();"
ICON_CSS_SELECTOR = '#bm-content > div.AuthoringLayout_container__N5HOH > div > div.HomeContainer_container__85Qcf > div > div > div:nth-child(1) > button > svg.Icon_icon__zcHyd.Icon_medium__8Hw0y > path'
HORSE_ICON = 'M13.1346'
TROT_ICON = 'M14.9389'
GREYHOUND_ICON = 'M2.73859'
WIN_MARKET_REGEX = re.compile(r'^R\d+$')
PRICE_PROJECTION = filters.price_projection(price_data = filters.price_data(ex_best_offers=True))

#First value is BETR venue name, second value is betfair venue name
VENUES = {# Greyhound races
          "Gunnedah": "Gunnedah",
          "Nowra": "Nowra",
          "Warrnambool": "Warrnambool",
          "Maitland": "Maitland",
          "Angle Park": "Angle Park",
          "Central Park Bags": "Central Park",
          "Suffolk Downs Am": "Suffolk Downs",
          "Perry Bar Bags": "Perry Barr",
          "Swindon Bags": "Swindon",
          "Sheffield Bags": "Sheffield",
          "Doncaster": "Doncaster",
          "Yarmouth Bags": "Yarmouth",
          "Nottingham Bags": "Nottingham",
          "Romford": "Romford",
          "Towcester Bags": "Towcester",
          "Albion Park": "Albion Park", # Both greyhounds and trots at Albion Park? Maybe need more logic to handle edge cases
          "Warragul": "Warragul",
          "Grafton": "Grafton",
          "Gosford": "Gosford",
          "Taree": "Taree",
          "Gawler": "Gawler",
          "Manawatu": "Manawatu",
          "Capalaba": "Capalaba",
          "The Meadows": "The Meadows",
          "Richmond": "Richmond",
          "Traralgon": "Traralgon",
          "Addington": "Addington",
          

          # Trots
          "Pinjarra": "Pinjarra",
          "Mildura": "Mildura",
          "Bendigo": "Bendigo",
          "Globe Derby": "Globe Derby",
          "Wagga": "Wagga",
          "Hamilton": "Hamilton",
          "Ascot Park": "Ascot Park",
          "Bunbury": "Bunbury",
          "Hamilton": "Hamilton",
          "Swan Hill": "Swan Hill",
          "Bathurst": "Bathurst",
          "Redcliffe": "Redcliffe",
          "Melton": "Melton",
          "Alexandra Park": "Alexandra Park",
          "Melton": "Melton",


          
          # Horse races
          "Geelong": "Geelong", # may need to be careful with this one, seen greyhounds at geelong
          "Murwillumbah": "Murwillumbah",
          "Newcastle": "Newcastle",
          "Le Croise Laroc": "Le Croise-Laroche",
          "Southwell": "Southwell",
          "Finger Lakes": "Finger Lakes",
          "Ludlow": "Ludlow",
          "Sedgefield": "Sedgefield",
          "Remington Park": "Remington Park",
          "Turf Paradise": "Turf Paradise",
          "Zia Park": "Zia Park",
          "Laurel Park": "Laurel Park",
          "Philadelphia Park": "Philadelphia",
          "Sandown": "Sandown",
          "Penn National": "Penn National",
          "Mountaineer Park": "Mountaineer Park",
          "Avondale": "Avondale",
          "Doomben": "Doomben",
          "Balaklava": "Balaklava",
          "Warwick Farm": "Warwick Farm",
          "Launceston": "Launceston",
          "Narromine": "Narromine",
          "Belmont": "Belmont",
          "Northam": "Northam",
          "Wyong": "Wyong",
          "Cairns": "Cairns",

          }
