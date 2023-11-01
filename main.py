from pytube import YouTube
youTube_link = input("Enter the YouTube video URL: ")
def ytDownload(link):
    youtubeObject = YouTube(youTube_link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")



ytDownload(youTube_link)
