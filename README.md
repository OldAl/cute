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

The program **cutelib.py** is being designed to be able to shorten the video file names so that they can be easier to see on the screen.  When the video equipment does not recognise some of the free video format, it may be necessary to transcode the file to a different format.  This can be done by various free open source programs.  We fancy **HandBrakeCLI**, which will be called by **cutelib.py** using a sub process, called by the program.

As the name suggests the emphasis is on being *cute* and Python is wonderfully suited for the code to be easy to read, to be *cute.*  

At this stage no **GUI** is planned for the cutelib.py.



