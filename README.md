# clean_subtitles

Remove Ads from your subtitles.

Ad example: in images folder.

![Ad Example](images/ad_example.png)

A little python script to clean ads from your subtitles, downloaded from opensubtitles.org or any other source.

# How it works:

-It reads the ads.txt file, and build regular expresion from each keyword (keywords are seprated by a comma ',').

-Then it matches the regular expresion with the start of each line in the subtitle file, and delete the whole line if there is a match.

# Requirements:

-Python 3.

-Windows. (just for the send to part)

# Setup:

- Clone the project.

- Edit the path to the ads.txt file, in the info.ini file.

- Edit the ads.txt file, and add your keywords.

- Run the script.

# Usage on windows:

- On windows "Ctrl+R" and run "shell:sendto", this will open the "send to" directory so we can add our bash script.

- Copy the clean_subtitle.cmd file to the "send to" directory.

- clean_subtitle.cmd (this name will show on the send to menu), is the script that sends the path of the selected file or files to our python script.

- Modify the path to the python script in the clean_subtitle.cmd file.

- Right click on any subtitle file or files, send to clean_subtitle.cmd.

# clean_subtitle.cmd example:

```
@echo off
cls
python3 path_to_script\clean_subtitles.py %*
pause
```
