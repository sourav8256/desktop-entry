#!/usr/bin/env python

import os.path
from os import path
from os.path import expanduser
import sys
import subprocess

home = expanduser("~");


def start():

    if len(sys.argv) <= 1 :
        print "please give the desktop-entry name as argument! if you give foo as argument, desktop entry foo.desktop will be created!";
        return
    else:
        name = sys.argv[1];
    

    finalPayload = """[Desktop Entry]
Type=
Name=
Comment=
Icon=
Exec=
Terminal=
Categories=
StartupWMClass=""";

    name =  name.lstrip();
    name =  name.rstrip()
    entryPath = home+"/.local/share/applications/" +name+".desktop";
    entry = open(entryPath, "w")
    entry.write(finalPayload)
    entry.close()
    print ("entry created!");
    #myCmd = os.popen('vi '+entryPath).read();

    EDITOR = os.environ.get('EDITOR','vim');
    subprocess.call([EDITOR, entryPath]);

    """

    #!/usr/bin/env xdg-open

    [Desktop Entry]
    Version=1.0
    Type=Application
    Terminal=false
    Exec=command to run here
    Name=visible name here
    Comment=comment here
    Icon=icon path here



    [Desktop Entry]
    Type=Application
    Name=Eclipse
    Comment=Eclipse Integrated Development Environment
    Icon=/home/sourav/eclipse/java-2019-03/eclipse/icon.xpm
    Exec=/home/sourav/eclipse/java-2019-03/eclipse/eclipse
    Terminal=false
    Categories=Development
    StartupWMClass=Eclipse



    """


def command():
    myCmd = os.popen('ls -la').read()
    print(myCmd)


start()

""" command(); """