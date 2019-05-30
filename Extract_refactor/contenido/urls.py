
from django.urls import path
from rest_framework.documentation import include_docs_urls

from .views import AnuncioInferiorView, AnuncioLateralView, AnuncioSuperiroView, BonosView, ExplicacionInicio, \
    QuienesSomosView, FaqsView, ExplicacionScrapyView, AndroidIndex

urlpatterns = [

    path('anunciosuperior/', AnuncioSuperiroView.as_view(), name='anuncio_superior'),
    path('anunciolateral/', AnuncioLateralView.as_view(), name='anuncio_lateral'),
    path('anunioinferior/', AnuncioInferiorView.as_view(), name='anunio_inferior'),
    path('bonos/', BonosView.as_view(), name='bonos'),
    path('explicacion-inicio/', ExplicacionInicio.as_view(), name='contenido_inicio'),
    path('explicacion-scrapy/', ExplicacionScrapyView.as_view(), name='contenido_inicio'),
    path('quien-somos/', QuienesSomosView.as_view(), name='quienSomos'),
    path('faqs/', FaqsView.as_view(), name='faqs'),
    path('.well-known/assetlinks.json/', AndroidIndex.as_view() , name='faqs'),

]