import pytube

url = input("url giriniz :")

path = ""

pytube.YouTube(url).streams.get_highest_resolution().download(path)
