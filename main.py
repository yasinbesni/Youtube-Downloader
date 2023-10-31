import pytube

url = input("Pleas Enter Url:")

path = "C:/Users/File"

pytube.YouTube(url).streams.get_highest_resolution().download(path)
