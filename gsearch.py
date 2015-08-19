from gi.repository import Gio, GObject, Nautilus
import dbus, os, requests, urlparse
from multiprocessing import Pool

class GoogleImageSearchExtention(GObject.GObject , Nautilus.MenuProvider):
    GIMAGE_URL='https://images.google.com/searchbyimage/upload'

    def __init__(self):
        pass

    def _upload_to_gsearch(self,file):
        p = urlparse.urlparse(file.get_uri())
        path = os.path.abspath(os.path.join(p.netloc, p.path))
        path = path.replace('%20',' ')
        multipart = {'encoded_image':(path, open(path,'rb')),'image_content': ''}
        session = requests.session()
        session.headers['User-Agent'] = "Nautilus Google Reverse Image search plugin v0.1"
        response = session.post(self.GIMAGE_URL,files=multipart,allow_redirects=False)
        fetchUrl = response.headers['Location']

    def _execute_command(self,menu,file):
        bus = dbus.SessionBus()
        bus_obj = bus.get_object("org.freedesktop.Notifications",
                                 "/org/freedesktop/Notifications")
        interface = dbus.Interface(bus_obj, "org.freedesktop.Notifications")

        interface.Notify("Nautilus", 0, "nautilus",
                         "Uploading %s" % file.get_name(),
                         "Your file is being uploaded",
                         [], [], 5000)

        pool = Pool(processes=1)
        fetchUrl = pool.apply_async(self._upload_to_gsearch,(file,))

        pool.close()
        interface.Notify("Nautilus", 0, "nautilus",
                         "Upload done",
                         "Your file %s was uploaded" % file.get_name(),
                         [], [], 5000)

        Gio.AppInfo.launch_default_for_uri(fetchUrl)


    def get_file_items(self, window, files):
        if len(files) != 1:
            return

        file = files[0]

        if "image/" in Gio.content_type_guess(file.get_name())[0]:
            item = Nautilus.MenuItem(
                name="SimpleMenuExtension::Show_File_Name",
                label="Search on Google Image",
                tip="Search %s" % file.get_name()
            )
            item.connect('activate', self._execute_command, file)

            return [item]