# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtigoAutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ArtigoCientifico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='titulo')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='nome')),
                ('eventoPrincipal', models.CharField(max_length=200, verbose_name='eventoPrincipal')),
                ('sigla', models.CharField(max_length=20, verbose_name='sigla')),
                ('dataEHoraDeInicio', models.DateTimeField(default=django.utils.timezone.now, verbose_name='dataEHoraDeInicio')),
                ('palavrasChave', models.CharField(max_length=200, verbose_name='palavrasChave')),
                ('logotipo', models.CharField(max_length=200, verbose_name='logotipo')),
                ('cidade', models.TextField(blank=True, null=True, verbose_name='cidade')),
                ('uf', models.CharField(max_length=2, verbose_name='uf')),
                ('endereco', models.TextField(blank=True, null=True, verbose_name='endereco')),
                ('cep', models.TextField(blank=True, null=True, verbose_name='cep')),
            ],
        ),
        migrations.CreateModel(
            name='Inscricoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataEHoraDaInscricao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='dataEHoraDaInscricao')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='nome')),
                ('email', models.CharField(max_length=200, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='TipoInscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, verbose_name='descricao')),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='evento.Pessoa')),
                ('curriculo', models.CharField(max_length=200, verbose_name='curriculo')),
            ],
            bases=('evento.pessoa',),
        ),
        migrations.CreateModel(
            name='EventoCientifico',
            fields=[
                ('evento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='evento.Evento')),
                ('issn', models.CharField(max_length=200, verbose_name='issn')),
            ],
            bases=('evento.evento',),
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='evento.Pessoa')),
                ('cpf', models.CharField(max_length=20, verbose_name='cpf')),
            ],
            bases=('evento.pessoa',),
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='evento.Pessoa')),
                ('cnpj', models.CharField(max_length=100, verbose_name='cnpj')),
                ('razaoSocial', models.CharField(max_length=200, verbose_name='razaoSocial')),
            ],
            bases=('evento.pessoa',),
        ),
        migrations.AddField(
            model_name='inscricoes',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.Evento'),
        ),
        migrations.AddField(
            model_name='inscricoes',
            name='tipoInscricao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.TipoInscricao'),
        ),
        migrations.AddField(
            model_name='evento',
            name='realizador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.Pessoa'),
        ),
        migrations.AddField(
            model_name='artigoautor',
            name='artigoCientifico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.ArtigoCientifico'),
        ),
        migrations.AddField(
            model_name='inscricoes',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.PessoaFisica'),
        ),
        migrations.AddField(
            model_name='artigocientifico',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.EventoCientifico'),
        ),
        migrations.AddField(
            model_name='artigoautor',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.Autor'),
        ),
    ]
