# Generated by Django 5.1 on 2024-10-02 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_registration_department_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="registration",
            old_name="name",
            new_name="leader_name",
        ),
        migrations.RemoveField(
            model_name="registration",
            name="non_technical_events",
        ),
        migrations.RemoveField(
            model_name="registration",
            name="technical_events",
        ),
        migrations.AddField(
            model_name="registration",
            name="member2_email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="registration",
            name="member2_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="registration",
            name="member2_non_technical_events",
            field=models.ManyToManyField(
                blank=True,
                related_name="member2_non_technical_registrations",
                to="app.event",
            ),
        ),
        migrations.AddField(
            model_name="registration",
            name="member2_phone",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="registration",
            name="member2_technical_events",
            field=models.ManyToManyField(
                blank=True,
                related_name="member2_technical_registrations",
                to="app.event",
            ),
        ),
        migrations.AddField(
            model_name="registration",
            name="member3_email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="registration",
            name="member3_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="registration",
            name="member3_non_technical_events",
            field=models.ManyToManyField(
                blank=True,
                related_name="member3_non_technical_registrations",
                to="app.event",
            ),
        ),
        migrations.AddField(
            model_name="registration",
            name="member3_phone",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="registration",
            name="member3_technical_events",
            field=models.ManyToManyField(
                blank=True,
                related_name="member3_technical_registrations",
                to="app.event",
            ),
        ),
        migrations.AddField(
            model_name="registration",
            name="paper_id",
            field=models.CharField(
                default="CISABZ/CSE/00", editable=False, max_length=20, unique=True
            ),
        ),
        migrations.AddField(
            model_name="registration",
            name="team_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="registration",
            name="department",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="registration",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="registration",
            name="phone",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
