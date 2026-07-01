from dataclasses import dataclass


@dataclass
class ServiceResult:
    message: str


@dataclass
class Success:
    value: ServiceResult
    status: str = "success"


@dataclass
class Failure:
    error: str
    status: str = "error"


class CloudMortemService:
    def __init__(self, should_fail: bool = False):
        self.should_fail = should_fail

    def run(self):
        if self.should_fail:
            return Failure(error="CloudMortem service failed intentionally")

        return Success(
            value=ServiceResult(message="CloudMortem service executed successfully")
        )
