   Jolla Brute Force Factory Resetter (Jolla BFF Resetter)
  
   This is a simple script to recover a lost security code and to do a factory reset for the original Jolla phone from 2013. It uses Jolla's built-in recovery mode, which can be interfaced with via telnet.

   Reminder: this will NOT recover your data. It will just reflash the phone back to factory settings and delete all your data.
  
   For instructions on how to set up the recovery mode, see: https://jolla.zendesk.com/hc/en-us/articles/204709607-Jolla-Phone-How-do-I-use-the-Recovery-Mode-
   
   With the device connected to your PC and recovery mode running, run this script. It uses Python 2.7.x, so you'll need to install that.
   See: https://www.python.org/downloads/
  
   When the script has found your password, it will alert you with an irritating beep, reset and reboot your phone and let you know your previous security code. Your Jolla device should start right up after the reset, but if it doesn for some reason, I'd suggest you to wait for around 5 mins for it to complete the reflashing procedure, just to be on the safe side of things and not brick your phone.
  
   This script is based on brute-force hacking (guessing in layman's terms), so it's best suited for those that have taken the route of least resistance and only used the minimum length of five digits.
  
   Time required is around 3,2 seconds per one telnet session and three attempts, which is the maximum that Jolla recovery mode v0.1 allows.
   Approximate time required in seconds for a password of length N can be calculated with 10^N * 1,067. For a five digit minimum length this is about 29,6 hours. The time required will increase exponentially for every additional digit. This could possibly be slighty reduced by enhancing the sync between the code and the telnet output. For now it uses a 0,5 second sleep() to wait for the correct input prompts from the Recovery.  
  
   I succesfully used this script to recover the long forgotten security code on my own Jolla device, which hasn't been updated in about three years and is still running 1.0.0.5 (Kaajanlampi)
   with recovery version 0.1.

   Later updates might've introduced additional security measures, such as limiting the number of allowed attempts before further locking down the device, rendering this script useless. In Kaajanlampi there's a setting in the menu for user to select the available number of attempts and fortunately I'd left that at 'unlimited'. In case you have a limit lower than unlimited, your best bet is to send your device to Jolla Care service or invest in some serious forensics hardware and 1337 skillz ;)
  
   Even the slightest variation in how the recovery mode works might completely destroy this piece of script. This has only been tested on version 1.0.0.5 (Kaajanlampi) of the Sailfish OS running Recovery version 0.1.
  
   If you choose to use this script, your mileage may vary and you do so entirely at your own risk. Any damage, time-loss or other harmful or irritating side-effects will be entirely your own responsibility.
   Only intended for use with a device that you legally own. Author is not responsible for any type of misuse of this script and definitely doesn't condone any sort of criminal activity.
  
   I've seen multiple posts around the internet from people who are locked out of their Jollas. Hope this can help a few of you out :)
  
   If you wish to contact me, you may do so on Github or using my e-mail address xtrom0rt@gmail.com. Feel free to report any problems either via Github issue tracker or e-mail. Same goes for contacting me about developing the script further for other versions of Sailfish Recovery.

   Sail on!
   //xtrom0rt