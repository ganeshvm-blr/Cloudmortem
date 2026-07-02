from platformiq.model import DiffResult

from cloudmortem import ReportingService


class FakeReporter:
    def report(self, result):
        return "drift report"


def test_reporting_service_generates_report():
    service = ReportingService(FakeReporter())

    output = service.generate_report(DiffResult())

    assert output == "drift report"
