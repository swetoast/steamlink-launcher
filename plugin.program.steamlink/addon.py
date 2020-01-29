"""Steamlink Launcher for OSMC"""
import os
import xbmc
import xbmcgui
import xbmcaddon

__plugin__ = "steamlink"
__author__ = "toast"
__url__ = "https://github.com/swetoast/steamlink-launcher/"
__git_url__ = "https://github.com/swetoast/steamlink-launcher/"
__credits__ = "toast"
__version__ = "0.0.7"

dialog = xbmcgui.Dialog()
addon = xbmcaddon.Addon(id='plugin.program.steamlink')

def main():
    """Main operations of this plugin."""
    if os.path.isfile("/tmp/steamlink-launcher.sh"):
        output = os.popen("sh /tmp/steamlink-launcher.sh").read()
    else:
        create_files()
        output = os.popen("sh /tmp/steamlink-launcher.sh").read()
    dialog.ok("Starting Steamlink", output)
    #print output
def create_files():
    """Creates bash files to be used for this plugin."""
    with open('/tmp/steamlink-launcher.sh', 'w') as outfile:
        outfile.write('#!/bin/sh\n'
                    'start_steamlink () {\n'
                    'sh /tmp/steamlink-watchdog.sh &\n'
                    'if [ -f "openvt" ]\n'
                    'then openvt -c 7 -s -f clear\n'
                    'openvt -c 7 -f -s steamlink > /dev/null 2> &1\n'
                    'systemctl stop mediacenter\n'
                    'else systemctl stop kodi && /storage/steamlink\n'
                    '}\n'
                    'install_steam () {\n'
                    'kodi-send --host=127.0.0.1 --action=Notification(Downloading,Downloading Steamlink, Please wait.....[,15000])\n'
                    'mkdir /storage\n'
                    'chown $USER /storage\n'
                    'if [ $(cat /etc/os-release | grep OSMC | vc - l) -eq 1 ]\n'
                    'then apt-get install replaceme\n'
                    'else wget replaceme -O /storage/lib.zip\n'
                    'rm /storage/lib.zip\n'
                    'mkdir /storage/steamlink/overlay_work\n'
                    'mkdir /storage/.config/system.d/\n'
                    'wget https://raw.githubusercontent.com/swetoast/steamlink-launcher/dev/libreelec_additonal/60-steam-input.rules -O /storage/.config/system.d/storage-steamlinkudev-rules.d.mount\n'
                    'if [ ! -f /lib/udev/rules.d/60-steam-input.rules ]; then\n'
                    'mount -t overlay overlay -o lowerdir=/lib/udev/rules.d,upperdir=/storage/steamlink/udev/rules.d/,workdir=/storage/steamlink/overlay_work /lib/udev/rules.d\n'
                    'udevadm trigger; fi\n'
                    'systemctl enable storage-steamlink-udev-rules.d.mount; fi\n'
                    'kodi-send --host=127.0.0.1 --action=Notification(Downloading,Downloading Steamlink Libraries, Please wait....[,15000])\n'
                    'wget "$(wget -q -O - http://media.steampowered.com/steamlink/rpi/public_build.txt)" -O /storage/steamlink.tar.gz\n'
                    'tar -zxf steamlink.tar.gz\n'
                    'rm steamlink.tar.gz\n'
                    'chown $USER /storage/steamlink\n'
                    'chmod +x $USER /storage/steamlink\n'
                    'usermod -a -G input,plugdev $USER\n'
                    'start_steamlink\n'
                    '}\n'
                    'if [ ! -f "/storage/steamlink" ]; then install_steamlink; else start_steamlink; fi')
        outfile.close()
    with open('/tmp/steamlink-watchdog.sh', 'w') as outfile:
        outfile.write('#!/bin/sh\n'
                    'if [ "$(pgrep hyperion | wc -l)" -eq 1 ]\n'
                    'then systemctl restart hyperion; fi\n'
                    'while true\n'
                    'do STEAMCHECK="$(pgrep steamlink)"\n'
                    'if [ ! "$STEAMCHECK" ]\n'
                    'if [ -f "openvt" ]\n'
                    'then openvt -c 7 -s -f clear\n'
                    'systemctl start mediacenter; fi\n'
                    'else systemctl start kodi\n'
                    'done')
        outfile.close()
main()
