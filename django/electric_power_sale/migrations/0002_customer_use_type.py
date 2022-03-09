# Generated by Django 3.2.12 on 2022-03-02 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electric_power_sale', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='use_type',
            field=models.CharField(choices=[('use_type_common', '常规'), ('use_type_seprate_time', '常规-分时段'), ('use_type_common_high_power', '常规-高耗能'), ('use_type_high_power_seprate_time', '高耗能-分时段')], default='use_type_common', max_length=80, verbose_name='客户用电性质'),
        ),
    ]