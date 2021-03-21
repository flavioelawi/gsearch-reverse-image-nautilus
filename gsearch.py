#!/usr/bin/env python

import base64
import logging
import os
import sys
from urllib.parse import urlparse

import dbus
import requests
from gi.repository import Gio, GObject, Nautilus

logger = logging.getLogger(__name__)


class GoogleImageSearchExtention(GObject.GObject , Nautilus.MenuProvider):
    def __init__(self):
        logger.debug=("Initializing Image Search extention...")
        self.SERVICE_MAPPING = {
            "Google": {
                "url": "https://images.google.com/searchbyimage/upload",
                "label": "Search on Google Image",
                "requester": self.gsearch
            },
        }
        self.session = requests.session()
        self.session.headers['User-Agent'] = "Nautilus Google Reverse Image search plugin v1.1"

    def _upload_to_browser(self, menu, _file, service):
        bus = dbus.SessionBus()
        bus_obj = bus.get_object("org.freedesktop.Notifications",
                                 "/org/freedesktop/Notifications")
        interface = dbus.Interface(bus_obj, "org.freedesktop.Notifications")
        interface.Notify("Nautilus", 0, "nautilus",
                         "Uploading %s" % _file.get_name(),
                         "Your file is being uploaded",
                         [], [], 5000)
        requester = self.SERVICE_MAPPING.get(service)["requester"]
        response_url = requester(_file)
        interface.Notify("Nautilus", 0, "nautilus",
                         "Upload done",
                         "Your file %s was uploaded" % _file.get_name(),
                         [], [], 5000)
        Gio.AppInfo.launch_default_for_uri(response_url)

    def get_file_items(self, window, files):
        for _file in files: 
            if "image/" in Gio.content_type_guess(_file.get_name())[0]:
                items = []
                for service in self.SERVICE_MAPPING:
                    item = Nautilus.MenuItem(
                        name="SimpleMenuExtension::Show_File_Name",
                        label=self.SERVICE_MAPPING[service]["label"],
                        tip="Search %s" % _file.get_name()
                    )
                    item.connect('activate', self._upload_to_browser, _file, service)
                    items.append(item)
        return items

    def _get_file_path(self, _file):
        p = urlparse(_file.get_uri())
        file_path = os.path.abspath(os.path.join(p.netloc, p.path))
        file_path = file_path.replace('%20',' ')
        return file_path

    def gsearch(self, _file):
        file_path = self._get_file_path(_file)
        multipart = {
            'encoded_image': open(file_path,'rb')
        }
        response = self.session.post(
            self.SERVICE_MAPPING.get("Google")["url"],
            files=multipart,
            allow_redirects=False
        )
        return response.headers['Location']

