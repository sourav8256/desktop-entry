#!/usr/bin/env python

import os.path
from os import path
from os.path import expanduser
import sys
import subprocess

home = expanduser("~");



def main():
    if(sys.argv) >= 1:
        if sys.argv[1] == "-l":
            listDesktopEntries();
        elif sys.argv[1] == "-c" :
            start();
        elif sys.argv[1] == "-e" :
            editDesktop();
        elif sys.argv[1] == "-h" or sys.argv[1] == "-help" :
            showHelp();
        elif sys.argv[1] == "-v" or sys.argv[1] == "-version" :
            print("1.0");



def showHelp():
    print("desktop-entry -l | for listing all desktop entries.");
    print("desktop-entry -e <desktop-entry-name> | for editing the desktop entry.");
    print("desktop-entry -c | for creating a new desktop entry.");



def listDesktopEntries():
    desktopPath = home+"/.local/share/applications/";
    for file in os.listdir(desktopPath):
        if file.endswith(".desktop"):
            print(file);


def editDesktop():
    desktopPath = home+"/.local/share/applications/";

    if sys.argv[2].endswith(".desktop"):
        path = desktopPath+sys.argv[2];
    else:
        path = desktopPath+sys.argv[2]+".desktop";

    EDITOR = os.environ.get('EDITOR','vi');
    subprocess.call([EDITOR, path]);



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

    EDITOR = os.environ.get('EDITOR','vi');
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


""" start() """

""" command(); """

main();