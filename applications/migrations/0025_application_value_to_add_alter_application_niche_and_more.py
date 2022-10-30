# Generated by Django 4.1 on 2022-10-29 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0024_application_avatar_url_alter_application_niche_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='value_to_add',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='niche',
            field=models.CharField(blank=True, choices=[('AR', 'Artist'), ('IF', 'Influencer'), ('CB', 'Community Builders'), ('NM', 'Normie'), ('DV', 'Developer'), ('PF', 'Project Founder')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Wl', 'Waitlist'), ('RJ', 'Rejected'), ('AC', 'Accepted'), ('UR', 'Under Review'), ('NA', 'Not Applied')], default='NA', max_length=2),
        ),
    ]