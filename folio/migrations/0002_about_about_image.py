# Generated by Django 4.2.5 on 2023-09-16 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='about_image',
            field=models.ImageField(default='folio/images/default.jpg', upload_to='folio/images/'),
        ),
    ]
