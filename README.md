#### This plugin adds a Google image search menu entry in Gnome Nautilus.

### Tested on:

* Arch

### Requirements:

* requests
* python-nautilus
* dbus-python
* python-requests

### Install the requirements:

##### Using the package manager provided by your distribution:

**Arch**

> sudo pacman -S  requests python-nautilus dbus-python python-requests

## Installation:

#### User

> python setup.py install

## Load the plugin
> Logoff/logon

Or
> restart gdm/lightdm

Or

> nautilus -q

> nautilus

##### Known Issues:

The requests are synchronous, so nautilus will lock until the image is uploaded (Watch out for big Images upload!!)
