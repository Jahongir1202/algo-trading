# Generated by Django 4.2.7 on 2023-11-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0010_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="mijoz",
            name="comment",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name="Comment",
        ),
    ]
