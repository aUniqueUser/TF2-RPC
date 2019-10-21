#
# A TF2 RPC script by EmeraldSnorlax
# https://github.com/EmeraldSnorlax
# https://steamcommunity.com/id/EmeraldSnorlax/
#


import tkinter
import easygui as gui
import os

tf_folder = ''

TITLE = 'TF2 Rich Presence'
if not os.path.isfile('tf_path.txt'):
    def msg(text):
        gui.msgbox(text, TITLE)

    def multiple(text, options):
        return gui.buttonbox(text, TITLE, options)

    # Get TF2 Path before handing over if user hasn't run this before.
    msg('It looks like this is your first time starting this. \nPerforming first time setup...')
    os = multiple('What OS are you using?', ['Linux', 'Windows', 'macOS'])
    # Grab TF2 folder.
    if os == 'Linux':
        if gui.ynbox('Is your Team Fortress 2 folder at: \n"~/.local/share/Steam/SteamApps/common/Team Fortress 2/" ?'):
            tf_folder = '~/.local/share/Steam/SteamApps/common/Team Fortress 2/'
        else:
            msg('Please open your Team Fortress 2 folder. It should contain a folder named "tf" and a folder named "hl2".')
            tf_folder = gui.diropenbox()
    elif os == 'Windows':
        if gui.ynbox('Is your Team Fortress 2 folder at:\n"C:/Program Files (x86)/Steam/SteamApps/common/Team Fortress 2/" ?'):
            tf_folder = 'C:/Program Files (x86)/Steam/SteamApps/common/Team Fortress 2/'
        else:
            msg('Please open your Team Fortress 2 folder. It should contain a folder named "tf" and a folder named "hl2".')
            tf_folder = gui.diropenbox()
    elif os == 'macOS':
        if gui.ynbox('Is your Team Fortress 2 folder at:\n"~/Library/Application Support/Steam/SteamApps/common/Team Fortress 2/" ?'):
            tf_folder = '~/Library/Application Support/Steam/SteamApps/common/Team Fortress 2/'
        else:
            msg('Please open your Team Fortress 2 folder. It should contain a folder named "tf" and a folder named "hl2".')
            tf_folder = gui.diropenbox()

    f = open('tf_path.txt', 'w+')
    f.write(tf_folder)
    f.close()

# Hand over to RPC script.
os.system('python rpc.py')
