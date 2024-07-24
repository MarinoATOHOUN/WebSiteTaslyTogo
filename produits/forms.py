from django import forms
from django_countries.fields import CountryField


class contact_us(forms.Form):
    nom = forms.CharField(required=True, 
                          max_length=100,
                          label="Nom & Prenoms",
                          error_messages={
                              "required": "Veillez remplire ce champ"
                              }
                        )
    
    email = forms.EmailField(required=False,
                             label="Adresse email",
                            )
    
    numero_telephone = forms.IntegerField(required=True,
                                          label="Numéro de téléphone",
                                          error_messages={
                                              "required":"Veillez entrer votre numéro de téléphone"
                                          })

    pays = CountryField().formfield()


class formPaiements(forms.Form):
    nom = forms.CharField(required=True,
                          max_length=100,
                          error_messages={
                              "required": "Veillez Entrer un nom valide"
                          })
    prenom = forms.CharField(required=True,
                             max_length=100,
                             error_messages={
                                 "required": "Veillez Entrer un prenom valide"
                             })
    email = forms.EmailField(required=False)
    contact = forms.IntegerField(required=True,
                                 error_messages={
                                     "required": "Veillez Entrer un numéro de téléphone valide. Ex: +22959037170"
                                 })
    addresse_detaille = forms.CharField(required=False)
    pays = forms.CharField(required=True,
                           max_length=100,
                           error_messages={
                               "required": "Veillez Entrer un Pays valide"
                           })
    ville = forms.CharField(required=True,
                            max_length=100,
                            error_messages={
                                "required": "Veillez Entrer une ville valide"
                            })
    codepostal = forms.CharField(required=False, max_length=100)
    produit = forms.CharField(required=True)
    prix = forms.IntegerField(required=True)


class formservices_paiement(forms.Form):
    s_nom = forms.CharField(required=True,
                          max_length=100,
                          error_messages={
                              "required": "Veillez Entrer un nom valide"
                          })
    s_prenom = forms.CharField(required=True,
                             max_length=100,
                             error_messages={
                                 "required": "Veillez Entrer un prenom valide"
                             })
    s_contact = forms.IntegerField(required=True,
                                 error_messages={
                                     "required": "Veillez Entrer un numéro de téléphone valide. Ex: +22959037170"
                                 })
    s_date_service = forms.CharField(required=True,
                                   max_length=100,
                                   error_messages={
                                       "required": "Veillez Entrer une date valide"
                                   })
    s_pays = forms.CharField(required=True,
                           max_length=100,
                           error_messages={
                               "required": "Veillez Entrer un Pays valide"
                           })
    s_ville = forms.CharField(required=True,
                            max_length=100,
                            error_messages={
                                "required": "Veillez Entrer une ville valide"
                            })
    s_services = forms.CharField(required=True)
    s_prix = forms.IntegerField(required=True)
