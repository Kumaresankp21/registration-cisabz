# Generated by Django 5.1 on 2024-10-08 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0012_team_remove_registration_member2_email_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="registration",
            name="payment_link",
        ),
        migrations.RemoveField(
            model_name="registration",
            name="transaction_number",
        ),
        migrations.RemoveField(
            model_name="registration",
            name="whatsapp_group_link",
        ),
    ]
