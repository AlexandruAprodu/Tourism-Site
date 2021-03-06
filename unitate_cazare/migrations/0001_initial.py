# Generated by Django 3.0.7 on 2020-09-08 13:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Judete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judet', models.CharField(max_length=100)),
                ('imagine_judet', models.ImageField(default=None, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='UnitateCazare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip_proprietate', models.CharField(choices=[('APARTAMENT', 'apartament'), ('CABANA', 'cabana'), ('COMPLEX TURISTIC', 'complex turistic'), ('HOTEL', 'hotel'), ('HOSTEL', 'hostel')], max_length=40)),
                ('nume_proprietate', models.CharField(max_length=100)),
                ('localitatea', models.CharField(max_length=50)),
                ('strada', models.CharField(choices=[('STRADA', 'strada'), ('BULEVARD', 'bulevard'), ('ALEEA', 'aleea'), ('SOSEAUA', 'soseaua'), ('FUNDATURA', 'fundatura')], default='STRADA', max_length=40)),
                ('numele_strazii', models.CharField(max_length=100)),
                ('numar', models.IntegerField()),
                ('nr_total_camere', models.IntegerField()),
                ('nr_total_locuri', models.IntegerField()),
                ('descriere_proprietate', models.TextField()),
                ('forma_client', models.CharField(choices=[('SRL', 'srl'), ('SA', 'sa'), ('PFA', 'pfa'), ('PF', 'persoana fizica')], default='SRL', max_length=40)),
                ('nume_client', models.CharField(max_length=100)),
                ('numar_telefon', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email_client', models.EmailField(max_length=254)),
                ('poza_prezentare', models.ImageField(default=None, upload_to='media')),
                ('judet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='unitate_cazare.Judete')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media', verbose_name='Image')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='unitate_cazare.UnitateCazare')),
            ],
        ),
    ]
