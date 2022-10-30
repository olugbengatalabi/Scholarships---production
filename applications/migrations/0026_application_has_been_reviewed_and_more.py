# Generated by Django 4.1 on 2022-10-29 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0025_application_value_to_add_alter_application_niche_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='has_been_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='niche',
            field=models.CharField(blank=True, choices=[('IF', 'Influencer'), ('PF', 'Project Founder'), ('DV', 'Developer'), ('CB', 'Community Builders'), ('NM', 'Normie'), ('AR', 'Artist')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Wl', 'Waitlist'), ('RJ', 'Rejected'), ('AC', 'Accepted'), ('NA', 'Not Applied'), ('UR', 'Under Review')], default='NA', max_length=2),
        ),
    ]