# Generated by Django 2.0.3 on 2018-04-11 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geocontext', '0014_auto_20180411_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contextserviceregistry',
            name='query_url',
            field=models.CharField(blank=True, help_text='Query URL for accessing Context Service.', max_length=1000, null=True),
        ),
    ]