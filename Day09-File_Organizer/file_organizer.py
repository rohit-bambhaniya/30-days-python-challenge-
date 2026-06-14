import os

img_count = 0
document_count = 0
video_count = 0
music_count = 0
other_count = 0
file_count = 0
folder_count = 0

path = input("Enter folder path: ")

if os.path.exists(path):

    print("Folder found!")

    files = os.listdir(path)

    for index, file in enumerate(files,start=1):

        full_path = os.path.join(path, file)

        if os.path.isdir(full_path):
          

            print(f"{index}.{file} -> Folder")
            folder_count += 1
            continue

        else:

            print(f"{index}.{file} -> File")
            file_count += 1
   

        _, extension = os.path.splitext(file)

        extension = extension.lower()

        if extension in [".jpg", ".jpeg", ".png"]:

            print(f"{file} -> Image")
            img_count += 1

        elif extension in [".pdf", ".docx", ".txt"]:

            print(f"{file} -> Document")
            document_count += 1

        elif extension in [".mp4", ".mkv"]:
            print(f"{file} -> Video")
            video_count += 1

        elif extension in [".mp3"]:
            print(f"{file} -> Music")
            music_count += 1

        else:
            print(f"{file} -> Other")
            other_count += 1

         
    print(f"Total folder {folder_count}")
    print(f"Total files {file_count}")
   

    print(f" Imges: {img_count}")
    print(f" Document: {document_count}")
    print(f" Video: {video_count}")
    print(f" Music: {music_count}")
    print(f" Other: {other_count}")
    print(f" total: {len(files)}")

else:

    print("Folder not found!")


       