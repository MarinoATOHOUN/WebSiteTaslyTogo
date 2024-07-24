from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from produits.models import produits
from produits.models import contact
from about.models import entete
from team.models import personnel
from services.models import services
from produits.forms import contact_us
from produits.forms import formservices_paiement
from produits.forms import formPaiements
from about.models import evenements
from about.models import tutos
from about.models import podcasts
from about.models import exploits
from about.models import form_img
from about.models import info_adhesion
from paiement.models import Paiements, services_paiement

#menu format telephone


def tuto_audio(request):
    podcast = podcasts.objects.all()
    entetes = entete.objects.all()
    research = request.GET.get('audio-search')
    if research != '' and research is not None:
        podcast = podcasts.objects.filter(titre__icontains=research)
    return render(request, "produits/TutoAudio.html", {'podcast': podcast,
                                                       'entete': entetes[0]})


def validation_paiement(request):
    return render(request, 'produits/validation.html')

def Services(request):
    service = services.objects.all()
    entetes = entete.objects.all()
    research = request.GET.get('service-search')
    if research != '' and research is not None:
        service = services.objects.filter(nom__icontains=research)
    return render(request, "produits/services.html", {'service': service,
                                                      'entete': entetes[0]})

def tuto_video(request):
    tuto = tutos.objects.all()
    entetes = entete.objects.all()
    research = request.GET.get('video-search')
    if research != '' and research is not None:
        tuto = tutos.objects.filter(titre__icontains=research)
    return render(request, "produits/Tuto-Video.html", {'tuto': tuto,
                                                        'entete': entetes[0]})

def details(request):
    entetes = entete.objects.all()
    produit = produits.objects.all()
    research = request.GET.get('product-search')
    if research != '' and research is not None:
        produit = produits.objects.filter(nom__icontains=research)
    return render(request, "produits/detail.html", {"produits": produit,
                                                    'entete': entetes[0]})

def prod_paiement(request, id):
    if request.method == 'POST':
        form = formPaiements(request.POST)
        if form.is_valid():
            Paiements.objects.create(
            nom = form.cleaned_data['nom'],
            prenom = form.cleaned_data['prenom'],
            email = form.cleaned_data['email'],
            contact = form.cleaned_data['contact'],
            addresse_detaille = form.cleaned_data['addresse_detaille'],
            pays = form.cleaned_data['pays'],
            ville = form.cleaned_data['ville'],
            codepostal = form.cleaned_data['codepostal'],
            produit = form.cleaned_data['produit'],
            prix = form.cleaned_data['prix']
            )
            return redirect('Validations')
    else:
        form = formPaiements()
    entetes = entete.objects.all()
    prod = produits.objects.get(id=id)
    return render(request, 'produits/paiement.html', {'prod': prod,
                                                      'entete': entetes[0],
                                                      'form': form})

def service_paiement(request, id):
    if request.method == 'POST':
        form = formservices_paiement(request.POST)
        if form.is_valid():
            services_paiement.objects.create(
                s_nom = form.cleaned_data['s_nom'],
                s_prenom = form.cleaned_data['s_prenom'],
                s_contact = form.cleaned_data['s_contact'],
                s_date_service = form.cleaned_data['s_date_service'],
                s_pays = form.cleaned_data['s_pays'],
                s_ville = form.cleaned_data['s_ville'],
                s_services = form.cleaned_data['s_services'],
                s_prix = form.cleaned_data['s_prix']
            )
        return redirect('Validations')
    else:
        form = formservices_paiement()
    entetes = entete.objects.all()
    service = services.objects.get(id=id)
    return render(request, 'produits/service-paiement.html', {'service': service,
                                                              'entete': entetes[0],
                                                              'form': form})

def produit(request):
    produit = produits.objects.all()
    entetes = entete.objects.all()
    personnels = personnel.objects.all()
    service = services.objects.all()
    evenement = evenements.objects.all()
    tuto = tutos.objects.all()
    podcast = podcasts.objects.all()
    exploit = exploits.objects.all()
    form_imgs = form_img.objects.all()
    adhesion = info_adhesion.objects.all()
    form = contact_us()
    paginate = Paginator(produit, 3)
    page = request.GET.get('page')
    produit = paginate.get_page(page)

    if request.method == "POST":
        Input = contact_us(request.POST)
        if Input.is_valid():
            dataform = Input.cleaned_data
            modelinstance = contact.objects.create(**dataform)
            modelinstance.save()
    else:
        Input = contact()

    return render(request, "produits/index.html", {'produits': produit,
                                                   'entete': entetes[0],
                                                   'personnel': personnels,
                                                   'service': service,
                                                   'form': form,
                                                   'evenement': evenement[0],
                                                   'tuto': tuto,
                                                   'podcast': podcast,
                                                   'exploit': exploit,
                                                   'form_img': form_imgs[0],
                                                   'adhesion': adhesion[0]})



