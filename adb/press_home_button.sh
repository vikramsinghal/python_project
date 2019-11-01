press_home_button=$(adb shell input keyevent 3) #HomeButton
echo "Home Button has been pressed."

#Launch Google Keep
launch_google_keep=$(adb shell am start -n com.google.android.keep)
echo "Google Keep should be up and running on the screen"
