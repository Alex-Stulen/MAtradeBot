import random
from dataclasses import dataclass, asdict

from ma_trade_bot.paper_trader import validations
from ma_trade_bot.paper_trader import exceptions


@dataclass
class PostData(object):
    pair: str
    timeframe: str
    candles: str = str(random.randint(1, 1000))
    ma: str = str(random.randint(1, 50))
    tp: str = str(random.randint(0, 100))  # 0% -100%
    sl: str = str(random.randint(0, 100))  # 0% - 100%


class PostDataHandle(object):
    """ Handler class for working with the PostData class. Available: validation, data transformation, etc. """
    def __init__(self, pair, timeframe, **kwargs):
        self.post_data = PostData(pair, timeframe, **kwargs)

        self._errors = []

    def as_dict(self):
        return asdict(self.post_data)

    def as_text(self, sep=', '):
        return f'{sep}'.join([f'{key}: {value}' for key, value in self.as_dict().items()])

    def is_valid(self):
        return not bool(len(self._errors))  # True if _errors is empty

    def _add_error(self, exception):
        self._errors.append(exception)

    @property
    def errors(self):
        """ Returns a errors list """
        return self._errors

    @property
    def errors_as_text_list(self):
        """ Returns a list where each element is an error text """
        return [error.text for error in self.errors]

    def errors_as_text(self, sep=', '):
        return f'{sep}'.join(self.errors_as_text_list)

    def validate(self):
        """ Validates dataclass fields and adds errors if needed """
        data: dict = self.as_dict()

        pair = data.get('pair')
        if not validations.is_valid_pair(pair):
            self._add_error(exceptions.ValidationError(f'pair `{pair}` is not valid'))

        timeframe = data.get('timeframe')
        if not validations.is_valid_timeframe(timeframe):
            self._add_error(exceptions.ValidationError(f'timeframe `{timeframe}` is not valid'))
