
from ast import If
from email.mime import application
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Application
from django.core.files.storage import FileSystemStorage
# Create your views here.


def index(request):
  return render(request, 'index.html')
  

def category_options(request):
  return render(request, 'step1.html')


def developer_form(request):
  if request.user.is_authenticated:
    if Application.objects.filter(user = request.user).exists():
      messages.info(request, "You already applied ")
      return redirect("index")
    else:
      if request.method == "POST":
        application_text = request.POST.get("application_text")
        wallet_address = request.POST.get("wallet_address")
        link1 = request.POST.get("link1")
        link2 = request.POST.get("link2")
        suggestion = request.POST.get("suggestion")
        image = request.FILES.get("image")
        avatar_url = request.POST.get("avatar_url")
        if wallet_address == '':
          messages.error(request, "Connect Martian wallet to continue")
          return redirect('developer_form')
        elif Application.objects.filter(wallet_address = wallet_address).exists():
          messages.error(request, "Wallet address already associated with another application")
          return redirect('developer_form')
        if application_text:
          Application.objects.create(user = request.user, niche = 'DV', status = 'UR', application_text = application_text, wallet_address = wallet_address, avatar_url = avatar_url )
        else:
          messages.error(request, "Application cannot be empty")
          return redirect('developer_form')
        
          
        user_application = get_object_or_404(Application, user = request.user)
        if image:
          if image.size > 3000000:
            messages.error(request, "Image size cannot exceed 3MB")
            return redirect('developer_form')
          fs = FileSystemStorage()
          filename = fs.save(image.name, image)
          upload_file_url = fs.url(filename)
          user_application.image = filename
          user_application.save()
          
        if link1:
          if "https://" not in link1:
            messages.error(request, "input a valid url")
            return redirect('developer_form')
          else:
            user_application.link1 = link1
            user_application.save()
        if link2:
          if "https://" not in link2:
            messages.error(request, "input a valid HTTPs url")
            return redirect('developer_form')
          else:
            user_application.link2 = link2
            user_application.save()
            
        if suggestion:
          user_application.suggestions = suggestion
          user_application.save()

          
        
        messages.success(request, "Application submitted")
        return redirect("success")
  else:
    messages.info(request, "Connect Twitter")
    return redirect("category_picker")
      

  return render(request, "developer_form.html")


def normie_form(request):
  if request.user.is_authenticated:
    if Application.objects.filter(user=request.user).exists():
      messages.info(request, "You already applied ")
      return redirect("index")
    else:
      if request.method == "POST":
        application_text = request.POST.get("application_text")
        wallet_address = request.POST.get("wallet_address")
        trader_type = request.POST.get("trader_type")
        first_nft = request.POST.get("firstNft")
        suggestion = request.POST.get("suggestion")
        nft_trading_duration = request.POST.get("nft_duration")
        avatar_url = request.POST.get("avatar_url")
        if wallet_address == '':
          messages.error(request, "Connect Martian wallet to continue")
          return redirect('normie_form')
        elif Application.objects.filter(wallet_address=wallet_address).exists():
          messages.error(
              request, "Wallet address already associated with another application")
          return redirect('normie_form')
        if first_nft == "" or None or trader_type == "" or None or nft_trading_duration == "" or None:
          messages.error(request, "Form field(s) cannot be empty")
          return redirect('normie_form')
        if application_text:
          Application.objects.create(user=request.user, niche='NM', status='UR' ,application_text=application_text, wallet_address=wallet_address, trader_type=trader_type, first_nft = first_nft, nft_trading_duration = nft_trading_duration, avatar_url = avatar_url)
        else:
          messages.error(request, "Application cannot be empty")
          return redirect('normie_form')

        user_application = get_object_or_404(Application, user=request.user)


        if suggestion:
          user_application.suggestions = suggestion
          user_application.save()

        messages.success(request, "Application submitted")
        return redirect("success")
  else:
    messages.info(request, "Connect Twitter")
    return redirect("category_picker")

  return render(request, "normie_form.html")


def influencer_form(request):
  if request.user.is_authenticated:
    if Application.objects.filter(user=request.user).exists():
      messages.info(request, "You already applied ")
      return redirect("index")
    else:
      if request.method == "POST":
        application_text = request.POST.get("application_text")
        wallet_address = request.POST.get("wallet_address")
        if_lost_followers = request.POST.get("if_lost_followers")
        suggestion = request.POST.get("suggestion")
        avatar_url = request.POST.get("avatar_url")
        
        if wallet_address == '':
          messages.error(request, "Connect Martian wallet to continue")
          return redirect('influencer_form')
        elif Application.objects.filter(wallet_address=wallet_address).exists():
          messages.error(
              request, "Wallet address already associated with another application")
          return redirect('influencer_form')
        if if_lost_followers == "" or None:
          messages.error(request, "Form field(s) cannot be empty")
          return redirect('influencer_form')

        if application_text:
          Application.objects.create(user=request.user, niche='IF', status='UR',
                                     application_text=application_text, wallet_address=wallet_address, if_lost_followersn=if_lost_followers, avatar_url=avatar_url)
        else:
          messages.error(request, "Application cannot be empty")
          return redirect('influencer_form')

        user_application = get_object_or_404(Application, user=request.user)

        if suggestion:
          user_application.suggestions = suggestion
          user_application.save()
        return redirect("success")
  else:
    messages.info(request, "Connect Twitter")
    return redirect("category_picker")
  return render(request, 'influencer_form.html')


def artist_form(request):
  if request.user.is_authenticated:
    if Application.objects.filter(user=request.user).exists():
      messages.info(request, "You already applied ")
      return redirect("index")
    else:
      if request.method == "POST":
        application_text = request.POST.get("application_text")
        wallet_address = request.POST.get("wallet_address")
        suggestion = request.POST.get("suggestion")
        image = request.FILES.get("image")
        image_2 = request.FILES.get("image2")
        image_3 = request.FILES.get("image3")
        avatar_url = request.POST.get("avatar_url")
        if wallet_address == '':
          messages.error(request, "Connect Martian wallet to continue")
          return redirect('artist_form')
        elif Application.objects.filter(wallet_address=wallet_address).exists():
          messages.error(
              request, "Wallet address already associated with another application")
          return redirect('artist_form')
        if application_text:
          Application.objects.create(user=request.user, niche='AR', status='UR', application_text=application_text, wallet_address=wallet_address, avatar_url = avatar_url)
        else:
          messages.error(request, "Application cannot be empty")
          return redirect('artist_form')

        user_application = get_object_or_404(Application, user=request.user)
        if image:
          if image.size > 3000000:
            messages.error(request, "Image size cannot exceed 3MB")
            return redirect('artist_form')
          fs = FileSystemStorage()
          filename = fs.save(image.name, image)

          upload_file_url = fs.url(filename)
          user_application.image = filename
          user_application.save()
        if image_2:
          if image_2.size > 3000000:
            messages.error(request, "Image size cannot exceed 3MB")
            return redirect('artist_form')
          fs = FileSystemStorage()
          filename = fs.save(image_2.name, image_2)

          upload_file_url = fs.url(filename)
          user_application.image_2 = filename
          user_application.save()
        if image_3:
          if image_3.size > 3000000:
            messages.error(request, "Image size cannot exceed 3MB")
            return redirect('artist_form')
          fs = FileSystemStorage()
          filename = fs.save(image_3.name, image_3)

          upload_file_url = fs.url(filename)
          user_application.image_3 = filename
          user_application.save()

        if suggestion:
          user_application.suggestions = suggestion
          user_application.save()
        return redirect("success")
  else:
    messages.info(request, "Connect Twitter")
    return redirect("category_picker")
      

  return render(request, "artist_form.html")


def founder_form(request):
  if request.user.is_authenticated:
    if Application.objects.filter(user=request.user).exists():
      messages.info(request, "You already applied ")
      return redirect("index")
    else:
      if request.method == "POST":
        application_text = request.POST.get("application_text")
        wallet_address = request.POST.get("wallet_address")
        problems_and_solution= request.POST.get("problems_and_solutions")
        suggestion = request.POST.get("suggestion")
        avatar_url = request.POST.get("avatar_url")
        if wallet_address == '':
          messages.error(request, "Connect Martian wallet to continue")
          return redirect('founder_form')
        elif Application.objects.filter(wallet_address=wallet_address).exists():
          messages.error(
              request, "Wallet address already associated with another application")
          return redirect('founder_form')
        if problems_and_solution == "" or None:
          messages.error(request, "Form field(s) cannot be empty")
          return redirect('founder_form')

        if application_text:
          Application.objects.create(user=request.user, niche='PF', status='UR',
                                     application_text=application_text, wallet_address=wallet_address, problems_and_solution=problems_and_solution, avatar_url = avatar_url)
        else:
          messages.error(request, "Application cannot be empty")
          return redirect('founder_form')

        user_application = get_object_or_404(Application, user=request.user)

        if suggestion:
          user_application.suggestions = suggestion
          user_application.save()
        return redirect("success")
  else:
    messages.info(request, "Connect Twitter")
    return redirect("category_picker")
  return render(request, 'founder_form.html')

def builder_form(request):
  if request.user.is_authenticated:
    if Application.objects.filter(user=request.user).exists():
      messages.info(request, "You already applied ")
      return redirect("index")
    else:
      if request.method == "POST":
        application_text = request.POST.get("application_text")
        wallet_address = request.POST.get("wallet_address")
        value_to_add = request.POST.get("value_to_add")
        suggestion = request.POST.get("suggestion")
        avatar_url = request.POST.get("avatar_url")
        if wallet_address == '':
          messages.error(request, "Connect Martian wallet to continue")
          return redirect('community_builder_form')
        elif Application.objects.filter(wallet_address=wallet_address).exists():
          messages.error(
              request, "Wallet address already associated with another application")
          return redirect('community_builder_form')
        if value_to_add == "" or None:
          messages.error(request, "Form field(s) cannot be empty")
          return redirect('community_builder_form')
        if application_text:
          Application.objects.create(user=request.user, niche='CB', status='UR', application_text=application_text, wallet_address=wallet_address, value_to_add=value_to_add, avatar_url = avatar_url)
        else:
          messages.error(request, "Application cannot be empty")
          return redirect('community_builder_form')

        user_application = get_object_or_404(Application, user=request.user)

        if suggestion:
          user_application.suggestions = suggestion
          user_application.save()

        messages.success(request, "Application submitted")
        return redirect("community_builder_form")
  else:
    messages.info(request, "Connect Twitter")
    return redirect("category_picker")

  return render(request, 'builder_form.html')



login_required()
def success(request):
  return render(request, "success.html")

def category_redirect(request):
  return redirect("category_picker")


