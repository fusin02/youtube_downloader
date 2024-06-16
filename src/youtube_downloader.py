import pytube
from pytube import YouTube
links = []
save_path = input('What is the save path? Eg: "C:/Users/your_name/Downloads": ')
while True:
    link = input('Insert youtube URL, or type "done" if you are done: ')
    if link == "done":
        break
    else :
        links.append(link)
for url in links:
    video = YouTube(url)
    video.streams.get_highest_resolution().download(save_path)
    print("Successfully downloaded: " + video.title)
