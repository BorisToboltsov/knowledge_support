class StateUser:
    def __init__(self):
        self._state_user = (
            {}
        )  # {telegram_id: {'answer_const': False, 'times_up': True}}

    async def create_user_from_state(self, telegram_id: int):
        if telegram_id not in self._state_user:
            self._state_user[telegram_id] = {"answer_const": False, "times_up": False}

    async def set_state_times_up(self, telegram_id: int, times_up: bool):
        if telegram_id in self._state_user:
            self._state_user[telegram_id]["times_up"] = times_up

    async def get_state_times_up(self, telegram_id: int) -> bool:
        if telegram_id in self._state_user:
            return self._state_user[telegram_id]["times_up"]

    async def set_state_answer_const(self, telegram_id: int, answer_const: bool):
        if telegram_id in self._state_user:
            self._state_user[telegram_id]["answer_const"] = answer_const
