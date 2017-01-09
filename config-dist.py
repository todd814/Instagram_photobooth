# Tumblr Setup
# Replace the values with your information
# OAuth keys can be generated from
# https://api.tumblr.com/console/calls/user/info
consumer_key = 'CONSUMER_KEY'  # replace with your key
consumer_secret = 'CONSUMER_SECRET'  # replace with your secret code
oath_token = 'OATH_TOKEN'  # replace with your oath token
oath_secret = 'OATH_SECRET'  # replace with your oath secret code
# replace with your tumblr account name without .tumblr.com
tumblr_blog = 'TUMBLR_BLOG'
tagsForTumblr = "MyTagsHere"  # change to tags you want, separated with commas

# Config settings to change behavior of photo booth
# width of the display monitor
monitor_w = 800
# height of the display monitor
monitor_h = 480
# path to save images
file_path = '/home/pi/photobooth/pics/'
# True will clear previously stored photos as the program launches. False
# will leave all previous photos.
clear_on_startup = False
# how long to debounce the button. Add more time if the button triggers
# too many times.
debounce = 0.3
# True to upload images. False to store locally only.
post_online = True
# if true, show a photo count between taking photos. If false, do not.
# False is faster.
capture_count_pics = True
# True to make an animated gif. False to post 4 jpgs into one post.
make_gifs = True
# True to save high res pics from camera.
# If also uploading, the program will also convert each image
# to a smaller image before making the gif.
# False to first capture low res pics. False is faster.
# Careful, each photo costs against your daily Tumblr upload max.
hi_res_pics = False
# adjust for lighting issues. Normal is 100 or 200. Sort of dark is 400.
# Dark is 800 max.
# available options: 100, 200, 320, 400, 500, 640, 800
camera_iso = 800

# full frame of v1 camera is 2592x1944. Wide screen max is 2592,1555
# if you run into resource issues, try smaller, like 1920x1152.
# or increase memory
# http://picamera.readthedocs.io/en/release-1.12/fov.html#hardware-limits
camera_high_res_w = 1296  # width
camera_high_res_h = 972  # height

# enable color on camera preview
camera_color_preview = False

# Configure sudoers on your system, to can execute shutdown whitout password
# Add this line in file /etc/sudoers
# myUser ALL = (root) NOPASSWD: /sbin/halt
enable_shutdown_btn = False

# Debug mode
debug_mode = False
