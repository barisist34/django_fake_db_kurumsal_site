from django.shortcuts import render
from django.http import HttpResponse
from random import randint

def home(request):
    # print("request.META:::",request.META)
    #print("request.HEADER:::",request.HEADERS)
    page_title="Anasayfa"
    hero_content="        Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus veniam exercitationem excepturi molestiae libero vel praesentium in culpa recusandae, alias, quasi fuga laborum quos, repellat obcaecati provident eius aut! Sequi natus ipsam et magni amet rem omnis cupiditate alias ratione. Eligendi accusamus, consequatur dignissimos deleniti quos cupiditate eos facere! Ipsam sint repudiandae "
    # context={"platform":f"Django platformu kullanildi,randint donen veri: {randint(1,100)}"}
    context=dict(page_title=page_title,hero_content=hero_content)
    #context={}
    return render(request,"page/home_page.html",context)
    #return HttpResponse("baris")

def oylesine_view(request):
    return HttpResponse("oylesine sayfasi")

def contact_us(request):
    page_title="İletisim"
    hero_content="        Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus veniam exercitationem excepturi molestiae libero vel praesentium in culpa recusandae, alias, quasi fuga laborum quos, repellat obcaecati provident eius aut! Sequi natus ipsam et magni amet rem omnis cupiditate alias ratione. Eligendi accusamus, consequatur dignissimos deleniti quos cupiditate eos facere! Ipsam sint repudiandae "
    context=dict(page_title=page_title,hero_content=hero_content)
    return render (request,"page/contact_us.html",context)

def vision_us(request):
    page_title="Vizyonumuz"
    context=dict(page_title=page_title)
    return render (request,"page/vision.html",context)

def about_us(request):
    page_title="Hakkimizda"
    hero_content="        Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus veniam exercitationem excepturi molestiae libero vel praesentium in culpa recusandae, alias, quasi fuga laborum quos, repellat obcaecati provident eius aut! Sequi natus ipsam et magni amet rem omnis cupiditate alias ratione. Eligendi accusamus, consequatur dignissimos deleniti quos cupiditate eos facere! Ipsam sint repudiandae "
    context=dict(page_title=page_title,hero_content=hero_content)
    return render (request,"page/about_us.html",context)
