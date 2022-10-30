# Generated by Django 4.1 on 2022-10-09 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0006_alter_application_niche_alter_application_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'ordering': ['-date_submitted']},
        ),
        migrations.AlterField(
            model_name='application',
            name='niche',
            field=models.CharField(blank=True, choices=[('DV', 'Developer'), ('CB', 'Community Builders'), ('AR', 'Artist')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.TextField(blank=True, choices=[('AC', 'Accepted'), ('Wl', 'Waitlist'), ('UR', 'Under Review'), ('RJ', 'Rejected')], max_length=2, null=True),
        ),
    ]