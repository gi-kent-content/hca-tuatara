# Generated by Django 2.1 on 2020-12-10 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hcat', '0025_auto_20201204_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='array_express_accession',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='cirm_accession',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='dbGap_accession',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='ega_study_accesion',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='ena_accession',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='geo_series',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='ncbi_bioproject_accession',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='sra_accession',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='file_bucket',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='File bucket'),
        ),
    ]