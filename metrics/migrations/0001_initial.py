# Generated by Django 2.2.6 on 2019-10-07 20:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('qr', '0002_videoqrcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ip', models.GenericIPAddressField()),
                ('device', models.CharField(max_length=150)),
                ('os', models.CharField(max_length=150)),
                ('browser', models.CharField(max_length=150)),
                ('qrcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qr.QrCode')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]