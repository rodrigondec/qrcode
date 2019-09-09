# Generated by Django 2.2.3 on 2019-09-09 19:42

from django.db import migrations, models
import logos.utils
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to=logos.utils.get_img_path)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
