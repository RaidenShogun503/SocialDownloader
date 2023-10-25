import yt_dlp
import youtube_dl
import instaloader
import tiktok_downloader
import requests
import re
import random
import colorama

gachngang = "----------------------------------------------------------------------------------------------------------------------------------------------"

chumodau = '''\033[35m
 ## ##    ## ##    ## ##     ####     ##     ####     ### ##    ## ##   ##   ##  ###  ##  ####      ## ##     ##     ### ##   ### ###  ### ##   
##   ##  ##   ##  ##   ##     ##       ##     ##       ##  ##  ##   ##  ##   ##    ## ##   ##      ##   ##     ##     ##  ##   ##  ##   ##  ##  
####     ##   ##  ##          ##     ## ##    ##       ##  ##  ##   ##  ##   ##   # ## #   ##      ##   ##   ## ##    ##  ##   ##       ##  ##  
 #####   ##   ##  ##          ##     ##  ##   ##       ##  ##  ##   ##  ## # ##   ## ##    ##      ##   ##   ##  ##   ##  ##   ## ##    ## ##   
    ###  ##   ##  ##          ##     ## ###   ##       ##  ##  ##   ##  # ### #   ##  ##   ##      ##   ##   ## ###   ##  ##   ##       ## ##   
##   ##  ##   ##  ##   ##     ##     ##  ##   ##  ##   ##  ##  ##   ##   ## ##    ##  ##   ##  ##  ##   ##   ##  ##   ##  ##   ##  ##   ##  ##  
 ## ##    ## ##    ## ##     ####   ###  ##  ### ###  ### ##    ## ##   ##   ##  ###  ##  ### ###   ## ##   ###  ##  ### ##   ### ###  #### ##                                                                                                                                                
'''
tiktoktext = '''\033[36m
#### ##    ####   ##  ###  #### ##   ## ##   ##  ###  ### ##    ## ##   ##   ##  ###  ##  ####      ## ##     ##     ### ##   ### ###  ### ##   
# ## ##     ##    ##  ##   # ## ##  ##   ##  ##  ##    ##  ##  ##   ##  ##   ##    ## ##   ##      ##   ##     ##     ##  ##   ##  ##   ##  ##  
  ##        ##    ## ##      ##     ##   ##  ## ##     ##  ##  ##   ##  ##   ##   # ## #   ##      ##   ##   ## ##    ##  ##   ##       ##  ##  
  ##        ##    ## ##      ##     ##   ##  ## ##     ##  ##  ##   ##  ## # ##   ## ##    ##      ##   ##   ##  ##   ##  ##   ## ##    ## ##   
  ##        ##    ## ###     ##     ##   ##  ## ###    ##  ##  ##   ##  # ### #   ##  ##   ##      ##   ##   ## ###   ##  ##   ##       ## ##   
  ##        ##    ##  ##     ##     ##   ##  ##  ##    ##  ##  ##   ##   ## ##    ##  ##   ##  ##  ##   ##   ##  ##   ##  ##   ##  ##   ##  ##  
 ####      ####   ##  ###   ####     ## ##   ##  ###  ### ##    ## ##   ##   ##  ###  ##  ### ###   ## ##   ###  ##  ### ##   ### ###  #### ##                                                                                                                                                 
'''

print(gachngang)
print(chumodau)
print("Made By Nguyen Hieu(RaidenShogun508)")
print(gachngang)

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
    print(gachngang)
    print("Youtube Downloader")
    print(gachngang)
    url = input("Dán link cần tải video vào đây:")

    # Download video
    video = yt_dlp.YoutubeDL().extract_info(url)
    video["filename"] = "video.mp4"
    
    print("------------------------")
    print("Thank You!")
    print("------------------------")

elif loai_luachon == 2:
    print(gachngang)
    print("Facebook Downloader")
    print(gachngang)
    
    

    print("-------------------------")
    print("Thank You!")
    print("-------------------------")

elif loai_luachon == 4:
    print(gachngang)
    print(tiktoktext)
    print(gachngang)
    
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    layurl = input("Dán link cần tải video:")

    querystring = {"url":layurl}

    headers = {
	    "X-RapidAPI-Key": "4ba4421df8mshd017caa9b41abdfp15e1b2jsn79bc2f27180f",
	    "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    video = response.text
    video = video.replace('[','')

    link = re.findall(r'{"video":"([^"]+)"',video)
    url_video = ''.join(link)
    print(url_video)
    names = random.randrange(1, 1000) 
    name = 'video'+str(names)+'.mp4'

    r = requests.get(url_video)
    with open(name, 'wb') as f:
        f.write(r.content)