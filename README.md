Simple scripts for AFK training in NFF

The .exe files are built via pyinstaller --onefile "path", for those worried about opening random .exe files just use the .py files instead
by opening any IDE that works with python and running it as a Python File.

The 1920x1080_ZX_training does exactly what the name suggests, it presses Z and X when it shows up in the middle of the screen
only works in 1920x1080 for the simple fact that the X and Z images were made for that size, for any different screen sizes you'll have
to get new Z and X images and replace the regions on the "image_location" variable.

The hotslotTraining is an even simpler script that presses 1-0 and TAB, tab for me is hotslot swap, again, if you want to swap that just open the python file
and replace the last line of the main loop "keyboard.press_and_release('tab')", heads-up, just replacing the key in the python file WILL NOT swap it in the .exe 
file for that you'll have to run pyinstaller on the hotslotTraining.py file.

The scripts work best together, the hotslot script attempts to hold Z down for chakra restore but some jutsus cancel that, if an outside source presses Z the script
will reset the Z flag and hold down Z again, hence why having the generative scroll on helps.
