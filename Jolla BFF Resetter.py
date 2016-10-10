## Jolla Brute Force Factory Resetter (Jolla BFF Resetter)
##
## This is a simple script to recover a lost security code and to do a factory reset for the original Jolla phone from 2013.
## It uses Jolla's built-in recovery mode, which can be interfaced with via telnet.
## Reminder: this will NOT recover your data. It will just reflash the phone back to factory settings and delete all your data.
##
## For instructions on how to set up the recovery mode, see: https://jolla.zendesk.com/hc/en-us/articles/204709607-Jolla-Phone-How-do-I-use-the-Recovery-Mode-
## With the device connected to your PC and recovery mode running, run this script. It uses Python 2.7.x, so you'll need to install that.
## See: https://www.python.org/downloads/
##
## When the script has found your password, it will alert you with an irritating beep, reset and reboot your phone and let you know your previous security code.
## Your Jolla device should start right up after the reset, but if it doesn for some reason, I'd suggest you to wait for around 5 mins, just to be on the safe side of things and to not brick your phone.
##
## This script is based on brute-force hacking (guessing in layman's terms), so it's best suited for those that have taken the route of least resistance and only used the minimum length
## of five digits. Worst case scenario for finding a five digit security code is around 30 hours. The could would have to be 99999 at this point.
##
## Time required is around 3,2 seconds per one telnet session and three attempts, which is the maximum that Jolla recovery mode v0.1 allows.
## Approximate time required in seconds for a password of length N can be calculated with 10^N * 1,067. For a five character minimum length this is about 29,6 hours.
## The time required will increase exponentially for every additional digit.
##
## I succesfully used this script to recover the long forgotten security code on my own Jolla device, which hasn't been updated in about three years and is still running 1.0.0.5 (Kaajanlampi)
## with recovery version 0.1.
## Later updates might've introduced additional security measures, such as limiting the number of allowed attempts before further locking down the device, rendering this script useless.
## In Kaajanlampi there's a setting in the menu for user to select the available number of attempts and fortunately I'd left it at 'unlimited'.
## In case you have a limit lower than unlimited, your best bet is to send your device to Jolla Care service or invest in some serious forensics hardware and 1337 skillz ;)
##
## Even the slightest variation in how the recovery mode works might completely destroy this piece of script. This has only been tested on version 1.0.0.5 (Kaajanlampi) with recovery version 0.1
## of the Sailfish OS.
##
## If you choose to use this script, your mileage may vary and you do so entirely at your own risk. Any damage, time-loss or other harmful or irritating side effects will be entirely your own problem.
## Only intended for use with a device that you legally own. Author is not responsible for any type of misuse of this script.
##
## I've seen multiple posts around the internet from people who are locked out of their Jollas.
## Hope this can help a few of you out :)
##
## If you wish to contact me, you may do so using my e-mail address xtrom0rt@gmail.com
## Feel free to report any problems with the code or to contact me about making arrangements to possibly get this code working on other versions of Sailfish OS

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
