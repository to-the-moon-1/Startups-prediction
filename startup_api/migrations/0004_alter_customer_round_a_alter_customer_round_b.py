# Generated by Django 4.1.2 on 2022-10-19 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup_api', '0003_alter_customer_avg_members_alter_customer_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='round_a',
            field=models.BooleanField(default=False, max_length=7),
        ),
        migrations.AlterField(
            model_name='customer',
            name='round_b',
            field=models.BooleanField(default=False, max_length=7),
        ),
    ]
