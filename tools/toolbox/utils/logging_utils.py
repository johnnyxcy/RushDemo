import logging
import sys
import typing
import colorama


def ascii_msg(log_level: int) -> typing.Callable[[str], str]:
    """Get message wrapper based on logging level

    Args:
        log_level (int): logging level

    Raises:
        NotImplementedError: Throw if invalid logging level

    Returns:
        typing.Callable[[str], str]: message wrapper
    """

    if log_level == logging.DEBUG:
        return lambda msg: f'{colorama.Fore.WHITE}{colorama.Style.DIM}{msg}{colorama.Fore.RESET}{colorama.Style.RESET_ALL}'
    elif log_level == logging.INFO:
        return lambda msg: f'{colorama.Fore.LIGHTGREEN_EX}{msg}{colorama.Fore.RESET}'
    elif log_level == logging.WARNING:
        return lambda msg: f'{colorama.Fore.LIGHTYELLOW_EX}{msg}{colorama.Fore.RESET}'
    elif log_level == logging.ERROR:
        return lambda msg: f'{colorama.Fore.LIGHTRED_EX}{msg}{colorama.Fore.RESET}'
    elif log_level == logging.CRITICAL:
        return lambda msg: f'{colorama.Fore.LIGHTWHITE_EX}{colorama.Back.RED}{msg}{colorama.Fore.RESET}{colorama.Back.RESET}'
    elif log_level == logging.NOTSET:
        return lambda msg: msg
    else:
        raise NotImplementedError('Not a log level')


# Since logging.Stream is only Generically typed in pyi,
# it is reasonable to ignore static typing check here
# pyright: reportMissingTypeArgument=warning
class AsciiStreamHandler(logging.StreamHandler):

    def emit(self, record: logging.LogRecord) -> None:
        msg = record.msg

        record.msg = f'[{record.levelname}] {msg}'
        return super().emit(record)


class _LoggerSingleton:
    _inst: typing.Optional[logging.Logger] = None

    def __new__(cls) -> logging.Logger:
        if cls._inst is None:
            cls._inst = logging.Logger(name='toolbox.utils.logger',
                                       level=logging.DEBUG)
            handler = AsciiStreamHandler(stream=sys.stdout)
            handler.setFormatter(logging.Formatter('%(message)s'))
            cls._inst.addHandler(handler)

        return cls._inst


logger = _LoggerSingleton()
