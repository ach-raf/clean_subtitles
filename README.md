# clean_subtitles
Remove Ads from your subtitles.

Ad example:

![Ad example](images/ad_example.png)

A little python script to clean your donwloaded subtitles from opensubtitles.org.

# Usage:

Right click on any .srt file or files, send to clean_srt.cmd.

# Requirements:
-Windows. (just for the send to part)

-Python 3.

# Setup:
Create a txt file to put the unwanted ads.

Download the clean_srt.py file, edit the path to the ads.txt file 

On windows "Ctrl+R" and run "shell:sendto"
this will open the "send to" directory so we can add our bash script.


To run the python script you must create clean_srt.cmd (this name will show on the send to menu)

clean_srt.cmd script that sends the path of the selected file or files to our python script
```
@echo off
cls
python3 path_to_script\clean_subs.py %*
pause
```



