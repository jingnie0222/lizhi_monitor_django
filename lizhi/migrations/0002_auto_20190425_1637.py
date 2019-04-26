# Generated by Django 2.0.5 on 2019-04-25 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lizhi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resultdetail',
            old_name='fetch_from',
            new_name='bd_res_type',
        ),
        migrations.RenameField(
            model_name='resultdetail',
            old_name='scene',
            new_name='bd_scene',
        ),
        migrations.RenameField(
            model_name='resultdetail',
            old_name='res_type',
            new_name='sg_res_type',
        ),
        migrations.AddField(
            model_name='resultdetail',
            name='sg_scene',
            field=models.CharField(default='', max_length=500),
        ),
    ]
