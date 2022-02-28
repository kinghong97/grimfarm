# Generated by Django 4.0.2 on 2022-02-25 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drawing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(max_length=30)),
                ('drawing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drawing.drawingmodel')),
            ],
            options={
                'db_table': 'notification',
            },
        ),
    ]
