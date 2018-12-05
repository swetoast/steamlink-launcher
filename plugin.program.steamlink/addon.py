

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57

"""Steamlink Launcher for OSMC"""
import os
import xbmc
import xbmcgui
import xbmcaddon

__plugin__ = "steamlink"
__author__ = "toast"
__url__ = "-/"
__git_url__ = "-"
__credits__ = "toast"
__version__ = "0.0.1"

dialog = xbmcgui.Dialog()
addon = xbmcaddon.Addon(id='plugin.program.steamlink')


def main():
    """Main operations of this plugin."""
    if os.path.isfile("/tmp/steamlink-launcher.sh"):
        output = os.popen("/tmp/steamlink-launcher.sh").read()
    else:
        create_files()
        output = os.popen("/tmp/steamlink-launcher.sh").read()
    dialog.ok("Starting Steamlink", output)
    #print output


def create_files():
    """Creates bash files to be used for this plugin."""
    with open('/tmp/steamlink-launcher.sh', 'w') as outfile:
        outfile.write('#!/bin/bash\n'
                      'if [ "$HYPERIONFIX" = 1 ]; then if [ "$(pgrep hyperion)" ]; '
                      'then sudo service hyperion stop; fi; fi\n'
                      'sleep 8\n'
                      'if [ "$HYPERIONFIX" = 1 ]; then if [ ! "$(pgrep hyperion)" ]; then '
                      'sudo service hyperion start; fi; fi\n'
                      'while true; do VAR1="$(pgrep steamlink)"; if [ ! "$VAR1" ]; then\n'
                      'sudo openvt -c 7 -s -f clear; sudo su -c '
                      '"sudo systemctl restart mediacenter &" &\n'
                      'exit\n'
                      'else sleep 2; fi\n'
                      'done\n'
                      'exit')
        outfile.close()
    with open('/tmp/steamlink-watchdog.sh', 'w') as outfile:
        outfile.write('#!/bin/bash\n'
                      'sudo openvt -c 7 -s -f clear\n'
                      'sudo su osmc -c "sh /tmp/steamlink_watchdog.sh &" &\n'
                      'sudo chown osmc:osmc /usr/bin/steamlink\n'
                      'sudo su osmc -c "nohup openvt -c 7 -f -s steamlink >/dev/null 2>&1 &" &\n'
                      'sudo openvt -c 7 -s -f clear\n'
                      'sleep 0.5; sudo su -c "systemctl stop mediacenter &" &\n'
                      'exit')
        outfile.close()
main()
