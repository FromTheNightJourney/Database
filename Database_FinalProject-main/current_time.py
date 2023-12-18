from datetime import datetime

dateNow = datetime.now()
dateFormat = dateNow.strftime("%m / %d /%Y")
timeNow = datetime.now().hour
dayNow = dateNow.strftime("%A")



TwoFourHrClock = datetime.now().strftime("%H:%M")

if 5 <= timeNow < 12:
    greeting = "morning"
elif 12 <= timeNow < 18:
    greeting = "afternoon"
else:
    greeting = "evening"
    
    
    
