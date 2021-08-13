import datetime as dt
import subprocess, time, pyautogui

# Get day from strftime
todaysDayName = dt.date.today().strftime("%a")
timeRightNow = dt.datetime.now().strftime("%H.%M")


def joinMeeting(meetingID, meetingPassword, duration):
    zoomJoinButtonX = 774
    zoomJoinButtonY = 462

    pyautogui.moveTo(
        x=zoomJoinButtonX,
        y=zoomJoinButtonY,
        duration=duration,
        tween=pyautogui.easeInOutQuad,
    )
    pyautogui.click(zoomJoinButtonX, zoomJoinButtonY)
    time.sleep(1.5)
    pyautogui.write(meetingID, interval=0.1)
    pyautogui.click(1000, 700)
    time.sleep(2.5)
    pyautogui.write(meetingPassword, interval=0.1)
    pyautogui.click(1000, 700)


if todaysDayName != "Sat" or todaysDayName != "Sun":
    subprocess.Popen(
        "C:\\Users\\my username duh\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
    )
    joinMeeting(duration=5)

else:
    pass
