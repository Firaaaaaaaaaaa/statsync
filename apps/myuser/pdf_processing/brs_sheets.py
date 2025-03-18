import os
import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import uuid
import requests

# Path absolut untuk file kredensial
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, "pdf_processing", "brs-sheets-api.json")

SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

# Pastikan file ada sebelum digunakan
if not os.path.exists(SERVICE_ACCOUNT_FILE):
    raise FileNotFoundError(f"File kredensial tidak ditemukan: {SERVICE_ACCOUNT_FILE}")

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Klien Google Sheets
client = gspread.authorize(creds)

def authenticate_drive():
    """
    Mengautentikasi Google Drive API.
    """
    return build('drive', 'v3', credentials=creds)

def get_access_token():
    creds.refresh(Request())  # Refresh kredensial secara langsung
    return creds.token  # Ambil token terbaru


def get_sheets_gid(drive_file_id):
    """
    Ambil daftar GID untuk setiap sheet di Google Sheets.
    """
    try:
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{drive_file_id}?fields=sheets(properties(sheetId,title))"
        
        # Ambil access token langsung dari kredensial
        access_token = get_access_token()

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json"
        }

        response = requests.get(url, headers=headers)
        print(response.json())  # Debugging, lihat apakah data muncul

        if response.status_code == 200:
            data = response.json()
            return {sheet["properties"]["title"]: sheet["properties"]["sheetId"] for sheet in data["sheets"]}
        else:
            print(f"⚠️ Gagal mendapatkan GID. Status: {response.status_code}, Response: {response.text}")
            return {}
    except Exception as e:
        print(f"Error fetching GID: {str(e)}")
        return {}



def get_sheets_preview(drive_file_id):
    """
    Mengambil daftar sheet dan link pratinjau dari Google Sheets.
    """
    try:
        spreadsheet = client.open_by_key(drive_file_id)
        sheets = spreadsheet.worksheets()

        preview_links = [{"name": sheet.title, "link": f"https://docs.google.com/spreadsheets/d/{drive_file_id}/edit?gid={sheet.id}#gid={sheet.id}"} for sheet in sheets]
        
        return preview_links
    except Exception as e:
        print(f"Error fetching sheets: {e}")
        return []
