# Generated by Django 4.0.6 on 2022-11-21 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_member_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='file',
        ),
        migrations.AddField(
            model_name='member',
            name='resume',
            field=models.FileField(default=None, null=True, upload_to='documents/'),
        ),
    ]
