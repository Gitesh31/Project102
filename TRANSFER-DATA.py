import dropbox
class  TransferData(object):
     def _init_(self,access_token):
         self.access_token = access_token
         
     def uploadFiles(self,fileFrom,fileTo):
          dbx = dropbox.DropBox(self.access_token)
          f = open(fileFrom, 'rb')
          dbx.files_upload(f.read(), fileTo)
          
def main():
    access_token = 'sl.A0u50iB2xygKSVpLwlJOihc4C4ziJyXLzt-AnTIGDzdzjA49mZTFz7vT-EmQu28xmdCc8QGZKNCM7QCOFFvACvETIxKJkCdHPf9qVasuy71M-VfOTnTZ2MJIX7rTBntF5ahINYI'
    transferData = TransferData(access_token)
    fileFrom = input("Enter the File Path :")
    fileTo = input("Enter the Destination Path :")
    transferData.uploadFiles("Files has been moved")

main()



