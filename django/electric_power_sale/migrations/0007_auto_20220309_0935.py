# Generated by Django 3.2.12 on 2022-03-09 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import electric_power_sale.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0008_auto_20220309_0900'),
        ('electric_power_sale', '0006_auto_20220309_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='MthAgentBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mth', models.IntegerField(default=electric_power_sale.models.default_cur_mth, verbose_name='月份')),
                ('state', models.CharField(default='draft', max_length=40, verbose_name='状态')),
                ('note', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('created_at', models.DateTimeField(default=electric_power_sale.models.default_cur_datetime, verbose_name='录入时间')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='录入人')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.organization', verbose_name='所属机构')),
            ],
        ),
        migrations.CreateModel(
            name='MthCustomerBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mth', models.IntegerField(default=electric_power_sale.models.default_cur_mth, verbose_name='月份')),
                ('state', models.CharField(default='draft', max_length=40, verbose_name='状态')),
                ('note', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('created_at', models.DateTimeField(default=electric_power_sale.models.default_cur_datetime, verbose_name='录入时间')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='录入人')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.organization', verbose_name='所属机构')),
            ],
        ),
        migrations.CreateModel(
            name='MthDiffCustomerBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mth', models.IntegerField(default=electric_power_sale.models.default_cur_mth, verbose_name='月份')),
                ('state', models.CharField(default='draft', max_length=40, verbose_name='状态')),
                ('note', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('created_at', models.DateTimeField(default=electric_power_sale.models.default_cur_datetime, verbose_name='录入时间')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='录入人')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.organization', verbose_name='所属机构')),
            ],
        ),
        migrations.CreateModel(
            name='MthDraftCustomerBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mth', models.IntegerField(default=electric_power_sale.models.default_cur_mth, verbose_name='月份')),
                ('state', models.CharField(default='draft', max_length=40, verbose_name='状态')),
                ('note', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('created_at', models.DateTimeField(default=electric_power_sale.models.default_cur_datetime, verbose_name='录入时间')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='录入人')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.organization', verbose_name='所属机构')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='transformer_type',
            field=models.CharField(blank=True, choices=[('transformer_type_lt_35', '35KVA以下'), ('transformer_type_lt_35', '35KVA以上')], default='transformer_type_lt_35', max_length=60, null=True, verbose_name='变压器容量类型'),
        ),
        migrations.CreateModel(
            name='MthDraftCustomerBillLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_device_no', models.CharField(max_length=40, verbose_name='户号')),
                ('act_common', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='月结算电量-常规')),
                ('act_flat', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='月结算电量-平时段')),
                ('act_valley', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='月结算电量-谷时段')),
                ('act_peak', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='月结算电量-峰时段')),
                ('state', models.CharField(default='draft', max_length=40, verbose_name='状态')),
                ('note', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='electric_power_sale.customer', verbose_name='关联客户')),
                ('mth_draft_customer_bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electric_power_sale.mthdraftcustomerbill', verbose_name='月度电量确认单主表')),
            ],
        ),
        migrations.CreateModel(
            name='MthDiffCustomerBillLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_device_no', models.CharField(max_length=40, verbose_name='户号')),
                ('plan_common', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='调整前计划电量-常规')),
                ('plan_flat', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='调整前计划电量-平时段')),
                ('plan_valley', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='调整前计划电量-谷时段')),
                ('plan_peak', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='调整前计划电量-峰时段')),
                ('act_common', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='月结算电量-常规')),
                ('act_flat', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='月结算电量-平时段')),
                ('act_valley', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='月结算电量-谷时段')),
                ('act_peak', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='月结算电量-峰时段')),
                ('state', models.CharField(default='draft', max_length=40, verbose_name='状态')),
                ('note', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='electric_power_sale.customer', verbose_name='关联客户')),
                ('mth_diff_customer_bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electric_power_sale.mthdiffcustomerbill', verbose_name='月度电量偏差控制主表')),
            ],
        ),
        migrations.CreateModel(
            name='MthCustomerBillLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_name', models.CharField(max_length=40, verbose_name='合同名称')),
                ('act_common', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='月结算电量-常规')),
                ('act_flat', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='月结算电量-平时段')),
                ('act_valley', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='月结算电量-谷时段')),
                ('act_peak', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='月结算电量-峰时段')),
                ('price_common', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='常规时段电价(元/KWA)')),
                ('price_peak', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='峰时段电价(元/KWA)')),
                ('price_flat', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='平时段电价(元/KWA)')),
                ('price_valley', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='谷时段电价(元/KWA)')),
                ('service_rate', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='代理服务费比例')),
                ('service_fee', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='代理服务费')),
                ('state', models.CharField(default='draft', max_length=40, verbose_name='状态')),
                ('note', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='electric_power_sale.customer', verbose_name='关联客户')),
                ('mth_customer_bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electric_power_sale.mthcustomerbill', verbose_name='月度电量结算单主表')),
            ],
        ),
        migrations.CreateModel(
            name='MthAgentBillLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_common', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='调整前计划电量-常规')),
                ('plan_flat', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='调整前计划电量-平时段')),
                ('plan_valley', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='调整前计划电量-谷时段')),
                ('plan_peak', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='调整前计划电量-峰时段')),
                ('act_common', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='月结算电量-常规')),
                ('act_flat', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='月结算电量-平时段')),
                ('act_valley', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='月结算电量-谷时段')),
                ('act_peak', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='月结算电量-峰时段')),
                ('price_common', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='常规时段电价(元/KWA)')),
                ('price_peak', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='峰时段电价(元/KWA)')),
                ('price_flat', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='平时段电价(元/KWA)')),
                ('price_valley', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='谷时段电价(元/KWA)')),
                ('service_rate', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='代理服务费比例')),
                ('service_fee', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='代理服务费')),
                ('agent_rate', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='居间分成比例')),
                ('agent_fee', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='居间分成金额')),
                ('tax_diff', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='增值税差额')),
                ('act_agent_fee', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='实际结算居间分成费')),
                ('agent_confirm_date', models.DateField(default=electric_power_sale.models.default_cur_date, verbose_name='居间确认时间')),
                ('state', models.CharField(default='draft', max_length=40, verbose_name='状态')),
                ('note', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='electric_power_sale.agent', verbose_name='居间')),
                ('mth_agent_bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electric_power_sale.mthagentbill', verbose_name='月度电量结算单主表')),
            ],
        ),
    ]