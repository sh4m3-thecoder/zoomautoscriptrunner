from datetime import date, datetime
import subprocess, time, pyautogui

meetingPianoID = "87205157552"
meetingPianoPassword = "V5Twix"

class9HarvardID = "94966897069"
class9HarvardPassword = "harvard9"


def joinMeeting(meetingID, meetingPassword, duration):
    zoomJoinButtonX = 774
    zoomJoinButtonY = 462

    # launch zoom
    subprocess.Popen("C:\\Users\\mahes\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")

    pyautogui.moveTo(
        x=zoomJoinButtonX,
        y=zoomJoinButtonY,
        duration=duration,
        tween=pyautogui.easeInOutQuad,
    )
    pyautogui.click(zoomJoinButtonX, zoomJoinButtonY)
    time.sleep(1.5)
    pyautogui.write(meetingID, interval=0.1)
    pyautogui.press("enter")
    time.sleep(2.5)
    pyautogui.write(meetingPassword, interval=0.05)
    pyautogui.press("enter")


# Check fuction if it's weekdays or weekends
def checkDayAndJoinMeeting():
    if datetime.today().weekday() == 5 or datetime.today().weekday() == 6:
        return False
    else:
        joinMeeting(class9HarvardID, class9HarvardPassword, 5)


checkDayAndJoinMeeting()
# joinMeeting(class9HarvardID, class9HarvardPassword, 5)
