from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# pip install PyDrive # need to install this library to be able to upload files to google drive

folder_id = '1WQaO9--CvQbLuSukGT0MqbpcrI4VLmIM' # Drive Excel File ID
def uploadfile(path, file_name):
    try:
        gauth = GoogleAuth()
        # gauth.LocalWebserverAuth()
        # gauth.SaveCredentialsFile("credentials.txt") # save credentails to txt file  
        gauth.LoadCredentialsFile("credentials.txt")# authenticate from save file txt
        
        drive = GoogleDrive(gauth)    
        myFile = drive.CreateFile({'title':file_name, 'parents': [{'kind': "drive#fileLink",'id': folder_id}] }) #{'title':file_name, 'parents': [{'kind': "drive#fileLink",'id': folder_id}] }
        myFile.SetContentFile(path+file_name)
        myFile.Upload()

        print(f"\nFile: '{file_name}' Uploaded successfully!\n")
    except :
        print("There was an error upload files to G Drive")
        exit()
        



# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()
# drive = GoogleDrive(gauth)

# pip install PyDrive2

# folder_id = '1WQaO9--CvQbLuSukGT0MqbpcrI4VLmIM' # Drive Excel File ID
# file_name = "allchats.xlsx" # a file to upload to google drive




# def getworkbook():
#     doc = './docs/'
#     # filename = input("Enter File name: ")
#     workbook = xlsxwriter.Workbook(file_name + '.xlsx')
#     return workbook

# def get_sheetnames_xlsx(filepath=file_name):
#     wb = load_workbook(filepath, read_only=True, keep_links=False)
#     # print(wb.sheetnames)
#     return wb.sheetnames






    # myFile = drive.CreateFile({'title':file_name, 'parents': [{'kind': "drive#fileLink",'id': folder_id}] })
    # myFile.SetContentFile(file_name)
    # myFile.Upload()



