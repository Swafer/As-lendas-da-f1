# Generated by Django 5.0.3 on 2024-08-13 23:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_bairro_cargo_cidade_pessoa_tipoimovel_tipologradouro_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Circuito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=50)),
                ('comprimento', models.FloatField(help_text='Comprimento do circuito em km')),
            ],
        ),
        migrations.CreateModel(
            name='Corrida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temporada', models.IntegerField()),
                ('data', models.DateField()),
                ('circuito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.circuito')),
            ],
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Piloto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=50)),
                ('data_nasc', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('valor_contrato', models.DecimalField(decimal_places=2, max_digits=10)),
                ('equipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.equipe')),
            ],
        ),
        migrations.CreateModel(
            name='Temporada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(unique=True)),
                ('campeao_equipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='campeao_equipe', to='app.equipe')),
                ('campeao_piloto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='campeao_piloto', to='app.piloto')),
            ],
        ),
        migrations.CreateModel(
            name='VitoriaF1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_vitorias', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='logradouro',
            name='bairro',
        ),
        migrations.RemoveField(
            model_name='imovel',
            name='bairro',
        ),
        migrations.DeleteModel(
            name='Cargo',
        ),
        migrations.RemoveField(
            model_name='logradouro',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='imovel',
            name='cidade',
        ),
        migrations.DeleteModel(
            name='estado',
        ),
        migrations.RemoveField(
            model_name='imovel',
            name='logradouro',
        ),
        migrations.RemoveField(
            model_name='imovel',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='imovel',
            name='tipo_logradouro',
        ),
        migrations.RemoveField(
            model_name='imovel',
            name='uf',
        ),
        migrations.RemoveField(
            model_name='vendaimovel',
            name='imovel',
        ),
        migrations.RemoveField(
            model_name='locacaoimovel',
            name='imovel',
        ),
        migrations.RemoveField(
            model_name='locatario',
            name='pessoa',
        ),
        migrations.RemoveField(
            model_name='logradouro',
            name='tipo',
        ),
        migrations.AddField(
            model_name='carro',
            name='equipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.equipe'),
        ),
        migrations.AddField(
            model_name='vitoriaf1',
            name='carro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.carro'),
        ),
        migrations.AddField(
            model_name='vitoriaf1',
            name='corrida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.corrida'),
        ),
        migrations.AddField(
            model_name='vitoriaf1',
            name='piloto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.piloto'),
        ),
        migrations.DeleteModel(
            name='Bairro',
        ),
        migrations.DeleteModel(
            name='Cidade',
        ),
        migrations.DeleteModel(
            name='TipoImovel',
        ),
        migrations.DeleteModel(
            name='UF',
        ),
        migrations.DeleteModel(
            name='VendaImovel',
        ),
        migrations.DeleteModel(
            name='Imovel',
        ),
        migrations.DeleteModel(
            name='LocacaoImovel',
        ),
        migrations.DeleteModel(
            name='Locatario',
        ),
        migrations.DeleteModel(
            name='Pessoa',
        ),
        migrations.DeleteModel(
            name='Logradouro',
        ),
        migrations.DeleteModel(
            name='TipoLogradouro',
        ),
    ]
