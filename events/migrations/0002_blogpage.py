# Generated by Django 2.2.4 on 2019-08-13 19:33

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('date', models.DateField(verbose_name='Event date')),
                ('place', models.CharField(max_length=250)),
                ('agenda', models.CharField(max_length=250)),
                ('notes', wagtail.core.fields.RichTextField(blank=True)),
                ('resources', wagtail.core.fields.RichTextField(blank=True)),
                ('attended', models.IntegerField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
