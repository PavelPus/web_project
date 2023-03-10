from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session

from django.db.models import Count, Avg, Max, Min
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json as simplejson

from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm, CommentFormAdd
#from .settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL

from .models import Vegetables,Tomato,Kapusta,Perets,Baklajan,Svekla,Morkov,Redis,Cucumber,Comments,Flowers
# Create your views here.
def index(request):
    context = {}
    #request.session.flush()
    list_of = Tomato.objects.values('veg_type', 'vids', 'image', 'name', 'pub_date').order_by('-pub_date')[:8]
    list_of = list_of.union(Baklajan.objects.values('veg_type', 'vids', 'image', 'name', 'pub_date').order_by('-pub_date')[:8])
    list_of = list_of.union(Kapusta.objects.values('veg_type', 'vids', 'image', 'name', 'pub_date').order_by('-pub_date')[:8])
    list_of = list_of.union(Perets.objects.values('veg_type', 'vids', 'image', 'name', 'pub_date').order_by('-pub_date')[:8])
    list_of = list_of.union(Svekla.objects.values('veg_type', 'vids', 'image', 'name', 'pub_date').order_by('-pub_date')[:8])
    list_of = list_of.union(Morkov.objects.values('veg_type', 'vids', 'image', 'name', 'pub_date').order_by('-pub_date')[:8])
    list_of = list_of.union(Redis.objects.values('veg_type', 'vids', 'image', 'name', 'pub_date').order_by('-pub_date')[:8])
    list_of = list_of.union(Cucumber.objects.values('veg_type', 'vids', 'image', 'name', 'pub_date').order_by('-pub_date')[:8])
    list_of_new_sorts = list_of.order_by('-pub_date')[:8]
    
    flower_new_sorts = Flowers.objects.order_by('pub_date')[:8]
    
    list_of_likes = Tomato.objects.values('veg_type', 'vids', 'image', 'name', 'likes').order_by('-likes')[:8]
    list_of_likes = list_of_likes.union(Baklajan.objects.values('veg_type', 'vids', 'image', 'name', 'likes').order_by('-likes')[:8])
    list_of_likes = list_of_likes.union(Kapusta.objects.values('veg_type', 'vids', 'image', 'name', 'likes').order_by('-likes')[:8])
    list_of_likes = list_of_likes.union(Perets.objects.values('veg_type', 'vids', 'image', 'name', 'likes').order_by('-likes')[:8])
    list_of_likes = list_of_likes.union(Svekla.objects.values('veg_type', 'vids', 'image', 'name', 'likes').order_by('-likes')[:8])
    list_of_likes = list_of_likes.union(Morkov.objects.values('veg_type', 'vids', 'image', 'name', 'likes').order_by('-likes')[:8])
    list_of_likes = list_of_likes.union(Redis.objects.values('veg_type', 'vids', 'image', 'name', 'likes').order_by('-likes')[:8])
    list_of_likes = list_of_likes.union(Cucumber.objects.values('veg_type', 'vids', 'image', 'name', 'likes').order_by('-likes')[:8])
    list_of_likes = list_of_likes.union(Flowers.objects.values('veg_type', 'vids', 'image', 'name', 'likes').order_by('-likes')[:8])
    list_of_likes_sorts = list_of_likes.order_by('-likes')[:8]
        
    context = {'new_sorts':list_of_new_sorts, 'likes_sorts':list_of_likes_sorts, 'flower_new_sorts':flower_new_sorts}
    #print(context)
    return render(request, 'ls/index.html', context)

def VegList(request):
    veg_list = Vegetables.objects.order_by('veg_type')
    context = {'veg_list':veg_list}
    list_of_likes = Tomato.objects.values('veg_type', 'vids', 'image', 'name', 'likes').order_by('-likes')[:8]
    list_of_likes = list_of_likes.union(Baklajan.objects.values('veg_type', 'vids', 'image', 'name', 'likes').order_by('-likes')[:8])
    list_of_likes = list_of_likes.union(Kapusta.objects.values('veg_type', 'vids', 'image', 'name', 'likes').order_by('-likes')[:8])
    list_of_likes = list_of_likes.union(Perets.objects.values('veg_type', 'vids', 'image', 'name', 'likes').order_by('-likes')[:8])
    list_of_likes = list_of_likes.union(Svekla.objects.values('veg_type', 'vids', 'image', 'name', 'likes').order_by('-likes')[:8])
    list_of_likes = list_of_likes.union(Morkov.objects.values('veg_type', 'vids', 'image', 'name', 'likes').order_by('-likes')[:8])
    list_of_likes = list_of_likes.union(Redis.objects.values('veg_type', 'vids', 'image', 'name', 'likes').order_by('-likes')[:8])
    list_of_likes = list_of_likes.union(Cucumber.objects.values('veg_type', 'vids', 'image', 'name', 'likes').order_by('-likes')[:8])
    list_of_likes_sorts = list_of_likes.order_by('-likes')[:8]
    context['list_of_likes_sorts'] = list_of_likes_sorts
    return render(request, 'ls/veg_types.html', context)

def InVegList(request, veg_type, veg_vids=''):
    context = {}
    #veg_descr = Vegetables.objects.filter(veg_type = veg_type).values('description')[0]['description']
    veg_descr = Vegetables.objects.get(veg_type = veg_type)
    #print(veg_descr)
    #print('veg_type={0}, veg_vids={1}'.format(veg_type,veg_vids))
    if veg_type == '??????????????':
        if veg_vids == '':
            veg_list = Kapusta.objects.values('vids', 'vids_image').annotate(Count('vids'))
            context = {'veg_list':veg_list,'veg_descr':veg_descr,'veg_type':veg_type, 'veg_vids':veg_vids}
        else:
            sort_list = Kapusta.objects.filter(vids = veg_vids)
            context = {'sort_list':sort_list,'veg_type':veg_type, 'veg_vids':veg_vids}
    if veg_type == '????????????':
        if veg_vids == '':
            veg_list = Tomato.objects.values('vids', 'vids_image').annotate(Count('vids'))
            context = {'veg_list':veg_list,'veg_descr':veg_descr,'veg_type':veg_type, 'veg_vids':veg_vids}
        else:
            sort_list = Tomato.objects.filter(vids = veg_vids)
            context = {'sort_list':sort_list,'veg_type':veg_type, 'veg_vids':veg_vids}
            print(sort_list)
    if veg_type == '??????????':
        if veg_vids == '':
            veg_list = Perets.objects.values('vids', 'vids_image').annotate(Count('vids'))
            context = {'veg_list':veg_list,'veg_descr':veg_descr,'veg_type':veg_type, 'veg_vids':veg_vids}
        else:
            sort_list = Perets.objects.filter(vids = veg_vids)
            context = {'sort_list':sort_list,'veg_type':veg_type, 'veg_vids':veg_vids}
    if veg_type == '??????????????????':
        if veg_vids == '':
            sort_list = Baklajan.objects.all()
            context = {'sort_list':sort_list,'veg_descr':veg_descr,'veg_type':veg_type}
    if veg_type == '????????????':
        if veg_vids == '':
            sort_list = Svekla.objects.all()
            context = {'sort_list':sort_list,'veg_descr':veg_descr,'veg_type':veg_type}
    if veg_type == '??????????????':
        if veg_vids == '':
            sort_list = Morkov.objects.all()
            context = {'sort_list':sort_list,'veg_descr':veg_descr,'veg_type':veg_type}
    if veg_type == '??????????':
        if veg_vids == '':
            sort_list = Redis.objects.all()
            context = {'sort_list':sort_list,'veg_descr':veg_descr,'veg_type':veg_type}
    if veg_type == '????????????':
        if veg_vids == '':
            sort_list = Cucumber.objects.all()
            context = {'sort_list':sort_list,'veg_descr':veg_descr,'veg_type':veg_type}
            #veg_list = Cucumber.objects.values('vids', 'vids_image').annotate(Count('vids'))
            #context = {'veg_list':veg_list,'veg_descr':veg_descr,'veg_type':veg_type, 'veg_vids':veg_vids}
        #else:
            #sort_list = Cucumber.objects.filter(vids = veg_vids)
            #context = {'sort_list':sort_list,'veg_type':veg_type, 'veg_vids':veg_vids}
    return render(request, 'ls/veg_details.html', context)


def SortDetails(request, name, veg_type, veg_vids=''):
    context = {}
    comment_form = CommentFormAdd()
    likes_color = {}
    ??ompare_color = ''
    isvis_like = ''
    isvis_compare = ''
    ??ompare_text = '???????????????? ?? ??????????????????'
    color_key = veg_type + name + 'likes_color'
    
    if color_key in request.session:
            likes_color = request.session[color_key]
            isvis_like = 'isvis_like'
    if '??ompare' in request.session:
        if veg_type in request.session['??ompare']:
            if name in request.session['??ompare'][veg_type]:
                isvis_compare = 'isvis_compare'
                ??ompare_color = 'compare_input-after'
    #print('SortDetails: veg_type={0}, veg_vids={1}, name={2}, approved={3}'.format(veg_type,veg_vids,name,approved))
    if veg_type == '????????????':
        sort_details = Tomato.objects.get(name = name)
        sort_related_list = Tomato.objects.filter(~Q(name=name)).order_by('-likes')[:6]

    if veg_type == '??????????':
        sort_details = Perets.objects.get(name = name)
        sort_related_list = Perets.objects.filter(~Q(name=name)).order_by('-likes')[:6]

    if veg_type == '??????????????':
        sort_details = Kapusta.objects.get(name = name)
        sort_related_list = Kapusta.objects.filter(~Q(name=name)).order_by('-likes')[:6]

    if veg_type == '??????????????????':
        sort_details = Baklajan.objects.get(name = name)
        sort_related_list = Baklajan.objects.filter(~Q(name=name)).order_by('-likes')[:6]

    if veg_type == '????????????':
        sort_details = Svekla.objects.get(name = name)
        sort_related_list = Svekla.objects.filter(~Q(name=name)).order_by('-likes')[:6]

    if veg_type == '??????????????':
        sort_details = Morkov.objects.get(name = name)
        sort_related_list = Morkov.objects.filter(~Q(name=name)).order_by('-likes')[:6]

    if veg_type == '??????????':
        sort_details = Redis.objects.get(name = name)
        sort_related_list = Redis.objects.filter(~Q(name=name)).order_by('-likes')[:6]

    if veg_type == '????????????':
        sort_details = Cucumber.objects.get(name = name)
        sort_related_list = Cucumber.objects.filter(~Q(name=name)).order_by('-likes')[:6]
        
    context={'sort_details':sort_details,'veg_type':veg_type,'veg_vids':veg_vids}
    context['comment_form'] = comment_form
    try:
        sort_comments = Comments.objects.filter(Q(toSortName=name)).filter(Q(approved=True)).order_by('-pub_date')
        context['sort_comments'] = sort_comments
        print(context)
    except:
        print('nothing')
    context['isvis_like'] = isvis_like
    context['isvis_compare'] = isvis_compare
    context['sort_related_list'] = sort_related_list
    context['likes_color'] = likes_color
    context['??ompare_color'] = ??ompare_color
    return render(request, 'ls/sort_details.html', context)

############ ?????????? ####
def FlowersVid(request):
    flower_list = Flowers.objects.values('vids', 'vid_image')#.annotate(Count=('vid'))
    list_of_likes_sorts = Flowers.objects.order_by('-likes')[:8]
    context = {'flower_list':flower_list}
    context['list_of_likes_sorts'] = list_of_likes_sorts
    return render(request, 'ls/flowers.html', context)

def FlowersVidDetails(request,vid):
    flower_vid_details = Flowers.objects.filter(vids = vid)
    context = {'flower_vid_details':flower_vid_details, 'vid':vid}
    #print(flower_vid_details[0])
    return render(request, 'ls/flowers_vid.html', context)

def FlowersSortDetails(request,vid, name):
    context = {}
    comment_form = CommentFormAdd()
    likes_color = {}
    ??ompare_color = ''
    isvis_like = ''
    isvis_compare = ''
    ??ompare_text = '???????????????? ?? ??????????????????'
    color_key = '??????????' + name + 'likes_color'
    if color_key in request.session:
        likes_color = request.session[color_key]
        isvis_like = 'isvis_like'
            
    flower_sort_details = Flowers.objects.get(name = name)
    context = {'flower_sort_details':flower_sort_details}
    context['likes_color'] = likes_color
    context['isvis_like'] = isvis_like
    #print(context)
    return render(request, 'ls/flower_sort_details.html', context)

@csrf_exempt
def SortVote(request):
    
    if request.method == 'POST':
        name = request.POST.get('sort_name', None)
        veg_type = request.POST.get('veg_type', None)
        color_key = veg_type + name + 'likes_color'
        if veg_type == '????????????':
            sort = Tomato.objects.get(name = name)
            sort.likes += 1
            sort.save()
            request.session[color_key] = 'likes_input-after'
        if veg_type == '??????????':
            sort = Perets.objects.get(name = name)
            sort.likes += 1
            sort.save()
            request.session[color_key] = 'likes_input-after'
        if veg_type == '??????????????????':
            sort = Baklajan.objects.get(name = name)
            sort.likes += 1
            sort.save()
            request.session[color_key] = 'likes_input-after'
        if veg_type == '??????????????':
            sort = Kapusta.objects.get(name = name)
            sort.likes += 1
            sort.save()
            request.session[color_key] = 'likes_input-after'
        if veg_type == '????????????':
            sort = Svekla.objects.get(name = name)
            sort.likes += 1
            sort.save()
            request.session[color_key] = 'likes_input-after'
        if veg_type == '??????????????':
            sort = Morkov.objects.get(name = name)
            sort.likes += 1
            sort.save()
            request.session[color_key] = 'likes_input-after'
        if veg_type == '??????????':
            sort = Redis.objects.get(name = name)
            sort.likes += 1
            sort.save()
            request.session[color_key] = 'likes_input-after'
        if veg_type == '????????????':
            sort = Cucumber.objects.get(name = name)
            sort.likes += 1
            sort.save()
            request.session[color_key] = 'likes_input-after'
        if veg_type == '??????????':
            print(name)
            sort = Flowers.objects.get(name = name)
            sort.likes += 1
            sort.save()
            request.session[color_key] = 'likes_input-after'

        return JsonResponse(veg_type, safe=False)

@csrf_exempt
def SortCompare(request):
    if request.method == 'POST':
        name = request.POST.get('sort_name', None)
        veg_type = request.POST.get('veg_type', None)
        if '??ompare' not in request.session:
            request.session['??ompare'] = {}
        if veg_type not in request.session['??ompare']:
            request.session['??ompare'][veg_type] =list()
        request.session['??ompare'][veg_type].append(name)
        request.session.save()
        return JsonResponse(veg_type, safe=False)

@csrf_exempt
def SortCompareDel(request):
    veg_type = request.POST.get('veg_type', None)
    name = request.POST.get('name', None)
    request.session['??ompare'][veg_type].remove(name)
    request.session.modified = True
    if len(request.session['??ompare'][veg_type]) == 0:
        del request.session['??ompare'][veg_type]
        request.session.modified = True
    return JsonResponse('', safe=False)

def CompareList(request):
    context = {}
    sort_details = []
    #s = Session.objects.get(pk='2j93yxr8ra07d07ka15a4wq5o4a9o36r')
    #print(request.session['??ompare'])
    if '??ompare' in request.session:
        if '????????????' in request.session['??ompare']:
            q_objects = Q(name='none')
            QQuery = []
            QQuery = request.session['??ompare']['????????????']
            for t in QQuery:
                q_objects |= Q(name=t)
            sort_details.append(Tomato.objects.filter(q_objects))
        if '??????????' in request.session['??ompare']:
            q_objects = Q(name='none')
            QQuery = []
            QQuery = request.session['??ompare']['??????????']
            for t in QQuery:
                q_objects |= Q(name=t)
            sort_details.append(Perets.objects.filter(q_objects))
        if '??????????????????' in request.session['??ompare']:
            q_objects = Q(name='none')
            QQuery = []
            QQuery = request.session['??ompare']['??????????????????']
            for t in QQuery:
                q_objects |= Q(name=t)
            sort_details.append(Baklajan.objects.filter(q_objects))
        if '??????????????' in request.session['??ompare']:
            q_objects = Q(name='none')
            QQuery = []
            QQuery = request.session['??ompare']['??????????????']
            for t in QQuery:
                q_objects |= Q(name=t)
            sort_details.append(Kapusta.objects.filter(q_objects))
        if '????????????' in request.session['??ompare']:
            q_objects = Q(name='none')
            QQuery = []
            QQuery = request.session['??ompare']['????????????']
            for t in QQuery:
                q_objects |= Q(name=t)
            sort_details.append(Svekla.objects.filter(q_objects))
        if '??????????????' in request.session['??ompare']:
            q_objects = Q(name='none')
            QQuery = []
            QQuery = request.session['??ompare']['??????????????']
            for t in QQuery:
                q_objects |= Q(name=t)
            sort_details.append(Morkov.objects.filter(q_objects))
        if '??????????' in request.session['??ompare']:
            q_objects = Q(name='none')
            QQuery = []
            QQuery = request.session['??ompare']['??????????']
            for t in QQuery:
                q_objects |= Q(name=t)
            sort_details.append(Redis.objects.filter(q_objects))
        if '????????????' in request.session['??ompare']:
            q_objects = Q(name='none')
            QQuery = []
            QQuery = request.session['??ompare']['????????????']
            for t in QQuery:
                q_objects |= Q(name=t)
            sort_details.append(Cucumber.objects.filter(q_objects))
    #print('???????????? ???? ????????????????????')
    context = {'lists': sort_details}
    #print(context)
    return render(request, 'ls/compare.html', context)

@csrf_exempt
def SearchList(request):
    search_list_dict = {}
    names = []
    images = []
    urls = []
    data = request.POST.get('sort_search', None)
    search_list = Tomato.objects.filter(Q(name__icontains=data)).values('name','image','veg_type','vids')
    search_list = search_list.union(Perets.objects.filter(Q(name__icontains=data)).values('name','image','veg_type','vids'))
    search_list = search_list.union(Baklajan.objects.filter(Q(name__icontains=data)).values('name','image','veg_type','vids'))
    search_list = search_list.union(Kapusta.objects.filter(Q(name__icontains=data)).values('name','image','veg_type','vids'))
    search_list = search_list.union(Svekla.objects.filter(Q(name__icontains=data)).values('name','image','veg_type','vids'))
    search_list = search_list.union(Morkov.objects.filter(Q(name__icontains=data)).values('name','image','veg_type','vids'))
    search_list = search_list.union(Redis.objects.filter(Q(name__icontains=data)).values('name','image','veg_type','vids'))
    search_list = search_list.union(Cucumber.objects.filter(Q(name__icontains=data)).values('name','image','veg_type','vids'))
    print('???????????? ??????????????='+data)
    print('search_list union')
    print(search_list)
    print('?????????? ???? ??????????????')
    for s in search_list:
        print(s['name'])
        if s['vids'] is None:
            names.append(s['name'])
            images.append('/static/'+str(s['image']))
            urls.append('/vegetables/' + s['veg_type'] + '/sorts/' + s['name']+'/')
            #print('????????????????={0}, ????????={1}, ????????={2}'.format(s.name, s.image, '/vegetables/' + s.veg_type + '/' + s.name))
        else:
            names.append(s['name'])
            images.append('/static/'+str(s['image']))
            urls.append('/vegetables/' + s['veg_type'] + '/' + s['vids'] + '/sorts/' + s['name']+'/')
            #print('????????????????={0}, ????????={1}, ????????={2}'.format(s.name, s.image, '/vegetables/' + s.veg_type + '/' + s.vids + '/' + s.name))
    search_list_dict['names'] = names
    search_list_dict['images'] = images
    search_list_dict['urls'] = urls
    print(search_list_dict)
    return JsonResponse(search_list_dict, safe=False)

############ EMAIL ############################################################
RECIPIENTS_EMAIL = ['ls@lovelysad.ru']
DEFAULT_FROM_EMAIL = 'ls@lovelysad.ru'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

def Contact(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # ???????? ?????????? POST, ???????????????? ?????????? ?? ???????????????? ????????????
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_name = form.cleaned_data['from_name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{from_name} ???????????????? {subject} ?? ?????????? {from_email} ???????? {ttt}', message,
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('???????????? ?? ???????? ????????????.')
            return HttpResponseRedirect(reverse('ls:Success', args=()))
    else:
        return HttpResponse('???????????????? ????????????.')
    return render(request, 'ls/contact_email.html', {'form': form})

def Success(request):
    return HttpResponse('??????????????! ?????????????? ???? ???????? ??????????????????.')

####################### Send response ###########################################################################
@csrf_exempt
def SendResponse(request):
    if request.method == 'POST':
        from_name = request.POST.get('from_name', None)
        from_email = request.POST.get('from_email', None)
        message = request.POST.get('message', None)
        sort = request.POST.get('sort', None)
        veg_type = request.POST.get('veg_type', None)
        veg_vids= request.POST.get('veg_vids', None)
        #print('?????????????????????? ???? {0} ?? ?????????????? {1} ?????????????????? {2} ???? ???????? {3} ?????? {4} ?????? {5}'.format(from_name,from_email,message,sort,veg_type,veg_vids))
        new_comment = Comments(toSortName = sort, authorName = from_name, authorEmail = from_email, comment = message)
        new_comment.save()
        try:
            send_mail(f'{from_name} ???????????????? ?????????????????????? ?? ?????????? {from_email} ?? ?????????? {sort}', message, DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
        except BadHeaderError:
            return HttpResponse('???????????? ?? ???????? ????????????.')
    return JsonResponse(from_name, safe=False)

######## ?????????????????????? html ###########################
def YandexVerification(request):
    return render(request, 'ls/yandex_151139b8777d3ae8.html')
