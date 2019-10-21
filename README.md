TF2 RPC
---

A theoretically cross-platform Discord Rich Presence Script for Team Fortress 2


Running from source
---
> MAKE SURE TO LAUNCH TF2 WITH THE `-condebug` LAUNCH OPTION

Run `main.py` and follow the prompts.
After setting your path the first time, you will not be asked again.
Delete `tf_path.txt` to reset your path.




FAQ
---

##### Is this VAC safe?

Yes. It does not mess with any of your TF2 files and runs independent of Team Fortress 2. It simply hooks onto the `console.log` file and processes the console output, then matches it up to events.

##### It keeps saying there is no log file found!

Make sure you are launching the game with the `-condebug` launch option. Launch options can be set by right-clicking Team Fortress 2 in your Steam Library, clicking properties, and clicking Set Launch Options. This launch option tells TF2 to leave a log file, which this program can then read.




Credits
---

Log file reading is powered by:
https://github.com/six8/pytailer

GUI is done by:
https://github.com/robertlugg/easygui

