from __future__ import annotations

from platformiq.contracts import Reporter
from platformiq.model import DiffResult


class ReportingService:
    """
    Application service responsible for producing reports.
    """

    def __init__(self, reporter: Reporter):
        self.reporter = reporter

    def generate_report(
        self,
        result: DiffResult,
    ) -> str:
        """
        Generate a report from analysis results.
        """

        return self.reporter.report(result)
