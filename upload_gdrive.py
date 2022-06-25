from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import httplib2
from httplib2 import socks

gauth = GoogleAuth()
http = httplib2.Http(proxy_info=httplib2.ProxyInfo(
    socks.PROXY_TYPE_HTTP, '10.59.66.1', 8080))
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

upload_file_list = ['F:/KY/tutela/2.pdf']

for upload_file in upload_file_list:
    name_file = upload_file.replace('F:/KY/tutela/', '')
    gfile = drive.CreateFile(
        {'parents': [{'id': '1Ihqj-AZaCAwdAVtwMRjNl7TatLQCB7QA'}], 'title': name_file})

    gfile.SetContentFile(upload_file)
    gfile.Upload(param={"http": http})
