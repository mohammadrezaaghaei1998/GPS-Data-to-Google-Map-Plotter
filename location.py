import PIL.Image
import PIL.ExifTags
from gmplot import gmplot
from geopy.geocoders import Nominatim
import webbrowser

img = PIL.Image.open("your image")

exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags
}

exif['GPSInfo']

north = exif['GPSInfor'][2]
east = exif['GPSInfo'][4]

print(north)
print(east)


lat = (((north[0] * 60) + north[0] * 60) + north[2]) /60 / 60
long = (((east[0] * 60) + east [1] *60) + east[2]) / 60 / 60


gmap = gmplot.GoogleMapPlotter(lat ,long, 12)
gmap.marker(lat,long, "cornflowerbluew")
gmap.draw("your html.html")

geoLoc = Nominatim(user_agent='GetLoc')


webbrowser.open('your html.html' ,new=2)