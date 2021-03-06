# Generated by Django 3.0.8 on 2020-09-16 01:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Piado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.CharField(max_length=400)),
                ('data_criacao', models.DateTimeField(auto_now=True)),
                ('comentario_hospedeiro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='piado.Piado')),
                ('curtidas', models.ManyToManyField(blank=True, related_name='curtidas', to=settings.AUTH_USER_MODEL)),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='piados', to=settings.AUTH_USER_MODEL)),
                ('repiado_hospedeiro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='repiados', to='piado.Piado')),
            ],
            options={
                'ordering': ['-data_criacao'],
            },
        ),
    ]
