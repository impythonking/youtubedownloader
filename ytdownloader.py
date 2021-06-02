from pytube import YouTube

url = input("Enter the link of YouTube video you want to download:")
video = YouTube(str(url))

print("Video Title: ",video.title)

print("Length of video: ",video.length)

ys = video.streams.get_highest_resolution()

print("Downloading Start...")
ys.download()
print("Download completed")