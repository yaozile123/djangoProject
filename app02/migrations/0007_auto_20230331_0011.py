# Generated by Django 3.2.18 on 2023-03-31 00:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0006_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department',
            field=models.CharField(max_length=32, unique=True, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.IntegerField(verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Balance'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app02.department', verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, 'male'), (2, 'female')], verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=16, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='pwd',
            field=models.CharField(max_length=32, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='register_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Joining Date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Paid'), (2, 'Unpaid')], verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='task',
            name='detail',
            field=models.TextField(max_length=200, verbose_name='Details'),
        ),
        migrations.AlterField(
            model_name='task',
            name='level',
            field=models.SmallIntegerField(choices=[(1, '紧急'), (2, '普通'), (3, '临时')], verbose_name='Level'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=16, verbose_name='Title'),
        ),
    ]
