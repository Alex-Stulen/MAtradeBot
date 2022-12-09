from aiogram.dispatcher.filters.state import State, StatesGroup


class PairState(StatesGroup):
    """ Step-by-step form (state) for getting data about the pair and timeframe from the user """
    pair = State()
    timeframe = State()
