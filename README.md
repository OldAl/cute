# cute
Python 3 program to organise (make cute) video library and optionally transcode some or all video files.

The inspiration for **cutelib.py** came from **PEP 324**.

**PEP 324** describes a new module for starting and communicating
    with processes. *Python 3.5* implements the subprocess module, discussed in *PEP 324*.

I quote *"Starting new processes is a common task in any programming language, and very common in a high-level language like Python.  Good support for this task is needed, because it makes Python an even better replacement language for over-complicated shell scripts."*

This PEP is implemented in python 3.5.
Currently highest version of python in "standard" ubuntu is python 3.4.3. Python3.5 is already available and soon will be part of the "standard" ubuntu, so this is a good time for the proposed program **cutelib.py**.
 
Why do I labour about starting yet another python scripting project? Why am I hesitant about it? It is simply because I am unusually old for this kind of activity. In February of 2016 I will be 91 years old. Many people seem to assume that at my age a person is bound to be more dead than alive. That may well be perfectly true, but we, really old people do have the choice:

We can spend the remaining time acting as if we are "half dead" or we can ignore our frailty and act as we we were still capable of using our remaining brain to some intellectually rewarding work.

Simply put, in old age we have a choice of being **half alive** or **half dead**. Which one is preferable?

The program **cutelib.py** is being designed to be able to shorten the video file names so that they can be easier to see on the screen.  When the video equipment does not recognise some of the free video format, it may be necessary to transcode the file to a different format.  This can be done by various free open source programs.  We fancy **HandBrakeCLI**, which will be ivoked by **cutelib.py** using a sub process, called by the program.

As the name suggests the emphasis is on being *cute* and Python is wonderfully suited for the code to be easy to read, to be *cute.*  

At this stage no **GUI** is planned for the cutelib.py.

**Development notes**

**Wish list**

Transcoding is a very slow process.  Typically, one hour flv video conversion to mp4 takes some 15 - 20 minutes.  It looks as if the program is dead whilst the computer furiously crunches numbers.  I failed to provide a signal, such as a series of dots, to show that something is going on.

**To Do**

Renaming of  files turns out to be a task that needs to be considered seriously. The file names shall:
* have no blanks.  Blanks are to be replaced by alphanumeric characters.
* No + - signs in the alpha, so no hyphens.
* In serials, serial and episode numbers near the beginning of file name.
* File name length not to exceed about 50 chars.  Why 50 - don't know :)

** ######## **

In renaming we need to consider what information can be discarded and what can be relegated to  a list of file names.  The list will inform users what is in the episode.  That will enable the user to select what she wants to watch.

The most flexible way of renaming is to do it by hand with the aid of a file manager, such as Dolphin. Most flexible and most tedious.  We will attempt to classify schemes for some types of related file names, so that they can be renamed programatically.

Usually a bunch of files of a serial video will have something in common.  It turns out that 

Naming

if list segments has three numbers then in the original file name
segments[0] is start of the special number field that will be moved
to the beginning of the file name
segment[1] is the length of the special field
segment[2] is the length of the name that is used. (If segment[2] is arbitrary large number, then the all characters of the name are used.
To visualise this, suppose that segment[0] =

And that is where the description was left to hybernate a couple of years...

**  2016 June 8  *  2016 June 8  *  2016 June 8  *  2016 June 8  *  2016 June 8  *  2016 June 8  **

Today is 2016 Jun 08.  On August 28, 2015 my beloved wife Vida passed away and I am a widower, with the intention of staying a widower.

So I have been away from programming for about 2 years.  Also the conditions have changed. i was spurred into action of writing "cute" because my TV did not recognise **flv** (Flash Video) format

My TV has not improved, however I now have a chrome book which is happy to read **flv** files and project them to my **TV** via a **HDMI** cable.  So the dreaded **transcoding** is not so important.  I now plan to develop a separate little program, called rename.py, which will not do any transcoding.  It will simply change the file names in a selection to a more Linux friendly naming convention. All files in a given set will be renamed, by  replacing significant blanks by a '_" underscore character.  Also any arithmetic signs, such as '-' minus and '+' plus will be "banned", as they can cause cofusion under some circumstances when handled by python. Also, I just do not like "+ - " and similar in the file names.  Also in Linux a higher version of python is now common.  In ubuntu and its variants python 3.1 is now "standard".  So first we will fully develop *renamer.py" in a **procedural programming** style, then we shall re-write it in the **object oriented** style.

Only then we will turn our attention to transcoding the files with the modified file names. 

We then will watch the sunsets and will maintain the two programs - renamer.py - renaming of file lists and cute.py - transcoding thus renamed programs. As I have mentioned, I want to write renamer.py in procedural style (**Procedural Style Program, psp**) and then **object oriented style, oos**.

If you see through my intensions an attempt to illustrate the differences between **psp** and **oos** styles, you are quite correct.  I spent my life teaching and I have no desire to stop now.

Al Kabaila  2016 June 8
e: alkabaila@gmail.com





