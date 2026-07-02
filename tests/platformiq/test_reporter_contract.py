from platformiq.contracts import Reporter
from platformiq.model import DiffResult


class FakeReporter(Reporter):
    def report(self, result: DiffResult) -> str:
        return "reported"


def test_reporter_returns_output():
    reporter = FakeReporter()

    result = reporter.report(DiffResult())

    assert result == "reported"
