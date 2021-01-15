from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
from apiclient.discovery  import build

# from __future__ import print_function
#googleapiclient.discovery
#
# from httplib2 import Http
# from oauth2client import file, client, tools
# from oauth2client.contrib import gce
# from apiclient.http import MediaFileUpload
# import numpy as np
# import pandas as pd
# from pandas import ExcelWriter
#
# import pathlib
# from pathlib import Path
# import io
# import glob
# import itertools
# import shutil
# import openpyxl
# from openpyxl import load_workbook
# from openpyxl.utils.dataframe import dataframe_to_rows
# from openpyxl.chart import (
#     LineChart,
#     Reference,
#     Series
# )
#
# import random
# import time
# from time import sleep
# import datetime
# import csv

from updatefile import update_file
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly', 'https://www.googleapis.com/auth/drive']

# SERVICE = build('drive', 'v3', http=creds.authorize(Http()))

# filename: your assigned filename to your Excel file .
# source: the absolute directory / file path of the Excel file in your computer
# folder id: the GDrive ID of the destination folder. You can dynamically get this from the getFolderfromGDrive method
# ---------------------------------------
# GDrive API: Upload files to Google Drive
# ---------------------------------------


def updatefile(filepath):
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentiala.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))

    service1 = build('drive', 'v2', credentials=creds)
    file_id = input("\nSelect file ID from the list: ") # '1QM2FWBUoNPtjW1IAziKZZzKC9qwtdgJf' #'1t-IAThW_3WCADG9ajif3ul23L4TAh6cq'
    # filepath = input("Enter file name with extension e.g. (myfile.xlsx): ")#'hyda.xlsx'
    filename = filepath.split('.')
    x, y = filename
    
    if file_id and filepath:
        print(x,y)
        update_file(service1, file_id, x, x, '[*/*]', './docs/'+filepath, 'name') # update existing file in google drive
    else:
        print("Must provide file ID and file name")

# if __name__ == '__main__':
#     updatefile()