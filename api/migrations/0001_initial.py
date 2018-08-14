# Generated by Django 2.1 on 2018-08-14 15:27

import app.validators
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
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images_quantity', models.PositiveSmallIntegerField(verbose_name='cantidad de imágenes')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Pendiente'), (2, 'Completado')], default=2, verbose_name='estado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='creado por')),
            ],
            options={
                'ordering': ('created_by',),
            },
        ),
        migrations.CreateModel(
            name='TicketImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=255, upload_to='', validators=[app.validators.FileSizeValidator(4000)])),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Ticket')),
            ],
            options={
                'ordering': ('ticket',),
            },
        ),
    ]