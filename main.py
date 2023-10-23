import yt_dlp
import youtube_dl
import instaloader
import tiktok_downloader
import requests


print("-------------------------------------")
print("SocialDownloader")
print("Made By Nguyen Hieu(RaidenShogun508)")
print("-------------------------------------")

print("Vui lòng chọn nền tảng cần tải video")
print("1.Youtube")
print("2.Facebook")
print("3.Instagram")
print("4.TikTok")

luachon = input(">>>")

loai_luachon = None
while loai_luachon is None:
    try:
        loai_luachon = int(luachon)
    except ValueError:
        print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
        luachon = input(">>>")

if loai_luachon == 1:
    print("-----------------------------")
    print("Youtube Downloader")
    print("-----------------------------")
    url = input("Dán link cần tải video vào đây:")

    # Download video
    video = yt_dlp.YoutubeDL().extract_info(url)
    video["filename"] = "video.mp4"
    
    print("------------------------")
    print("Thank You!")
    print("------------------------")

elif loai_luachon == 2:
    print("------------------------")
    print("Facebook Downloader")
    print("------------------------")
    url = input("Nhập đường link cần tải video vào đây:")
    with youtube_dl.YoutubeDL({'format': 'best'}) as ydl:
        ydl.download([url])
    print("-------------------------")
    print("Thank You!")
    print("-------------------------")

elif loai_luachon == 4:
    print("-----------------------")
    print("Tiktok Downloader")
    print("-----------------------")
    url = input("Nhập đường link cần tải video:")
    
    response = requests.get(url)

    video_data = response.content

    with open("video.mp4", "wb") as f:
        f.write(video_data)