# Generated by Django 5.0.1 on 2024-01-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile_Number', models.CharField(max_length=15)),
                ('Website_Url', models.URLField()),
                ('Page_Url', models.URLField()),
                ('Date', models.CharField(max_length=15)),
                ('Time', models.CharField(max_length=15)),
                ('Lead_ID', models.CharField(max_length=50)),
                ('Referral_information_field', models.TextField()),
                ('Visitor_came_from', models.CharField(max_length=100)),
                ('utm_source', models.CharField(max_length=50)),
                ('utm_medium', models.CharField(max_length=50)),
                ('utm_campaign', models.CharField(max_length=50)),
                ('Last_visited_pages', models.TextField()),
            ],
        ),
    ]