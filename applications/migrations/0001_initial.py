# Generated by Django 4.1 on 2022-10-02 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('wallet_address', models.CharField(max_length=100)),
                ('wallet_balance', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('application_text', models.CharField(max_length=500)),
                ('link1', models.URLField(blank=True, null=True)),
                ('link2', models.URLField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('suggestions', models.CharField(max_length=500)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('under_review', models.BooleanField(default=False)),
            ],
        ),
    ]
