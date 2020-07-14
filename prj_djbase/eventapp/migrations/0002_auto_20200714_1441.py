# Generated by Django 3.0.8 on 2020-07-14 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='scope',
        ),
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RenameModel(
            old_name='SkillGrid',
            new_name='Category',
        ),
        migrations.DeleteModel(
            name='Scope',
        ),
        migrations.AddField(
            model_name='type',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.Category'),
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(default=999, on_delete=django.db.models.deletion.PROTECT, to='eventapp.Type'),
            preserve_default=False,
        ),
    ]
