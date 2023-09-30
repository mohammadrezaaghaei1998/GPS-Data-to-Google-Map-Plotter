GPS Data to Google Map Plotter
This Python script extracts GPS information from an image's EXIF metadata, converts it to latitude and longitude coordinates, and then creates a Google Map plot with a marker at that location. Additionally, it retrieves the location's address using the Geopy library and displays it on the console.

Dependencies
Before using this script, make sure you have the following dependencies installed:

Pillow: A Python Imaging Library (PIL) fork for opening, manipulating, and saving image files.


pip install Pillow
gmplot: A Python library to create Google Map plots.


pip install gmplot
geopy: A Python library for geocoding and reverse geocoding.


pip install geopy
Usage
Prepare Your Image: Replace "your_image.jpg" with the file path to the image from which you want to extract GPS information. Ensure the image has GPS metadata.

Run the Script:


python script_name.py
Replace script_name.py with the name of your Python script.

Output:

The script will attempt to extract GPS information from the image's EXIF data.
If successful, it will convert the GPS data to latitude and longitude coordinates.
It will then use Geopy to retrieve the location's address and display it on the console.
Finally, it will create a Google Map plot with a marker at the specified GPS coordinates and open it in your default web browser.
Note: If GPS information is not found in the image or if an error occurs, appropriate messages will be displayed in the console.



License
This project is licensed under the MIT License.