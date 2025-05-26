# VAttackBS
Integration to let you play Brawl Stars with only your voice!

This program only works if you have an Android phone, and preferably a Windows PC (but I'm sure if you're Linux savvy, you can get that to work too). Installation sounds long and confusing, but if I could do it...

Installation steps:
1. Download all of the files in this repository
2. Make sure you have installed Python 3.13 or later. If you have not, make sure to install Python from THE PYTHON WEBSITE AND NOT THE MICROSOFT STORE! Make sure to select "install Python 3.xx to Path" when the option appears.
3. Open a command prompt as an administrator and run "pip install pure-python-adb"
4. Install the program "SCRCPY" (screencopy), also on GitHub. Follow the steps on the page to launch the program properly.
5. Install VoiceAttack if you do not have it installed. (You shouldn't need the paid version; the free version should suffice)
6. Use the shortcut key WIN+R, and then copy in "C:\Users\<your username>\AppData\Roaming\VoiceAttack", making sure to change the username to your Windows account name. Then replace the VoiceAttack.dat file with the one in this repository.
7. Launch the Python file. A command prompt should appear.  
8.  Launch VoiceAttack. You will now have to make a slight change to each command. Hit the pad and pen button in the top left of the program. Double tap on the first command (should be right), and find the selection that is labeled "Send Command to this Target". Select it if not already selected. On the line below that one, select the second option of the two (should be a blank box or a box with a file path in it). Click the dropdown arrow and then select the name that corresponds with the command prompt from step 7. I also recommend exiting the mini window, clicking the wrench in the bottom right of the main page, clicking on the recognition tab, and then changing the Speech Engine to Microsoft.
9. You are almost done! If you happen to have a device that shares the screen size of the Galaxy S21 FE (1080*2400) and are running the default Brawl Stars controls, then you are done! If you are not, there is an easy temporary calibration fix and a harder permanent calibration fix.
10a. (easy) Open your mobile device's settings app -> Developer Settings-> turn on the "Show Taps" setting. Then head to Brawl Stars -> Settings -> Edit Controls.  Type in any one of the movement commands into the command prompt (l,r,u,d), and see where the tap starts from. Move the movement joystick to this location. Do the same with the attack button (a) and the super button (s). You should be fully calibrated!
10b. (hard) Open your mobile device's settings app ->  Developer Settings-> turn on the "Pointer Location" setting. Open the Python file with a IDE (VSCode, Pycharm, Notepad++ for the oldies). Then head to Brawl Stars -> Settings -> Edit Controls. Find the x/y coordinates of each one of the joysticks. Then change the coordinates in the Python file. For movement, the first two numbers correspond to the center of the joystick, and the last two should be the location you drag it to move in the direction specified. The attack and super buttons are auto-aimed and therefore are only the coordinates of the center of the joysticks. Save and relaunch the file. You are fully calibrated!
