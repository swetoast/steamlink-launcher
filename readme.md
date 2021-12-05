[![GitHub Release][releases-shield]][releases]
[![GPL license](https://img.shields.io/badge/License-GPL-blue.svg?style=for-the-badge)](LICENSE.md)
![Project Maintenance][maintenance-shield1]
[![Contributors][contributors-shield]][contributors]
<a href="https://liberapay.com/Toast/donate"><img alt="Donate using Liberapay" align="right" align="top" src="https://liberapay.com/assets/widgets/donate.svg"></a>
# Steamlink Launcher for OSMC

**NOTE: Steamlink is broken as of Kodi 19 (for further info see known issues below)**

This is a laucher only for Open Source Mediacenter (OSMC), the launcher installs two scripts that run and handles Steamlink remember this is all beta so report performance issues to Valve and launcher issues here, i will not handle performance issues at all will refer to Valve for that.

## Installation

* download the [zip](https://github.com/swetoast/steamlink-launcher/releases) of the launcher and install it via Kodi
* the addon installs Steamlink automatically, wakeuponlan is also supported if its installed all you have to do is create a file in home directory called .wakeup and add your MAC id `nano /home/osmc/.wakeup`
* This addon needs Kodi version **19** to be installed since its **python 3**.

## Want to contribute


Make sure to lint your code so its proper then submit it via PR here on the tracker.

## Acknowledgement

© 2021 Valve Corporation. All rights reserved. Valve, Steam Link and Steam are trademarks and/or 
registered trademarks of Valve Corporation in the US and other countries. 

## Credits

Here is a full list of people that helped out on this project

* [Ludeeus](https://github.com/ludeeus) - code clean up
* [Valve/Slouken](https://github.com/swetoast/steamlink-launcher/commits?author=slouken) - for additional code donations and for adding lib replacement for OSMC
* [sgroen88](https://github.com/sgroen88) - adding shell execution to the script

## Donator

Here is a list of people that donated to this project, super thankful for people donating.

* Moritz Goltdammer

## Got issues

* if the bug is related to the launcher, file an issue
* if its related to OSMC like crashing the pi adding overlays etc start a thread on OSMC Forums.

this makes it less spammy on the issue tracker with OSMC issues again this launcher does very little on a OS level all it does is starts steamlink.

Known issues:

if these fixes are out of date and its working report back on the tracker.

RPI4 crashes in kernel with error message: `vc4_hdmi fef05700.hdmi: ASoC: error at snd_soc_dai_startup on fef05700.hdmi`

Status: **Reported**

* https://discourse.osmc.tv/t/steamlink-issues-with-kodi-19-and-bootloader-4-0-0/89990/7
* https://github.com/swetoast/steamlink-launcher/issues/37
  

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
