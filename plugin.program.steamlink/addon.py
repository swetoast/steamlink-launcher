"""Steamlink Launcher for OSMC"""
import os
import xbmc
import xbmcgui
import xbmcaddon

__plugin__ = "Steamlink"
__author__ = "Toast"
__url__ = "https://github.com/swetoast/steamlink-launcher/"
__git_url__ = "https://github.com/swetoast/steamlink-launcher/"
__credits__ = "Ludeeus, Slouken, sgroen88, ToiletSalad"
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
# installation part
install_on_libre () {
kodi-send --action="Notification(Installing Steamlink, Please wait while installing Steamlink and packages.. this might take awhile,1500)"
   mkdir -p /storage/steamlink
   mkdir -p /storage/steamlink/overlay_work
   mkdir -p /storage/steamlink/lib
   mv /storage/steamlink/udev/rules.d/55-steamlink.rules /storage/.config/udev.rules.d/55-steamlink.rules
wget https://raw.githubusercontent.com/swetoast/steamlink-launcher/dev/libreelec_additonal/60-steam-input.rules -O /storage/.config/system.d/storage-steamlink-udev-rules.d.mount
   systemctl enable storage-steamlink-udev-rules.d.mount
   udevadm trigger
wget "$(wget -q -O - http://media.steampowered.com/steamlink/rpi/public_build.txt)" -O /storage/steamlink/steamlink.tar.gz
   tar -zxf /storage/steamlink/steamlink.tar.gz
   rm /storage/steamlink/steamlink.tar.gz
   mkdir /storage/raspbian
   wget https://downloads.raspberrypi.org/raspbian_full_latest -O /storage/raspbian/raspbian-stretch-full.zip
   unzip /storage/raspbian/raspbian-stretch-full.zip
   mkdir /storage/raspbian/lib
   mount -o loop,ro,offset=50331648 -t ext4  /storage/raspbian/raspbian-stretch-full.zip
   cd /storage/raspbian/lib
   for i in libpng16.so.16 libicui18n.so.57 libicuuc.so.57 libicudata.so.57 libX11-xcb.so.1 libX11.so.6 libXext.so.6 libxcb.so.1 libxkbcommon-x11.so.0 libXau.so.6 libXdmcp.so.6 libxcb-xkb.so.1 libbsd.so.0; do cp "$(find -name $i)" .. ; done
   cd ..
   umount /storage/raspbian/lib
   rmdir /storage/raspbian/lib
   rm -r /storage/rasbian/
   mv /storage/raspbian/lib /storage/steamlink/lib
start_steamlink
}

install_on_osmc () {
kodi-send --action="Notification(Installing Steamlink, Please wait while installing Steamlink and packages,1500)"
sudo mv /home/osmc/.local/share/SteamLink/udev/rules.d/55-steamlink.rules /lib/udev/rules.d/55-steamlink.rules 
   sudo apt-get install curl gnupg libc6 xz-utils -y
wget http://media.steampowered.com/steamlink/rpi/steamlink.deb -O /tmp/steamlink.deb
   sudo dpkg -i /tmp/steamlink.deb
   rm -f /tmp/steamlink.deb
   sudo -u osmc steamlink
start_steamlink
}

install_on_os () {
case $(cat /etc/os-release | grep -oE "^NAME=\".*") in
 *LibreELEC*) install_on_libre ;;
      *OSMC*) install_on_osmc ;;
esac
}


start_steamlink () {
chmod 755 /tmp/steamlink-watchdog.sh
case $(cat /etc/os-release | grep -oE "^NAME=\".*") in
 *LibreELEC*) su -c "nohup /tmp/steamlink-watchdog.sh >/dev/null 2>&1 &" ;;
      *OSMC*) sudo su -c "nohup sudo openvt -c 7 -s -f -l /tmp/steamlink-watchdog.sh >/dev/null 2>&1 &" ;;
esac   

detect_steamlink () {
case $(cat /etc/os-release | grep -oE "^NAME=\".*") in
 *LibreELEC*) if [ -f "/storage/steamlink/steamlink" ]; then start_steamlink ; else install_on_os; fi ;;
      *OSMC*) if [ "$(which steamlink)" -eq "1" ]; then start_steamlink ; else install_on_os; fi ;;
esac   

}

detect_steamlink
""")

    with open('/tmp/steamlink-watchdog.sh', 'w') as outfile:
    outfile.write("""#!/bin/bash
# watchdog part
watchdog_osmc () {
sudo systemctl stop mediacenter
if [ "$HYPERIONFIX" = 1 ]; then
   if [ "$(pgrep hyperion)" ]; then sudo systemctl stop hyperion; fi
   if [ ! "$(pgrep hyperion)" ]; then sudo systemctl start hyperion; fi
fi
sudo -u osmc steamlink
sudo openvt -c 7 -s -f clear
sudo systemctl start mediacenter
}

watchdog_libre () {
systemctl stop kodi
if [ "$HYPERIONFIX" = 1 ]; then
   if [ "$(pgrep hyperion)" ]; then systemctl stop hyperion; fi
   if [ ! "$(pgrep hyperion)" ]; then systemctl start hyperion; fi
fi
systemctl stop kodi
/storage/steamlink/steamlink.sh &> /storage/steamlink/steamlink.log >/dev/null 2>&1 &
systemctl start kodi
}

os_detection () {
case $(cat /etc/os-release | grep -oE "^NAME=\".*") in
 *LibreELEC*) watchdog_libre ;;
      *OSMC*) watchdog_osmc ;;
esac
}

os_detection
""")
        outfile.close()
main()
