import mimetypes,os,requests,urlparse,subprocess
from gi.repository import Gio, GObject, Nautilus


class GoogleImageSearchExtention(GObject.GObject , Nautilus.MenuProvider):
    GIMAGE_URL='https://images.google.com/searchbyimage/upload'

    def __init__(self):
        pass

    def _upload_to_browser(self,menu,file):

        subprocess.Popen(['notify-send','Uploading ' + file.get_name()])

        p= urlparse.urlparse(file.get_uri())

        path = os.path.abspath(os.path.join(p.netloc, p.path))
        path=path.replace('%20',' ')
        multipart = {'encoded_image':(path, open(path,'rb')),'image_content': ''}
        session = requests.session()
        session.headers['User-Agent'] = "Nautilus Google Reverse Image search plugin v0.1"
        response = session.post(self.GIMAGE_URL,files=multipart,allow_redirects=False)
        fetchUrl = response.headers['Location']
        subprocess.Popen(['notify-send','Upload Done ' + file.get_name()])
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
            item.connect('activate', self._upload_to_browser, file)

            return [item]