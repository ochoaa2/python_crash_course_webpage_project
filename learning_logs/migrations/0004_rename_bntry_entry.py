# Generated by Django 4.2.8 on 2023-12-24 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_rename_entry_bntry'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bntry',
            new_name='Entry',
        ),
    ]
