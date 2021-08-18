# Generated by Django 3.2.6 on 2021-08-18 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='机构名称')),
                ('address', models.CharField(max_length=200, verbose_name='地址')),
                ('note', models.TextField(verbose_name='备注')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('header', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='负责人')),
                ('parent_org', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.organization', verbose_name='上级机构')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar_url', models.CharField(max_length=200, verbose_name='头像地址')),
                ('note', models.TextField(verbose_name='note')),
                ('default_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group', verbose_name='默认用户组')),
                ('default_org', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.organization', verbose_name='默认机构')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
