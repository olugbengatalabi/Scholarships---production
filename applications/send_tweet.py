from json import load
import os
import tweepy
from django.conf import settings
from fileinput import filename
import requests
import shutil
from PIL import Image, ImageDraw, ImageFilter, ImageFont




api = tweepy.API(auth)


def send_tweet(username, avatar_url):
  my_image = Image.open(settings.MEDIA_ROOT + '/backplate.jpg')
  font_location = settings.STATIC_ROOT + '/fonts/leaguespartan-bold.ttf'
  title_font = ImageFont.truetype(font_location, 70)
  title_text = "@" + username
  image_editable = ImageDraw.Draw(my_image)
  image_editable.text((150,540), title_text, (200, 130, 211), font=title_font)
  my_image.save(settings.MEDIA_ROOT + '/backplate_texted.jpg') 
  url = avatar_url
  response = requests.get(url, stream=True)
  file_name = settings.MEDIA_ROOT + '/avatar.jpg'
  if response.status_code == 200:
    with open(file_name, 'wb') as f:
        shutil.copyfileobj(response.raw, f)
        im1 = Image.open(settings.MEDIA_ROOT + '/backplate_texted.jpg')
        im2 = Image.open(settings.MEDIA_ROOT + '/avatar.jpg')
        mask_im = Image.new("L", im2.size, 0)
        draw = ImageDraw.Draw(mask_im)
        
        draw.ellipse((0, 0, 400, 400), fill=255)
        mask_im.save(settings.MEDIA_ROOT + '/mask.jpg', quality=95)
        back_im = im1.copy()
        back_im.paste(im2, (1860, 380), mask_im)
        back_im.save(settings.MEDIA_ROOT + '/final_img.jpg', quality=95)
        media = api.media_upload(settings.MEDIA_ROOT + '/final_img.jpg')
        tweet = "Congratulations " + "@" + username + " welcome to the Dvmpster"
        post_result = api.update_status(status=tweet, media_ids=[media.media_id])
        os.remove(settings.MEDIA_ROOT + '/final_img.jpg')
        # os.remove(settings.MEDIA_ROOT + '/avatar.jpg')
        os.remove(settings.MEDIA_ROOT + '/backplate_texted.jpg')
        os.remove(settings.MEDIA_ROOT + '/mask.jpg')


  else:
      print('Image Couldn\'t be retrieved')
    



# send_tweet(username = '3scoopsofchilin', avatar_url='http://pbs.twimg.com/profile_images/1584254257376681988/PuFm6Wzi.jpg')

