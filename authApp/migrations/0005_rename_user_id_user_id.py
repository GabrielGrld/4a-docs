# Generated by Django 3.2.8 on 2021-10-13 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0004_alter_user_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_id',
            new_name='id',
        ),
    ]
