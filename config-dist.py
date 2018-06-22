# Debug mode
debug_mode = True

# Instagram Setup
# Replace the values with your information
# https://github.com/LevPasha/Instagram-API-python
Insta_login = "" # User Name
Insta_pass = "" #Password
Insta_caption = "#" #Hashtag

#the below uses RAM memory to temporairly store images during processing
# edit /etc/fstab and add tmpfs /home/pi/photobooth/temp_pics/ tmpfs defaults,noatime,nosuid,mode=0777,size=50m 0 0
temp_file_path = "/home/pi/photobooth/temp_pics/"

# path to save final images on sdcard
file_path = "/home/pi/photobooth/event_pics/"

make_montage = True #must be true to post to insta
#use logo **if using text this must be false
use_logo = False
if use_logo:
	logo_dir = "logos/"
	logo_file = "your_logo.png" #must not extend 0x132
	logo_path = logo_dir + logo_file
	#text under pic
#print text **if using logo this must be false

use_text = True #**if using logo this must be false
if use_text:
	text = "'text" + " " + "0,38" + " " + '"Example Text"' +"'" #your text goes in the ""
	font = "helvetica"
	color = "black"
	size = "72"


# True will clear previously stored photos as the program launches. False
# will leave all previous photos.
clear_on_startup = False
# how long to debounce the button. Add more time if the button triggers
# too many times.
debounce = 0.3
# True to upload images. False to store locally only.
post_online = True
# True to upload images to insta. False to store locally only.
post_insta = True
# True to upload images. False to store locally only.
post_gdrive = False
# if true, show a photo count between taking photos. If false, do not.
# False is faster.
capture_count_pics = True ##didnt work on false
# True to make an animated gif. False to post 4 jpgs into one post.
make_gifs = True
#make a mp4 to upload to instagram
make_mp4 = False
# True to make an photomaton image. False do nothing.
make_photobooth_image = False
#thermal printer
make_thermal = False


# True to save high res pics from camera.
# If also uploading, the program will also convert each image
# to a smaller image before making the gif.
# False to first capture low res pics. False is faster.
hi_res_pics = True
# adjust for lighting issues. Normal is 100 or 200. Sort of dark is 400.
# Dark is 800 max.
# available options: 100, 200, 320, 400, 500, 640, 800
camera_iso = 200

# full frame of v2 camera is 3280x2464. Wide screen max is 2592,1555
# if you run into resource issues, try smaller, like 1920x1152.
# or increase memory
camera_high_res_w = 1920  # width (max 3280) 
camera_high_res_h = 1080  # height (max 2464)

# enable color
camera_color_preview = True

# camera orientation
camera_landscape = True

# Configure sudoers on your system, to can execute shutdown whitout password
# Add this line in file /etc/sudoers
# myUser ALL = (root) NOPASSWD: /sbin/halt
enable_shutdown_btn = False

# Printing configuration
enable_print_btn = False

# Config settings to change behavior of photo booth
# width of the display monitor
monitor_w = 800
# height of the display monitor
monitor_h = 480
