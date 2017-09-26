#### This plugin adds a Google image search menu entry in Gnome Nautilus.

### Tested on:

* Ubuntu from 14.04 to 17.10 (Gnome-shell - unity-shell)

* Debian 8

* Fedora 25 (gnome-shell tested)

* Fedora 22

###Requirements:

* requests

* nautilus-python python-requests nautilus-python

### Install the requirements:

#####Using the package manager provided by your distribution:

**Debian-based**

> sudo apt-get install python-requests python-nautilus

**RHEL-based**

> sudo yum install python-requests nautilus-python

**Fedora 25**

> sudo dnf install python-requests nautilus-python python3-dbus

## Installation:

#### Global

> put the file gsearch.py in /usr/share/nautilus-python/extensions/

#### User
> python setup.py install

* or
>  ~/.local/share/nautilus-python/extensions


## Load the plugin
> restart gdm/lightdm

or

> nautilus -q

> nautilus

##### Known Issues:

The requests are synchronous, so nautilus will lock until the image is uploaded (Watch out for big Images upload!!)
