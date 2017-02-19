This plugin adds a Google image search menu entry in Gnome Nautilus.

**Tested on:**

* Ubuntu 15.04 with Unity

* Debian 8

* Fedora 25 (gnome-shell tested)

* Fedora 22

**Requirements:**

* requests

* nautilus-python python-requests nautilus-python

**Using the package manager provided by your distribution:**

**Debian-based**

> sudo apt-get install python-requests python-nautilus

**RHEL-based**

> sudo yum install python-requests nautilus-python

**Fedora 25**

> sudo dnf install python-requests nautilus-python python3-dbus

**Known Issues:**

The requests are synchronous, so nautilus will lock until the image is uploaded (Watch out for big Images upload!!)

**Installation:**

* Global

> put the file gsearch.py in /usr/share/nautilus-python/extensions/

* User

> * ~/.local/share/nautilus-python/extensions

* restart gdm/lightdm

or

> nautilus -q

> nautilus
