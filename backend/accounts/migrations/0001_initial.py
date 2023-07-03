# Generated by Django 4.2.2 on 2023-06-19 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(editable=False, max_length=254, unique=True, verbose_name='email address')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_vet', models.BooleanField(blank=True, default=False, null=True)),
                ('profile_img', models.ImageField(default='profile/default.png', upload_to='profile/')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('species', models.CharField(blank=True, max_length=255, null=True)),
                ('birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', '수컷'), ('F', '암컷')], max_length=1)),
                ('is_neu', models.BooleanField(default=False)),
                ('adoption_date', models.DateField(blank=True, db_column='adoptionDate', null=True)),
                ('ownerid', models.ForeignKey(db_column='ownerID', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'pet',
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hos_name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('officenumber', models.CharField(blank=True, db_column='officeNumber', max_length=255, null=True)),
                ('introduction', models.CharField(blank=True, max_length=255, null=True)),
                ('hos_profile_img', models.ImageField(default='profile_hos/default.png', upload_to='profile_hos/')),
                ('user_id', models.OneToOneField(db_column='user_id', editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'hospital',
            },
        ),
    ]