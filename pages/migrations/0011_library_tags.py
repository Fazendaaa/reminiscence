# Generated by Django 2.0.7 on 2018-08-02 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_usersettings_auto_archieve'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='tags',
            field=models.CharField(max_length=4096, null=True),
        ),
    ]