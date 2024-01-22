[![GitHub Release][releases-shield]][releases]
[![GPL license](https://img.shields.io/badge/License-GPL-blue.svg?style=for-the-badge)](LICENSE.md)
![Project Maintenance][maintenance-shield1]
[![Contributors][contributors-shield]][contributors]
<a href="https://liberapay.com/Toast/donate"><img alt="Donate using Liberapay" align="right" align="top" src="https://liberapay.com/assets/widgets/donate.svg"></a>
# Steamlink Launcher for OSMC

  [Installation](#installation) | [Want to contribute](#want-to-contribute) | [Acknowledgement](#acknowledgement) |  [Credits](#credits) | [Donator](#donator) | [Got issues](#got-issues) | [License](#license) | [Links](#links)



This launcher is exclusively designed for the Open Source Media Center (OSMC). It facilitates the installation of two scripts that operate and manage Steamlink. Please note that this is still in beta testing, so any performance-related issues should be reported directly to Valve. While I'm here to address issues related to the launcher, I won't be able to assist with performance problems - these should be directed to Valve.

## Installation

1. Download the [zip](https://github.com/swetoast/steamlink-launcher/releases) file of the launcher and install it using Kodi.
2. The add-on will automatically install Steamlink. If wakeuponlan is installed, it is also supported. To use it, create a file in the home directory named `.wakeup` and add your MAC ID using the command `nano /home/osmc/.wakeup`.
NOTE: Please note that this add-on requires Kodi version 19 to be installed as it uses Python 3.

## Want to contribute


Make sure to lint your code so its proper then submit it via PR here on the tracker.

## Acknowledgement

© 2023 Valve Corporation. All rights reserved. Valve, Steam Link and Steam are trademarks and/or 
registered trademarks of Valve Corporation in the US and other countries. 

## Credits

Here is a full list of people that helped out on this project

* [Ludeeus](https://github.com/ludeeus) - code clean up
* [Valve/Slouken](https://github.com/swetoast/steamlink-launcher/commits?author=slouken) - for additional code donations and for adding lib replacement for OSMC
* [sgroen88](https://github.com/sgroen88) - adding shell execution to the script
* [ninfur](https://github.com/ninfur) - fixing the watchdog
* [Sam Crawley](https://github.com/sam-crawley) - watchdog rewrite 

## Donator

Here is a list of people that donated to this project, super thankful for people donating.

* Moritz Goltdammer

## Got issues

* If you encounter a bug associated with the launcher, please submit an issue.
* If you experience problems related to OSMC, such as the Pi crashing or issues with overlays, initiate a discussion on the OSMC Forums.
* If Steamlink starts but you’re facing difficulties, seek support on the [Steam Forums](https://steamcommunity.com/app/353380/discussions/).
* 
To minimize clutter on the issue tracker with OSMC-related issues, please remember that this launcher primarily initiates Steamlink and has minimal interaction with the operating system.
When reporting a bug, it's crucial to include logs. You can obtain these via the command line using `grab-logs -A`.
If you find that these fixes are outdated but everything is functioning correctly, please provide an update on the issue tracker.

### Known Workarounds:

* if you get a black stream from your Steam host, you need `dtoverlay=vc4-fkms-v3d,cma-512` instead of `dtoverlay=vc4-kms-v3d` in `config.txt` this workaround is for Raspberry Pi 4 (only)

## License

Steamlink Launcher is licensed under GPL2

## Links

* [Valve Forums](https://steamcommunity.com/app/353380/discussions/6/)
* [OSMC Forums](https://discourse.osmc.tv/t/regarding-steamlink/76800)

[contributors-shield]: https://img.shields.io/github/contributors/swetoast/steamlink-launcher.svg?style=for-the-badge
[contributors]: https://github.com/swetoast/steamlink-launcher/graphs/contributors/
[license-shield]: https://img.shields.io/github/license/swetoast/steamlink-launcher.svg?style=for-the-badge
[maintenance-shield1]: https://img.shields.io/badge/maintainer-Toast%20%40swetoast-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/swetoast/steamlink-launcher.svg?style=for-the-badge
[releases]: https://github.com/swetoast/steamlink-launcher/releases
