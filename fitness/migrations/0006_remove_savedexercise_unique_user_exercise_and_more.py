# Generated by Django 5.1.6 on 2025-05-08 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0005_alter_savedexercise_unique_together_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='savedexercise',
            name='unique_user_exercise',
        ),
        migrations.RemoveField(
            model_name='savedexercise',
            name='exercise',
        ),
        migrations.AddField(
            model_name='savedexercise',
            name='exercise_id',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
