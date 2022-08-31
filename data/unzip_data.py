from zipfile import ZipFile


def unzip_dataset(zip_folder_path = "SCUT-FBP5500_v2.1.zip"):
    with ZipFile(zip_folder_path) as z:
        z.extractall()

if __name__=="__main__":
    unzip_dataset()