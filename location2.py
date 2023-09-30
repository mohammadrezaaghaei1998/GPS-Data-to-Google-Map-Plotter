import PIL.Image
import PIL.ExifTags
from gmplot import gmplot
from geopy.geocoders import Nominatim
import webbrowser

def extract_gps_info(image_path):
    try:
        img = PIL.Image.open('image_path')
        exif = {
            PIL.ExifTags.TAGS[k]: v
            for k, v in img._getexif().items()
            if k in PIL.ExifTags
        }
        return exif.get('GPSInfo', None)
    except Exception as e:
        print(f"Error extracting GPS info: {str(e)}")
        return None



def convert_gps_to_lat_long(gps_info):
    if gps_info is None:
        return None, None

    north = gps_info[2]
    east = gps_info[4]

    lat = (((north[0] * 60) + north[1]) + north[2] / 60.0) / 60.0
    long = (((east[0] * 60) + east[1]) + east[2] / 60.0) / 60.0

    return lat, long



def get_location_address(lat, long):
    geolocator = Nominatim(user_agent='GetLoc')
    location = geolocator.reverse(f"{lat}, {long}")
    return location.address if location else None



def create_google_map_marker(lat, long, zoom=12):
    gmap = gmplot.GoogleMapPlotter(lat, long, zoom)
    gmap.marker(lat, long, "cornflowerblue")
    return gmap



def main():
    image_path = "your_image.jpg"
    gps_info = extract_gps_info(image_path)
    lat, long = convert_gps_to_lat_long(gps_info)

    if lat is not None and long is not None:
        location_address = get_location_address(lat, long)
        if location_address:
            print(f"Location Address: {location_address}")
            gmap = create_google_map_marker(lat, long)
            gmap.draw("your_map.html")
            webbrowser.open('your_map.html', new=2)
        else:
            print("Location address not found.")
    else:
        print("GPS information not found in the image.")

if __name__ == "__main__":
    main()