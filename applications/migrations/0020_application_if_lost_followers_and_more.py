# Generated by Django 4.1 on 2022-10-24 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0019_alter_application_niche_alter_application_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='if_lost_followers',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='niche',
            field=models.CharField(blank=True, choices=[('IF', 'Influencer'), ('DV', 'Developer'), ('NM', 'Normie'), ('PF', 'Project Founder'), ('AR', 'Artist'), ('CB', 'Community Builders')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('RJ', 'Rejected'), ('UR', 'Under Review'), ('Wl', 'Waitlist'), ('NA', 'Not Applied'), ('AC', 'Accepted')], default='NA', max_length=2),
        ),
    ]