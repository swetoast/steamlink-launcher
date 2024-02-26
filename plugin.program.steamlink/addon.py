import os
import subprocess
import xbmc
import xbmcaddon
import xbmcgui
import urllib.request
import shutil

addon = xbmcaddon.Addon()

# Path to the Steamlink deb package
steamlink_url = "http://media.steampowered.com/steamlink/rpi/latest/steamlink.deb"

# List of prerequisite packages
packages = ["gnupg", "curl", "libgles2", "libegl1", "libgl1-mesa-dri"]

def is_installed(package):
    try:
        subprocess.run(["dpkg", "-s", package], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def install_package(package):
    # Create a progress dialog
    progress_dialog = xbmcgui.DialogProgress()
    progress_dialog.create(f'Installing {package}', 'Please wait...')
    
    try:
        # Install the package
        subprocess.run(["sudo", "apt-get", "install", "-y", package], check=True)
        progress_dialog.update(100, f'Installing {package}', 'Installation complete.')
        xbmcgui.Dialog().ok('Success', f'The package {package} has been installed successfully.')
    except subprocess.CalledProcessError:
        xbmcgui.Dialog().ok('Error', f'An error occurred while installing the package {package}.')
    finally:
        # Close the progress dialog
        progress_dialog.close()

def is_steamlink_installed():
    try:
        subprocess.run(["dpkg", "-s", "steamlink"], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def install_steamlink():
    # Create a progress dialog
    progress_dialog = xbmcgui.DialogProgress()
    progress_dialog.create('Installing Steamlink', 'Please wait...')
    
    try:
        # Custom download function with progress
        def download_with_progress(url, dest):
            with urllib.request.urlopen(url) as response, open(dest, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
                progress_dialog.update(50, 'Installing Steamlink', 'Download complete.')
                print(f"Downloaded {os.path.getsize(dest)} bytes")

        # Download the Steamlink package
        download_with_progress(steamlink_url, "/tmp/steamlink.deb")
        xbmcgui.Dialog().ok('Success', 'The Steamlink package has been downloaded successfully.')
        
        # Install the Steamlink package
        subprocess.run(["sudo", "dpkg", "-i", "/tmp/steamlink.deb"], check=True)
        progress_dialog.update(100, 'Installing Steamlink', 'Installation complete.')
        xbmcgui.Dialog().ok('Success', 'The Steamlink package has been installed successfully.')
        
        # Remove the Steamlink package from /tmp
        os.remove("/tmp/steamlink.deb")
        xbmcgui.Dialog().ok('Success', 'The Steamlink package has been removed from /tmp.')
    except Exception as e:
        xbmcgui.Dialog().ok('Error', f'An error occurred: {str(e)}')
    finally:
        # Close the progress dialog
        progress_dialog.close()

for package in packages:
    if not is_installed(package):
        xbmcgui.Dialog().ok('Missing Prerequisite', f'The package {package} is not installed. Installing now...')
        install_package(package)

if not is_steamlink_installed():
    xbmcgui.Dialog().ok('Missing Prerequisite', 'Steamlink is not installed. Installing now...')
    install_steamlink()
else:
    xbmcgui.Dialog().ok('Already Installed', 'Steamlink is already installed.')

# Stop Kodi
subprocess.run(["sudo", "systemctl", "stop", "mediacenter"], check=True)

# Launch Steamlink
subprocess.run(["sudo", "-u", "osmc", "steamlink"], check=True)
subprocess.run(["openvt", "-c", "7", "-s", "-f", "clear"], check=True)

# Start Kodi
subprocess.run(["sudo", "systemctl", "start", "mediacenter"], check=True)
