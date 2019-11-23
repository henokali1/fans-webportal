from googleapiclient.discovery import build
from google.oauth2 import service_account
from apiclient.http import MediaFileUpload
from apiclient import errors
import mimetypes


SCOPES = ['https://www.googleapis.com/auth/drive',
          'https://www.googleapis.com/auth/documents',
          'https://www.googleapis.com/auth/gmail.readonly',
        ]

SERVICE_ACCOUNT_FILE = '/etc/fans-drive-drive-service-e09581e98544.json'
FILE_PATH = '/home/ubuntu/fansWebportalEnv/fans-webportal/media/'

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('drive', 'v3', credentials=creds)
doc_service = build('docs', 'v1', credentials=creds)
gmail_service = build('gmail', 'v1', credentials=creds)

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

def save_on_drive(file_name):
    file_metadata = {
        'name': file_name,
    }
    mime_type = get_mime_type(file_name)
    media = MediaFileUpload(file_name, mimetype=mime_type)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    file_id = file.get('id')
    print('File ID: %s' % file.get('id'))
    # print('update_permission', update_permission(file_id))
    # print('disable_copy_download', disable_copy_download(file_id))
    return file_id

def list_files():
    r = service.files().list(pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = r.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{1} - {0}'.format(item['name'], item['id']))

def delete_drive_file(file_id):
    """
    Permanently delete a file, skipping the trash.

    Args:
    file_id: ID of the file to delete.
    """
    try:
        service.files().delete(fileId=file_id).execute()
        print(i, 'Deleted')
    except:
        print('Err')


def prepReq(data_dict):
	requests = []
	for i in data_dict:
		requests.append(
			{
				'replaceAllText': {
					'containsText': {
						'text': '{{' + i + '}}',
						'matchCase':  'true'
					},
					'replaceText': data_dict[i],
				}}
			)
	return requests


def createDoc():
	title = 'My Document'
	body = {
		'title': title
	}

	doc = doc_service.documents().create(body=body).execute()
	print('Created document with title: {0}'.format(doc.get('title')))


def shareDocEmail(file_id, email):
    perm = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': email,
    }
    try:
        return service.permissions().create(fileId=file_id, body=perm, fields='id').execute()
    except:
        return 'err'


def change_name(document_id):
    first_name = 'FN'
    last_name = 'LN'
    gender = 'M'

    requests = [
         {
            'replaceAllText': {
                'containsText': {
                    'text': '{{first_name}}',
                    'matchCase':  'true'
                },
                'replaceText': first_name,
            }},
            {
            'replaceAllText': {
                'containsText': {
                    'text': '{{last_name}}',
                    'matchCase':  'true'
                },
                'replaceText': last_name,
            }}
    ]

    result = doc_service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()


def edit_doc(document_id, requests):
	return doc_service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()


dd = {'first_name': 'henok', 'last_name':'Ali', 'gender':'M'}

req = prepReq(dd)

print(edit_doc("1lIqBtLUWeNkogkikbk43ExToGfI53jg6g6YbXlWPGrI", req))


def tst_gmail():
    # Call the Gmail API
    results = gmail_service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string())}

create_message('me', 'henokali1@gmail.com', 'subject', 'msg')