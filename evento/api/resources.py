from tastypie.resources import ModelResource
from tastypie import fields, utils
from evento.models import *
from django.contrib.auth.models import User
from tastypie.authorization import Authorization

class TipoInscricaoResource(ModelResource):
    class Meta:
        queryset = TipoInscricao.objects.all()
        allowed_methods = ['get', 'post', 'delete','put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith', 'endswith', 'contains',) # pra ser igual a palavra usa =    pra ser startswith usa __nome do metodo  e assim por diante
        }


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password', 'is_active']

class PessoaFisicaResource(ModelResource):
    class Meta:
        queryset = PessoaFisica.objects.all()
        allowed_methods = ['get', 'post', 'delete','put']
        authorization = Authorization()
        filtering = {'cpf':('exact', 'startswith', 'endswith', 'contains')}



class PessoaResource(ModelResource):
    class Meta:
        queryset = Pessoa.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization= Authorization()
        filtering = {'nome':('exact', 'startswith', 'endswith', 'contains')}


class PessoaJuridicaResource(ModelResource):
    class Meta:
        queryset = PessoaJuridica.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization = Authorization()
        filtering = {'cnpj':('exact', 'startswith', 'endswith', 'contains')}


class EventoResource(ModelResource):
    realizador = fields.ToOneField(PessoaResource, 'realizador')
    class Meta:
        queryset = Evento.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization=Authorization()
        filtering = {'palavrasChave' : ('exact', 'startswith', 'contains')}

class EventoCientificoResource(ModelResource):
    class Meta:
        queryset = EventoCientifico.objects.all()
        allowed_methods = ['get','put','post','delete']
        authorization=Authorization()
        filtering = {'issn' : ('exact', 'startswith', 'contains, endswith')}

class ArtigoAutorResource(ModelResource):
    class Meta:
        queryset = ArtigoAutor.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization=Authorization()
        filtering = {'palavrasChave' : ('exact', 'startswith', 'contains')}

class ArtigoCientificoResource(ModelResource):
    class Meta:
        queryset = ArtigoCientifico.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization=Authorization()
        filtering = {'titulo': ('exact', 'startswith', 'endswith, contains')}

class InscricaoResource(ModelResource):
    pessoa = fields.ToOneField(PessoaFisicaResource, 'pessoa') # ToOneField = de 1 pra 1 toManyField = de 1 pra muitos
    evento = fields.ToOneField(EventoResource,'evento')
    tipoInscricao = fields.ToOneField(TipoInscricaoResource,'tipoInscricao')
    class Meta:
        queryset = Inscricoes.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization=Authorization()
        filtering = {'cpf': ('exact', 'startswith', 'endswith, contains')}
