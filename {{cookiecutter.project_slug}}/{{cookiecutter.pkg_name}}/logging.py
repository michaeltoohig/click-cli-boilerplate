import logging
import sys

import structlog


def configure_logger(strict, level=logging.INFO) -> None:
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=level,
    )

    processors = [
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.filter_by_level,  # First step, filter by level to
        structlog.stdlib.add_logger_name,  # module name
        structlog.stdlib.add_log_level,  # log level
        structlog.processors.TimeStamper(fmt="iso"),  # ISO timestamp UTC by default
        structlog.processors.UnicodeDecoder(),  # Decodes all bytes to unicode
        structlog.processors.StackInfoRenderer(),
    ]
    if strict:
        processors += [
            structlog.processors.dict_tracebacks,
            structlog.processors.JSONRenderer(),
        ]
    else:
        processors += [
            structlog.dev.ConsoleRenderer(
                exception_formatter=structlog.dev.rich_traceback,
            ),
        ]

    structlog.configure(
        processors=processors,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
