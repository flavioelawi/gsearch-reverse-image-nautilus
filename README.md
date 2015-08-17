This plugin adds a Google image search menu entry in Gnome Nautilus.

**Tested on:**

* Ubuntu 15.04 with Unity

* Fedora 22

**Requirements:**

* requests

* nautilus-python

**Requests**
> sudo pip install requests

or

> sudo apt-get install python-requests

**nautilus-python**

> sudo apt-get install nautilus-python

> sudo yum install nautilus-python

**Known Issues:**

The requests are sync, so nautilus will lock until the image is uploaded (Big image files warning!!)


**Installation:**

* put the file gsearch.py in /usr/share/nautilus-python/extensions/

* restart gdm/lightdm

or

> nautilus -q

> nautilus
