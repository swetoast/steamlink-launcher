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
create_files()
output = os.popen("sh /tmp/steamlink-launcher.sh").read()
dialog.ok("Starting Steamlink...", output)

def create_files():
"""Creates bash files to be used for this plugin."""
with open('/tmp/steamlink-launcher.sh', 'w') as outfile:
outfile.write("""#!/bin/sh
os_detection () {
if [ "$(cat "/etc/os-release" | grep "OSMC" | wc - l)" -eq 1 ]
   then detect_steamlink
   else install_steamlink
fi
}

detect_steamlink () {
if [ "$(which steamlink)" -eq "1" ]; then start_steamlink ; else install_on_os; fi
}

install_on_os () {
if [ "$(cat "/etc/os-release" | grep "OSMC" | wc - l)" -eq 1 ]
   then install_on_osmc
   else install_on_libre
fi
}

start_steamlink () {
if [ "$(cat "/etc/os-release" | grep "OSMC" | wc - l)" -eq 1 ]
   then watchdog_osmc
   else watchdog_libre
fi
}

install_on_libre () {
kodi-send --action="Notification(Installing Steamlink, Please wait while installing Steamlink and packages,1500)"
   mkdir -p /storage/steamlink
   mkdir -p /storage/steamlink/overlay_work
   mkdir -p /storage/steamlink/libs
   mkdir -p /storage/.config/system.d/
wget https://raw.githubusercontent.com/swetoast/steamlink-launcher/dev/libreelec_additonal/60-steam-input.rules -O /storage/.config/system.d/storage-steamlinkudev-rules.d.mount
wget https://raw.githubusercontent.com/swetoast/steamlink-launcher/dev/libreelec_additonal/55-steam-input.rules -O /storage/.config/system.d/storage-steamlinkudev-rules.d.mount
   mount -t overlay overlay -o lowerdir=/lib/udev/rules.d,upperdir=/storage/steamlink/udev/rules.d/,workdir=/storage/steamlink/overlay_work /lib/udev/rules.d
   udevadm trigger
systemctl enable storage-steamlink-udev-rules.d.mount
wget "$(wget -q -O - http://media.steampowered.com/steamlink/rpi/public_build.txt)" -O /storage/steamlink/steamlink.tar.gz
   tar -zxf /storage/steamlink/steamlink.tar.gz
   rm /storage/steamlink/steamlink.tar.gz
   wget REPLACEME -O /storage/steamlink/lib.zip
   unzip /storage/steamlink/lib.zip
   rm /storage/steamlink/lib.zip
   usermod -a -G input,plugdev root
start_steamlink
}

install_on_osmc () {
if [ "$(id -u)" != "0" ]; then exec /usr/bin/sudo /bin/bash "$0"; fi # root check
kodi-send --action="Notification(Installing Steamlink, Please wait while installing Steamlink and packages,1500)"
wget https://raw.githubusercontent.com/swetoast/steamlink-launcher/dev/libreelec_additonal/55-steam-input.rules -O /lib/udev/rules.d/55-steamlink.rules
   apt-get install curl gnupg libc6 xz-utils -y
wget http://media.steampowered.com/steamlink/rpi/steamlink.deb -O /tmp/steamlink.deb
   dpkg -i /tmp/steamlink.deb
   rm -f /tmp/steamlink.deb
   sudo -u osmc steamlink
start_steamlink
}

watchdog_osmc () {
if [ "$(id -u)" != "0" ]; then exec /usr/bin/sudo /bin/bash "$0"; fi # root check
systemctl stop mediacenter
if [ "$HYPERIONFIX" = 1 ]; then
   if [ "$(pgrep hyperion)" ]; then systemctl stop hyperion; fi
   if [ ! "$(pgrep hyperion)" ]; then systemctl start hyperion; fi
fi
sudo -u osmc steamlink
openvt -c 7 -s -f clear
systemctl start mediacenter
}

watchdog_libre () {
systemctl stop kodi
if [ "$HYPERIONFIX" = 1 ]; then
   if [ "$(pgrep hyperion)" ]; then systemctl stop hyperion; fi
   if [ ! "$(pgrep hyperion)" ]; then systemctl start hyperion; fi
fi
systemctl stop kodi
/storage/steamlink/steamlink &> /storage/steamlink/steamlink.log >/dev/null 2>&1 &
systemctl start kodi
}
""")
        outfile.close()
main()
