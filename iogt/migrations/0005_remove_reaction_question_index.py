# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-16 07:12
from __future__ import unicode_literals

from django.db import migrations
from django.core.management.sql import emit_post_migrate_signal


def remove_reaction_question_index(apps, schema_editor):
    """ Search for the Reaction Question Index then delete it """

    db_alias = schema_editor.connection.alias
    emit_post_migrate_signal(2, False, db_alias)

    ReactionQuestionIndexPage = apps.get_model(
        'core', 'ReactionQuestionIndexPage')
    ReactionQuestionIndexPage.objects.using(db_alias).all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0060_reaction_questions_index_page'),
        ('iogt', '0004_create_me_expert'),
    ]

    operations = [
        migrations.RunPython(remove_reaction_question_index)
    ]
