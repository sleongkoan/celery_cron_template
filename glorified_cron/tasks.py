# -*- coding: utf-8 -*-
"""Celery App to regularly send data to New Relic Insights."""

from __future__ import absolute_import, division, print_function, unicode_literals

import logging
import logging.config

from celery import Celery
from celery.schedules import crontab
from celery.utils.log import get_task_logger

from glorified_cron import utils


_logger = get_task_logger(__name__)


app = Celery('glorified_cron.tasks')
app.config_from_object('celeryconfig')

# Set up crontab type periodic tasks
app.conf.beat_schedule = {
    scheduled_task['name']: {
        'task': scheduled_task['task'],
        'schedule': crontab(**scheduled_task['schedule']),  # Everyday at 11AM
        'args': scheduled_task['args'],
        'kwargs': scheduled_task['kwargs']
    }
    for scheduled_task in app.conf.SCHEDULED_TASKS
}

# set log config
logging.config.dictConfig(app.conf.LOGGER_CONFIG)

_logger.debug('initialized')


@app.task(bind=True)
def my_python_task(self):
    """Call python method."""
    try:
        return 'Hello from Python task.'
    except Exception as exc:
        _logger.exception('Epic Fail!.', extra={'request_id': self.request.id})
        raise exc



@app.task(bind=True)
def call_command(self, command):
    """Call cmdline command."""
    try:
        _logger.info('executing {}'.format(command), extra={'request_id': self.request.id})
        return utils.call_command(command, raise_exc=True)
    except Exception as exc:
        _logger.exception('Failure detected.', extra={'request_id': self.request.id})
        raise exc
