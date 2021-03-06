# Generated by Django 2.0.6 on 2019-12-20 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('current_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('DateOfBirth', models.DateTimeField(null=True)),
                ('Profile_Picture', models.ImageField(blank=True, null=True, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Stylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ForeignKey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Time', models.DateTimeField(auto_now_add=True)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PrimpApp.Stylist')),
            ],
        ),
    ]
