from posix import listdir
from skpy import Skype
from getpass import getpass
from extractor import allgchistory, singlegchistory
import re
from quickstart import updatefile
from uploadtogdrive import uploadfile
import os.path
from os import path
from os.path import isfile, join, isdir
from skpy.core import SkypeObj, SkypeEnum, SkypeApiException, SkypeAuthException


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    sentinel = input("\nPress 1 to proceed Generate GC History:\nPress 3 to Upload or Update file in G Drive:\nPress "
                     "0 to exit: ")
    login = False
    gcid = []
    sk = None
    while sentinel != '0':
        if sentinel == '1':

            isfolderexists()  # auto create docs folder excel file will have in this folder

            if not login:
                print('\nEnter password to login:\n')
                try:
                    sk = Skype(input("Enter username: "), getpass())
                    login = True
                    if sk.conn.connected:
                        gcid = sk.chats.recent()

                except SkypeAuthException as auth:
                    print("Authentications with username and password : ", auth)
                    return

            groupid(gcid)

            param = input("Enter GC ID, or Press Enter to Generate all GC History: ")

            try:
                if param:
                    singlegchistory(sk, gcid, param)
                    del gcid[param]
                elif not param:
                    allgchistory(sk, gcid)
            except SkypeApiException as e:
                print("There was an error: ", e)
                # grouped(gcid)


        elif sentinel == '3':

            updateuploadinGDrive()

        # elif sentinel == "0":
        #     exit()

        sentinel = input(
            "\nPress 1 to proceed Generate GC History:\nPress 3 to Upload or Update file in G Drive:\nPress 0 to exit: ")


def groupid(gcid):
    for x in gcid:
        if re.findall("19", x):
            print("Group Name: ", gcid[x].topic, "Group ID: ", x)
    print("\n")


def updateuploadinGDrive():
    isfolderexists()  # auto create docs folder excel file will have in this folder
    folder_content = [f for f in listdir('./docs') if isfile(join('./docs/', f))]

    os.system('cls' if os.name == 'nt' else 'clear')
    print(len(folder_content), ' docs folder content')
    if len(folder_content) <= 0:
        print("There are no files in docs folder")
        return

    uploadupdate = input("\nPress 1 to upload file to G Drive,\nPress 3 to Update file in G Drive,\nPress 0 to exit: ")

    if uploadupdate == "1":
        filename = input("Enter file name: ")
        if filename:
            uploadfile('./docs/', filename + '.xlsx')
        else:
            print("Must profie file name.\n")
            return
    elif uploadupdate == '3':
        filename = input("Enter file name: ")
        if filename:
            updatefile(filename + '.xlsx')
        else:
            print("Must provide file.\n")
            return
        # updateinGDrive(filename+'.xlsx')  


def isfolderexists():
    if not path.exists('./docs'):
        try:
            os.mkdir('docs')
        except OSError as error:
            print("There was an error: ", error)
            return


if __name__ == "__main__":
    main()
