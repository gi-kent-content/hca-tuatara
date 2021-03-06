# Generated by Django 2.1 on 2019-10-08 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hcat', '0015_auto_20191008_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='sheet_that_validated',
            new_name='sheet_submitted',
        ),
        migrations.AlterField(
            model_name='project',
            name='staging_area',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Staging S3 bucket'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tAndC_comments',
            field=models.CharField(blank=True, max_length=255, verbose_name='T&C'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tAndC_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='T&C date'),
        ),
    ]
