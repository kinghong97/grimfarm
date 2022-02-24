# Generated by Django 4.0.2 on 2022-02-24 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drawing', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawingmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='drawingmodel',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
