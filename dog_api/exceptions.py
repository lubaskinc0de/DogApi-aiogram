class ApiError(Exception):

    def __init__(self, message='Ошибка при обращении к API') -> None:
        self.message = message
        super().__init__(self.message)