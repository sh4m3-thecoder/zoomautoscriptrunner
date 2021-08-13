import datetime as dt
import subprocess, time, pyautogui

# Get day or string from
todaysDayName = dt.date.today().strftime("%a")
timeRightNow = dt.datetime.now().strftime("%H.%M")


meetingPianoID = "87205157552"
meetingPianoPassword = "V5Twix"

class9HarvardID = "94966897069"
class9HarvardPassword = "harvard9"


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
    subprocess.Popen("C:\\Users\\mahes\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    joinMeeting(class9HarvardID, class9HarvardPassword, duration=5)

else:
    pass
