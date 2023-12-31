# Generated by Django 4.2.5 on 2023-09-17 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0004_project_start_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('main_tech', models.CharField(max_length=200)),
                ('technologies', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='folio.project'),
        ),
    ]
