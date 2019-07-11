from googleapiclient.discovery import build
from google.oauth2 import service_account
from apiclient.http import MediaFileUpload
from apiclient import errors
import mimetypes


SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = '/etc/drive-api-service-key.json'

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('drive', 'v3', credentials=creds)


def get_mime_type(file_name):
	mimetypes.init()
	file_ext = '.' + file_name.split('.')[-1]
	return mimetypes.types_map[file_ext.lower()]



def disable_copy_download(file_id):
	try:
		p = {
			'type': 'anyone',
			'role': 'reader',
		}
		service.files().update(fileId=file_id, body={'copyRequiresWriterPermission': True}).execute()
		return 'Copy & Download Permisson Disabled: ' + file_id
	except:
		return 'err'


def update_permission(file_id):
	perm = {
		'type': 'anyone',
		'role': 'reader',
	}
	try:
		return service.permissions().create(fileId=file_id, body=perm, fields='id').execute()
	except:
		return 'err'


def upload_tst(file_name):
	file_metadata = {
		'name': file_name,
	}
	mime_type = get_mime_type(file_name)
	media = MediaFileUpload(file_name, mimetype=mime_type)
	file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
	file_id = file.get('id')
	print('File ID: %s' % file.get('id'))
	print('update_permission', update_permission(file_id))
	print('disable_copy_download', disable_copy_download(file_id))




upload_tst('p.PNG')
