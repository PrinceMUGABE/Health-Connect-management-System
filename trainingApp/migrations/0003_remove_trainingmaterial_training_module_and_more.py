# Generated by Django 5.0.7 on 2024-10-26 02:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainingApp', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingmaterial',
            name='training',
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='trainingApp.training')),
            ],
        ),
        migrations.AddField(
            model_name='trainingmaterial',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='trainingApp.module'),
        ),
    ]
