# clean_subtitles
Remove Ads from your subtitles.

Ad example: in images folder.

![Ad Example](images/ad_example.png)


A little python script to clean your downloaded subtitles from opensubtitles.org.

# Usage:

Right click on any .srt file or files, send to clean_srt.cmd.

# Requirements:
-Windows. (just for the send to part)

-Python 3.

# How it works:
-I use regular expresions to match each keyword from the ads.txt file, with the start of each line in the subtitle file, and delete the whole line if there is a match.

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



