# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-13 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_project_classifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='classifier',
            field=models.CharField(choices=[('logistic_regression', 'Logistic Regression (default)'), ('svm', 'Nonlinear Support Vector Machine (SVM)'), ('lsvm', 'Linear Support Vector Machine (SVM)'), ('random_forest', 'Random Forest')], default='logistic_regression', max_length=19),
        ),
    ]
