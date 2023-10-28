import yt_dlp
import youtube_dl
import instaloader
import tiktok_downloader
import requests
import re
import random
import colorama
import json

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
facebooktext = '''\033[37m
 ######     ##      ####    ######   #####     ####     ####    ##  ##   ####      ####    ##   ##  ##  ##   ##        ####      ##     ####     ######   #####   
 ##        ####    ##  ##   ##       ##  ##   ##  ##   ##  ##   ## ##    ## ##    ##  ##   ##   ##  ### ##   ##       ##  ##    ####    ## ##    ##       ##  ##  
 ##       ##  ##   ##       ##       ##  ##   ##  ##   ##  ##   ####     ##  ##   ##  ##   ##   ##  ######   ##       ##  ##   ##  ##   ##  ##   ##       ##  ##  
 ####     ######   ##       ####     #####    ##  ##   ##  ##   ###      ##  ##   ##  ##   ## # ##  ######   ##       ##  ##   ######   ##  ##   ####     #####   
 ##       ##  ##   ##       ##       ##  ##   ##  ##   ##  ##   ####     ##  ##   ##  ##   #######  ## ###   ##       ##  ##   ##  ##   ##  ##   ##       ####    
 ##       ##  ##   ##  ##   ##       ##  ##   ##  ##   ##  ##   ## ##    ## ##    ##  ##   ### ###  ##  ##   ##       ##  ##   ##  ##   ## ##    ##       ## ##   
 ##       ##  ##    ####    ######   #####     ####     ####    ##  ##   ####      ####    ##   ##  ##  ##   ######    ####    ##  ##   ####     ######   ##  ##
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
youtubetext = '''\033[31m
##  ##    ## ##   ##  ###  #### ##  ##  ###  ### ##   ### ###  ### ##    ## ##   ##   ##  ###  ##  ####      ## ##     ##     ### ##   ### ###  ### ##   
##  ##   ##   ##  ##   ##  # ## ##  ##   ##   ##  ##   ##  ##   ##  ##  ##   ##  ##   ##    ## ##   ##      ##   ##     ##     ##  ##   ##  ##   ##  ##  
##  ##   ##   ##  ##   ##    ##     ##   ##   ##  ##   ##       ##  ##  ##   ##  ##   ##   # ## #   ##      ##   ##   ## ##    ##  ##   ##       ##  ##  
 ## ##   ##   ##  ##   ##    ##     ##   ##   ## ##    ## ##    ##  ##  ##   ##  ## # ##   ## ##    ##      ##   ##   ##  ##   ##  ##   ## ##    ## ##   
  ##     ##   ##  ##   ##    ##     ##   ##   ##  ##   ##       ##  ##  ##   ##  # ### #   ##  ##   ##      ##   ##   ## ###   ##  ##   ##       ## ##   
  ##     ##   ##  ##   ##    ##     ##   ##   ##  ##   ##  ##   ##  ##  ##   ##   ## ##    ##  ##   ##  ##  ##   ##   ##  ##   ##  ##   ##  ##   ##  ##  
  ##      ## ##    ## ##    ####     ## ##   ### ##   ### ###  ### ##    ## ##   ##   ##  ###  ##  ### ###   ## ##   ###  ##  ### ##   ### ###  #### ## 
'''
thankyoutext = '''
# #####  ##  ##    ###    ##   ##  ### ###  ###  ###  #####   ##   ##  
## ## ##  ##  ##   ## ##   ###  ##   ## ##    ##  ##  ### ###  ##   ##  
   ##     ##  ##  ##   ##  #### ##   ####      ####   ##   ##  ##   ##  
   ##     ######  ##   ##  #######   ###        ##    ##   ##  ##   ##  
   ##     ##  ##  #######  ## ####   ####       ##    ##   ##  ##   ##  
   ##     ##  ##  ##   ##  ##  ###   ## ##      ##    ### ###  ##   ##  
  ####    ##  ##  ##   ##  ##   ##  ### ###    ####    #####    ##### 
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
    print(youtubetext)
    print(gachngang)
    url = input("Dán link cần tải video vào đây:")

    # Download video
    video = yt_dlp.YoutubeDL().extract_info(url)
    video["filename"] = "video.mp4"
    
    print(gachngang)
    print(thankyoutext)
    print(gachngang)

elif loai_luachon == 2:
    print(gachngang)
    print(facebooktext)
    print(gachngang)
#tach link bang api 
    def get_download_high_quality_url(json_data):

        links =json_data['links']
        downloads_high_quality_url = links["Download High Quality"]
        return downloads_high_quality_url
    url = "https://facebook-reel-and-video-downloader.p.rapidapi.com/app/main.php"
    nhapurl = input("Nhập link Facebook cần tải video:")
    querystring = {"url":nhapurl}
    
    headers = {
        "X-RapidAPI-Key": "4ba4421df8mshd017caa9b41abdfp15e1b2jsn79bc2f27180f",
        "X-RapidAPI-Host": "facebook-reel-and-video-downloader.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    json_data = response.json()
    download_high_quality_url = get_download_high_quality_url(json_data)
    print(download_high_quality_url)
    r = requests.get(download_high_quality_url)
    names = random.randrange(1,10000)
    name = 'video'+str(names)+'.mp4'
    r = requests.get(download_high_quality_url)
    with open (name, 'wb') as f:
        f.write(r.content)

    
    

    print(gachngang)
    print(thankyoutext)
    print(gachngang)

elif loai_luachon == 3:
    print(gachngang)
    print("Hiện tại chức năng này không khả dụng,Vui lòng quay lại sau")
    print(gachngang)
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

    print(gachngang)
    print(thankyoutext)
    print(gachngang)