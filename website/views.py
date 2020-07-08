from django.shortcuts import render, redirect
from .getNews import *
from .stockScrapper import *
from .techNewsScrapper import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib import messages
from .models import *
import datetime


# Create your views here.
def home(request):
    return render(request, 'website/home.html', {})


def politics(request):
    return render(request, 'website/politics.html', {})


def environment(request):
    return render(request, "website/environment.html", {})


def culture(request):
    return render(request, "website/culture.html", {})


def topnews(request):
    usnewscrapper = USNewsScrapper()
    usresponse = usnewscrapper.getNews()
    hknewscrapper = HKNewsScrapper()
    hkresponse = hknewscrapper.getNews()
    twnewscrapper = TWNewsScrapper()
    twresponse = twnewscrapper.getNews()
    canewscrapper = CANewsScrapper()
    caresponse = canewscrapper.getNews()
    cnnewsscrapper = ChinaNewsScrapper()
    cnresponse = cnnewsscrapper.getNews()
    gbnewsscrapper = UKNewsScrapper()
    gbresponse = gbnewsscrapper.getNews()
    return render(request, "website/topheadlines.html", {'usnews': usresponse, 'hknews': hkresponse
    , 'twnews':twresponse, 'canews': caresponse, 'cnnews': cnresponse, 'gbnews': gbresponse})


def technology(request):
    ainewscrapper = AINewsScrapper()
    airesponse = ainewscrapper.getNews()
    ronewscrapper = RoboticsNewsScrapper()
    roresponse = ronewscrapper.getNews()
    bdnewscrapper = BDNewsScrapper()
    bdresponse = bdnewscrapper.getNews()
    ccnewscrapper = CCNewsScrapper()
    ccresponse = ccnewscrapper.getNews()
    iotnewscrapper = IOTNewsScrapper()
    iotresponse = iotnewscrapper.getNews()
    energynewscrapper = EnergyNewsScrapper()
    energyresponse = energynewscrapper.getNews()
    brainewscrapper = BrainNews()
    brainresponse = brainewscrapper.getNews()
    geneNewscrapper = GeneEditNews()
    generesponse = geneNewscrapper.getNews()
    spaceScrapper = SpaceNews()
    spaceresponse = spaceScrapper.getNews()
    nanoNewsScrapper = NanotechNews()
    nanoresponse = nanoNewsScrapper.getNews()
    synBioNewsScrapper = SynthBioNews()
    synbioresponse = synBioNewsScrapper.getNews()
    blockchainNewscrapper = BlockchainNews()
    blockchainresponse = blockchainNewscrapper.getNews()
    return render(request, "website/technology.html", {'ainews':airesponse, 'ronews':roresponse,
    'bdnews':bdresponse, 'ccnews':ccresponse, 'iotnews':iotresponse, 'energynews':energyresponse,
    'brainnews':brainresponse, 'genenews':generesponse, 'spacenews': spaceresponse, 'nanonews':nanoresponse,
    'synbionews':synbioresponse, 'bcnews': blockchainresponse})


def economics(request):
    dow_jones_scrapper = DowJonesScrapper()
    dow_jones_data = dow_jones_scrapper.get_data()
    heng_seng_scrapper = HSIScrapper()
    heng_seng_data = heng_seng_scrapper.get_data()
    london_scrapper = LSIScrapper()
    london_data = london_scrapper.get_data()
    crude_oil_scrapper = CrudeOilScrapper()
    crude_oil_data = crude_oil_scrapper.get_data()
    brent_oil_scrapper = BrentScrapper()
    brent_oil_data = brent_oil_scrapper.get_data()
    ng_scrapper = NgScrapper()
    ng_data = ng_scrapper.get_data()
    corn_scrapper = CornScrapper()
    corn_data = corn_scrapper.get_data()
    wheat_scrapper = WheatScrapper()
    wheat_data = wheat_scrapper.get_data()
    rice_scrapper = RoughRiceScrapper()
    rice_data = rice_scrapper.get_data()
    oats_scrapper = OatsScrapper()
    oats_data = oats_scrapper.get_data()
    gold_scrapper = GoldScrapper()
    gold_data = gold_scrapper.get_data()
    sil_scrapper = SilverScrapper()
    silver_data = sil_scrapper.get_data()
    cu_scrapper = CopperScrapper()
    copper_data = cu_scrapper.get_data()
    platinum_scrapper = PlatinumScrapper()
    platinum_data = platinum_scrapper.get_data()
    currency_scrapper = CurrencyScrapper()
    currency_data = currency_scrapper.get_data()
    future_scrapper = FuturesScrapper()
    future_data = future_scrapper.get_data()
    return render(request, "website/economics.html", {'dowjones': dow_jones_data, 'hengseng': heng_seng_data, 'london':london_data,
    'crudeoil': crude_oil_data, 'ng': ng_data, 'crn':corn_data, 'wt': wheat_data, 'rr':rice_data, 'oats': oats_data,
    'gold':gold_data, 'sil':silver_data, 'cu': copper_data, 'pt': platinum_data, 'brent': brent_oil_data,
    'currency': currency_data, 'futures': future_data})


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            member = Member(user=user)
            member.save()
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            print(user)
            login(request, user)
            return redirect('website:discussions')
    else:
        form = UserCreationForm()
    print("You have reached here")
    return render(request, 'website/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('login_username')
        password = request.POST.get('login_password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('website:discussions')
        else:
            messages.error(request,'Login failed. Please try again.')
    return render(request, 'website/login.html', {})


def logout(request):
    logout(request)
    return redirect('website:discussions')


def discussions(request):
    post = Post.objects.all().order_by('-release_date')
    return render(request, 'website/discussions.html', {'posts': post})


def add_post(request):
    title = request.GET.get('title')
    category = request.GET.get('category')
    content = request.GET.get('content')
    user = User.objects.get(pk=request.GET.get('user_id'))
    member = Member.objects.get(user=user)
    post = Post(title=title, category=category, content=content,
                release_date=datetime.date.today(), user=member)
    post.save()
    return redirect('website:discussions')


def add_comment(request):
    member = Member.objects.get(pk=request.GET.get('member_id'))
    post = Post.objects.get(pk=request.GET.get('post_id'))
    text = request.GET.get('text')
    comment = Comment(user=member, post=post, text=text)
    comment.save()
    return redirect('website:discussions')


def render_comment_modal(request):
    post = Post.objects.get(pk=request.GET.get('post_id'))
    return render(request, 'website/comment_modal.html', {'post': post})


def like_post(request):
    member = Member.objects.get(pk=request.GET.get('member_id'))
    post = Post.objects.get(pk=request.GET.get('post_id'))
    post.likes += 1
    post.save()
    member.liked_post += str(post.pk)
    member.liked_post += ", "
    member.save()
    return redirect('website:discussions')


def unlike_post(request):
    member = Member.objects.get(pk=request.GET.get('member_id'))
    post = Post.objects.get(pk=request.GET.get('post_id'))
    post.likes -= 1
    post.save()
    like_post_ids = member.liked_post.split(", ")
    like_post_ids.pop()
    like_post_ids.remove(str(post.pk))
    new_liked_post = ""
    for id in like_post_ids:
        new_liked_post += id
        new_liked_post += ", "
    member.liked_post = new_liked_post
    member.save()
    return redirect('website:discussions')


def dislike_post(request):
    member = Member.objects.get(pk=request.GET.get('member_id'))
    post = Post.objects.get(pk=request.GET.get('post_id'))
    post.dislikes += 1
    post.save()
    member.disliked_posts += str(post.pk)
    member.disliked_posts += ", "
    member.save()
    return redirect('website:discussions')


def undislike_post(request):
    member = Member.objects.get(pk=request.GET.get('member_id'))
    post = Post.objects.get(pk=request.GET.get('post_id'))
    post.dislikes -= 1
    post.save()
    dislike_post_ids = member.disliked_posts.split(", ")
    dislike_post_ids.pop()
    dislike_post_ids.remove(str(post.pk))
    new_disliked_post = ""
    for id in dislike_post_ids:
        new_disliked_post += id
        new_disliked_post += ", "
    member.disliked_posts = new_disliked_post
    member.save()
    return redirect('website:discussions')


def render_reply_comment_modal(request):
    comment = Comment.objects.get(pk=request.GET.get('comment_id'))
    return render(request, 'website/reply_comment_modal.html', {'comment': comment})


def add_reply_comment(request):
    member = Member.objects.get(pk=request.GET.get('member_id'))
    comment = Comment.objects.get(pk=request.GET.get('comment_id'))
    post = comment.post
    text = request.GET.get('text')
    new_comment = Comment(user=member, post=post, text=text, reply=True, reply_comment_id=comment.pk)
    new_comment.save()
    return redirect('website:discussions')


def like_comment(request):
    member = Member.objects.get(pk=request.GET.get('member_id'))
    comment = Comment.objects.get(pk=request.GET.get('comment_id'))
    comment.likes += 1
    comment.save()
    member.liked_comments += str(comment.pk)
    member.liked_comments += ", "
    member.save()
    return redirect('website:discussions')


def unlike_comment(request):
    member = Member.objects.get(pk=request.GET.get('member_id'))
    comment = Comment.objects.get(pk=request.GET.get('comment_id'))
    comment.likes -= 1
    comment.save()
    like_com_ids = member.liked_comments.split(", ")
    print(like_com_ids)
    like_com_ids.pop()
    like_com_ids.remove(str(comment.pk))
    print(like_com_ids)
    new_liked_com = ""
    for d in like_com_ids:
        new_liked_com += d
        new_liked_com += ", "
    member.liked_comments = new_liked_com
    print(new_liked_com)
    member.save()
    return redirect('website:discussions')


def dislike_comment(request):
    member = Member.objects.get(pk=request.GET.get('member_id'))
    comment = Comment.objects.get(pk=request.GET.get('comment_id'))
    comment.dislikes += 1
    comment.save()
    member.dislike_comments += str(comment.pk)
    member.dislike_comments += ", "
    member.save()
    return redirect('website:discussions')


def undislike_comment(request):
    member = Member.objects.get(pk=request.GET.get('member_id'))
    comment = Comment.objects.get(pk=request.GET.get('comment_id'))
    comment.dislikes -= 1
    comment.save()
    dislike_com_ids = member.dislike_comments.split(", ")
    dislike_com_ids.pop()
    dislike_com_ids.remove(str(comment.pk))
    new_disliked_com = ""
    for id in dislike_com_ids:
        new_disliked_com += id
        new_disliked_com += ", "
    member.dislike_comments = new_disliked_com
    member.save()
    return redirect('website:discussions')
