import mutagen
from PIL import Image
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from io import BytesIO


def loadfile(path):
    try:
        audio = MP3(path)
        info = [audio["TIT2"],audio["TPE1"],audio['TALB'],int(audio["TCON"]),int(audio["TRCK"]),int(audio["TPOS"]),audio["TDRC"],
                audio.info.length]
        try:
            info.append(audio.get('APIC:thumbnail').data)
        except:
            info.append(audio.get('APIC:').data)

        try:
            info.append(audio["USLT::XXX"])
        except:
            print("Your song doesn't include lyrics.")
            info.append("Lyrics not found.")
        finally:
            return info


    except:
        print("There has been an error importing the file selected. Please, make sure the file is correct.")
        return 0


# audio2 = FLAC("exampleflac.flac")
# print(list(audio2))
# print(audio2['artists'][0])
# print(audio2['totaltracks'][0])
#
# audio = MP3("honza.mp3")
# print(list(audio))
# #print(audio['COMM::eng']) #Commentary
# #print(audio["TPE2"]) #Artist2
# #print(audio["TSOA"]) #Album
# #print(audio["TSOT"]) #Track
#
# try:
#     pics = audio.get('APIC:thumbnail').data
# except:
#     pics = audio.get('APIC:').data
#
# print(pics)
# img = Image.open(BytesIO(pics))
# img = img.save(f'{audio["TIT2"]}.jpg')
# print(list(audio))
# print(audio["TIT2"]) #Track
# print(audio["TPE1"]) #Artist
# print(audio['TALB']) #Album
# print(audio["TCON"]) #Genre
# print(audio["TRCK"]) #TrackNumber
# print(audio["TPOS"]) #Disc
# print(audio["TDRC"]) #Year
# print(audio.info.length) #Runtime
# print(audio["USLT::XXX"]) #Lyrics