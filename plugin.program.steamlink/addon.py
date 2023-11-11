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
__version__ = "0.0.13"

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
        outfile.write("""#!/bin/bash
chmod 755 /tmp/steamlink-watchdog.sh
sudo openvt -c 7 -s -f clear
sudo su -c "nohup sudo openvt -c 7 -s -f -l /tmp/steamlink-watchdog.sh >/dev/null 2>&1 &"
""")
        outfile.close()
    with open('/tmp/steamlink-watchdog.sh', 'w') as outfile:
        outfile.write("""#!/bin/bash
        
check_pkgs_installed() {
	output=$(dpkg --list $@ 2>&1)
}

req_packages="gnupg curl libgles2 libegl1 libgl1-mesa-dri"

if ! check_pkgs_installed $req_packages; then        
	sudo apt update
	for pkg in $req_packages; do
	
		if ! check_pkgs_installed $pkg; then 
			kodi-send --action="Notification(Downloading and installing Steamlink dependencies ($pkg)... ,3000)"
			sudo apt install $pkg -y
		fi
	done
fi

if [ "$(which steamlink)" = "" ]; then
    kodi-send --action="Notification(Downloading and installing Steamlink Application... ,3000)" 
    curl -o /tmp/steamlink.deb -#Of http://media.steampowered.com/steamlink/rpi/latest/steamlink.deb
    sudo dpkg -i /tmp/steamlink.deb
    rm -f /tmp/steamlink.deb
fi

if [ -f "/home/osmc/.wakeup" ]; then
	if ! check_pkgs_installed wakeonlan; then
		sudo apt install wakeonlan -y;
	fi
   
   /usr/bin/wakeonlan "$(cat "/home/osmc/.wakeup")"
fi

if [ -x "/home/osmc/steamlink/startup.sh" ]
   then sudo -u osmc /home/osmc/steamlink/startup.sh
fi

systemctl stop mediacenter
if [ "$(systemctl is-active hyperion.service)" = "active" ]; then systemctl restart hyperion; fi
sudo -u osmc steamlink
openvt -c 7 -s -f clear

if [ -x "/home/osmc/steamlink/shutdown.sh" ]
   then sudo -u osmc /home/osmc/steamlink/shutdown.sh
fi

systemctl start mediacenter
""")
        outfile.close()
main()
