from django.shortcuts import render
from django.http import HttpResponse
from random import randint

FAKE_DB_PROJECTS= [f"https://picsum.photos/id/{id}/100/80" for id in range(21,28)]
#8 adet resim adresi
FAKE_DB_CAROUSEL=[
    f"https://picsum.photos/id/{id}/1200/300" for id in range(24,28)
]
# <div class="carousel-indicators"> de 4 adet slide tanimli oldugu icin 24-28 4 adet adres tanimlanmali,yoksa hatali calisir.

def home(request):
    # print("request.META:::",request.META)
    #print("request.HEADER:::",request.HEADERS)
    page_title="Anasayfa"
    hero_content="        Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus veniam exercitationem excepturi molestiae libero vel praesentium in culpa recusandae, alias, quasi fuga laborum quos, repellat obcaecati provident eius aut! Sequi natus ipsam et magni amet rem omnis cupiditate alias ratione. Eligendi accusamus, consequatur dignissimos deleniti quos cupiditate eos facere! Ipsam sint repudiandae "
    # context={"platform":f"Django platformu kullanildi,randint donen veri: {randint(1,100)}"}
    context=dict(page_title=page_title,hero_content=hero_content,FAKE_DB_CAROUSEL=FAKE_DB_CAROUSEL)
    context['FAKE_DB_PROJECTS']=FAKE_DB_PROJECTS
    #context={}
    return render(request,"page/home_page.html",context)
    #return HttpResponse("baris")

def oylesine_view(request):
    return HttpResponse("oylesine sayfasi")

def contact_us(request):
    page_title="İletisim"
    hero_content="        Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus veniam exercitationem excepturi molestiae libero vel praesentium in culpa recusandae, alias, quasi fuga laborum quos, repellat obcaecati provident eius aut! Sequi natus ipsam et magni amet rem omnis cupiditate alias ratione. Eligendi accusamus, consequatur dignissimos deleniti quos cupiditate eos facere! Ipsam sint repudiandae "
    context=dict(page_title=page_title,hero_content=hero_content,FAKE_DB_PROJECTS=FAKE_DB_PROJECTS)
    return render (request,"page/contact_us.html",context)

def vision_us(request):
    page_title="Vizyonumuz"
    context=dict(page_title=page_title)
    context['FAKE_DB_PROJECTS']=FAKE_DB_PROJECTS
    return render (request,"page/vision.html",context)

def about_us(request):
    page_title="Hakkimizda"
    hero_content="        Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus veniam exercitationem excepturi molestiae libero vel praesentium in culpa recusandae, alias, quasi fuga laborum quos, repellat obcaecati provident eius aut! Sequi natus ipsam et magni amet rem omnis cupiditate alias ratione. Eligendi accusamus, consequatur dignissimos deleniti quos cupiditate eos facere! Ipsam sint repudiandae "
    context=dict(page_title=page_title,hero_content=hero_content,FAKE_DB_PROJECTS=FAKE_DB_PROJECTS)
    return render (request,"page/about_us.html",context)
