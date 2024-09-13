import sys

from .logging_filters import (ErrorLogFilter, InfoLogFilter, WarningLogFilter,
                              CriticalLogFilter, DebugLogFilter)

logging_config = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': "{filename}:{funcName}:{lineno} #{levelname:8} [{asctime}] - {name} - {message}",
            'style': "{"
        },
        'main_formatter': {
            'format': "{filename}: {lineno} #{levelname:8} [{asctime}] - {name} - {message}",
            'style': "{"
        },
        'handler': {
            'format': "{filename}: {funcName}: {lineno} #{levelname:8} [{asctime}] - {name} - {message}",
            'style': "{"
        },
        'no_format': {
            'format': ""
        }
    },
    'filters': {
        'critical_filter': {
            '()': CriticalLogFilter,
        },
        'error_filter': {
            '()': ErrorLogFilter,
        },
        'debug_warning_filter': {
            '()': WarningLogFilter,
        },
        'info_filter': {
            '()': InfoLogFilter
        },
        'debug_filter': {
            '()': DebugLogFilter
        }
    },
    'handlers': {
        'root': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': 'DEBUG'
        },
        'default': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': 'DEBUG'
        },
        'stderr': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': 'DEBUG'
        },
        'stdout': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': sys.stdout,
            'level': 'DEBUG'
        },
        # 'error_file': {
        #     'class': 'logging.FileHandler',
        #     'filename': 'error.log',
        #     'mode': 'w',
        #     'level': 'DEBUG',
        #     'formatter': 'default',
        #     'filters': ['error_filter']
        # },
        # 'critical_file': {
        #     'class': 'logging.FileHandler',
        #     'filename': 'critical.log',
        #     'mode': 'w',
        #     'formatter': 'default',
        #     'filters': ['critical_filter']
        # },
        'no_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'no_format',
            'level': "DEBUG"
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['default']

        },
        '__main__': {
            'handlers': ['default'],
            'level': 'DEBUG'
        },
        'handlers': {
            'handlers': ['default'],
            'level': 'DEBUG'
        },
        'database': {
            'handlers': ['default'],
            'level': 'DEBUG'
        }
    },
    'root': {
        'formatter': 'default',
        'handlers': ['root'],
        'level': 'DEBUG'
    }
}
