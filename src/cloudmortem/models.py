from dataclasses import dataclass


@dataclass
class ServiceResult:
    message: str


class Success:
    def __init__(self, value: ServiceResult):
        self.value = value


class Failure:
    def __init__(self, error: str):
        self.error = error
