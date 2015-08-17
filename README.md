This plugin adds a Google image search menu entry in Gnome Nautilus.

**Installation:**
* put the file gsearch.py in /usr/share/nautilus-python/extensions/
* restart gdm/lightdm

or

> nautilus -q

> nautilus


Tested on Ubuntu 15.04 with Unity

**Requirements:**
* requests

> sudo pip install requests

or

> sudo apt-get install python-requests

**Known Issues:**

The requests are sync, so nautilus will lock until the image is uploaded (Big image files warning!!)
