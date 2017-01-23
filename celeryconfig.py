# Celery configs
BROKER_URL = "redis://localhost:6379/0"
RESULT_BACKEND = "redis://localhost:6379/1"
TASK_SERIALIZER = "json"
RESULT_SERIALIZER = "json"
ACCEPT_CONTENT = ["json"]
CELERYBEAT_SCHEDULE = {
    "my-python-task": {
        "task": "glorified_cron.tasks.my_python_task",
        "schedule": 60.0, "args": []
    }
}
ENABLE_UTC = True

# Custom configs
# Because some periodic tasks needs to be scheduled using crontabs method.
# For help, see this http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#crontab-schedules
SCHEDULED_TASKS = [
    {
        'name': 'call-bash-command',
        'task': 'glorified_cron.tasks.call_command',
        'schedule': {'minute': '*'},
        'args': [],
        'kwargs': {'command': 'echo "hello world"'}
    }
]


LOGGER_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": 10
        },
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": "glorified_cron.log",
            "formatter": "standard",
            "backupCount": 10,
            "interval": 1,
            "when": "d",
            "level": 30
        }
    },
    "loggers": {
        "": {
            "handlers": ["console", "file"],
            "level": 30,
            "propagate": True
        },
        "glorified_cron": {
            "handlers": ["console", "file"],
            "level": 10,
            "propagate": False
        }
    }
}
