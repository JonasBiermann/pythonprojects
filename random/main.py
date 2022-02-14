from pytube import YouTube

link = input('Enter in the link to the video: ')

video = YouTube(link)

print(video.title)

stream = video.streams.get_by_itag(22)
stream.download()
print('Video downloaded')