# Generated by Django 4.1.3 on 2022-12-10 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_newsstory_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsstory',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AddField(
            model_name='newsstory',
            name='image_url',
            field=models.URLField(null=True),
        ),
    ]