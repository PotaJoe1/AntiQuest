# AntiQuest
A script to remove junk Quest Link log files from your C drive.<br>
<hr>
Quest/Oculus Link has a bug where sometimes it will begin spitting absurd amounts of empty junk log files into the root of your C drive. This can eventually cause instability and slowdown from the sheer amount of files it generates. I didn't notice the issue until it had already created over <b>5 million</b> files.<br>
This program simply looks for the right filenames and extensions of the log files and gets rid of them. It can be used once to deal with existing log files or setup to run on startup to keep it at bay whenever your PC turns on. It won't affect the function of the link software or your VR headset in any way.
<hr>
<h2>Running at startup</h2>
-Install <a href="https://www.python.org/downloads/">Python</a> if you haven't already.<br>
-Download AntiQuest.py from this repository and move it somewhere safe on your PC where it won't get deleted.<br>
-Press Win+R and type "shell:startup" into the run window, then hit enter to bring up the startup folder.<br>
-Create a shortcut to AntiQuest.py and drag it into the Startup folder. This shortcut will then be run every time the system starts.<br>
