# Generated by Django 2.2.15 on 2020-10-17 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import storages.backends.s3boto3


class Migration(migrations.Migration):

    dependencies = [
        ('cuser', '0007_auto_20201006_1527'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-email']},
        ),
        migrations.CreateModel(
            name='Post_book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('img', models.ImageField(storage=storages.backends.s3boto3.S3Boto3Storage(bucket_name='book-post-images'), upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
