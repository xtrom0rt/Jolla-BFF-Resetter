import telnetlib
import winsound

from sys import exit
from time import sleep

sleepTime = 0.5
currentPwCandidate = 0

def pwGenerator():
    global currentPwCandidate
    currentPwCandidate += 1
    return str(currentPwCandidate).zfill(5)

def pwFound(tn, output, pwCandidate):

    print "I think I found the code. Now let me make some noise for a while to alert you to my success :)"
    winsound.Beep(1000,5000)
    
    print "Here's the last output: \n\n"
    
    print output + "\n\n"
    print "Your phone should be currently resetting itself."
    print "Let it do its thing for a while and it should start right up."
    print "By the way: your lost security code was " + pwCandidate + "."
    print "Please stand by and wait for your Jolla to reboot..."
    
    # thirty seconds should be enough for the phone to reflash itself
    sleep(30)

    # one final press of enter and we should be good to go
    tn.write("\n")

    # wait two secs and exit
    sleep(2)
    exit()
    return

def openConnection():
    # connection params
    host = "10.42.66.66"
    port = 23
    timeout = 15

    # open connection, time out after 15 secs of unsuccesful trying
    print "Attempting telnet connection to the device @ " + host + ":" + str(port) + " (time-out after " + str(timeout) + " seconds"
    tn = telnetlib.Telnet(host, port, 15)    
    
    return tn
    
def attemptPasswordInput(tn):

    # Output when password is wrong
    # [WARNING] Wrong code, try again (x left)

    #

    # Type your devicelock code and press [ENTER] key:

    # (please note that the typed numbers won't be shown for security reasons)

    pwCandidate = pwGenerator()
    print "Current password candidate: " + pwCandidate
    tn.write(pwCandidate + "\n")
    sleep(sleepTime)
    output = tn.read_very_eager()

    # Phone says something with "Wrong code" NOT in it. This is either good or very bad.
    if ("Wrong code" in output) == False: 
         pwFound(tn, output, pwCandidate)
    
    print output

    return
         
def haxx0rSession(tn):

    # Output should be:
    # -----------------------------
    #     Jolla Recovery v0.1
    # -----------------------------
    # Welcome to the recovery tool!
    # The available options are:
    # 1) Reset phone to factory settings
    # 2) Reboot phone
    # 3) Exit
    # Type the number of the desired action and press [ENTER]:

    sleep(sleepTime)
    output = tn.read_very_eager()
    print output

    # select factory reset
    tn.write("1\n")

    sleep(sleepTime)
    output = tn.read_very_eager()
    print output

    # Output should be:
    # Are you really SURE? If you continue, ALL DATA (pictures, videos, messages, accounts and all the personal data) stored in the device memory WILL BE ERASED! [y/n]

    # confirm factory reset
    tn.write("y\n")

    sleep(sleepTime)
    output = tn.read_very_eager()
    print output
    
    # Output should be:
    # [CLEANUP] Starting cleanup!
    # [CLEANUP] Umounting top volume...
    # [CLEANUP] Cleanup done.
    # Mounting /dev/mmcblk0p28 on /mnt
    #
    # Type your devicelock code and press [ENTER] key:
    # (please note that the typed numbers won't be shown for security reasons)

    # at this point, we got three attempts to guess the password
    for attemptNum in range(0,3):
        attemptPasswordInput(tn)

    haxx0rSession(openConnection())

    return

haxx0rSession(openConnection())