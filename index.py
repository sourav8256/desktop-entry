#!/usr/bin/env python

import os.path
import subprocess
from os import path
from os.path import expanduser


home = expanduser("~");


def start():
    version_default = "1.0"
    type_default = "Application"
    category_default = "Development"
    terminal_default = "false"
    mexec_default = ""
    name_default = ""
    comment_default = ""
    icon_default = ""

    repeat = True

    while repeat:

        print("\n\n***************** Taking Inputs **********************\n\n")

        version = raw_input("Plese enter version (blank defaults to {version_default}) : ".format(
            version_default=version_default))
        type = raw_input("Please enter the type (blank defaults to {type_default}) : ".format(
            type_default=type_default))
        terminal = raw_input("Plese enter \"true\" for terminal and \"false\" for GUI (blank defaults to {terminal_default}) : ".format(
            terminal_default=terminal_default))
        mexec = raw_input(
            "Plese enter command to be executed (compulsory, current value = {}) : ")
        name = raw_input("Plese enter name of the application (compulsory) : ")
        comment = raw_input("Plese enter any comment (optional) : ")
        icon = raw_input("Plese enter the path to the Icon : ")

        print("\n\n***************** Given Inputs **********************\n\n")

        print("Plese enter version (blank defaults to 1.0) : "+version)
        print("Please enter the type (blank defaults to Application) : "+type)
        print("Plese enter 1 for terminal and 0 for GUI (blank defaults to 1) : "+terminal)
        print("Plese enter command to be executed (compulsory) : 1 "+mexec)
        print("Plese enter name of the application (compulsory) : "+name)
        print("Plese enter any comment (optional) : "+comment)
        print("Plese enter the path to the Icon : "+icon)

        print("\n\n*****************************************************\n\n")

        res = raw_input("press y to continue e to edit the variables again : ")

        if res == 'e':
            repeat = True
        elif res == 'y':
            repeat = False
        else:
            repeat = False

    """ VALIATION """
    if not path.exists(icon):
        print("warning : The icon fie path is invalid.")

    version_default = version
    type_default = type
    terminal_default = terminal
    mexec_default = mexec
    name_default = name
    comment_default = comment
    icon_default = icon

    finalPayload = """
[Desktop Entry]
Type={type_default}
Name={name_default}
Comment={comment_default}
Icon={icon_default}
Exec={mexec_default}
Terminal={terminal_default}
Categories={category_default}
StartupWMClass=Eclipse

""".format(
    version_default=version_default,
    type_default=type_default,
    terminal_default=terminal_default,
    mexec_default=mexec_default,
    name_default=name_default,
    comment_default=comment_default,
    icon_default=icon_default
)

    name =  name.lstrip();
    name =  name.rstrip()
    entry = open(home+"/.local/share/applications/" +name+".desktop", "w")
    entry.write(finalPayload)
    entry.close()

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


start()
