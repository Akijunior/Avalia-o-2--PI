# Generated by Django 2.0.2 on 2018-02-23 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0004_auto_20180222_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_post', models.CharField(max_length=140)),
                ('data_postagem', models.DateField(auto_now_add=True)),
                ('titulo', models.CharField(max_length=80, verbose_name='Título')),
                ('criador_do_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meus_posts', to='perfis.Perfil')),
            ],
        ),
    ]