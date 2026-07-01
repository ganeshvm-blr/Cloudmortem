from cloudmortem.service import CloudMortemService
from cloudmortem.formatter import format_output


def run_command(args):
    service = CloudMortemService(should_fail=args.fail)

    result = service.run()

    output = format_output(result, json_mode=args.json)

    return result, output


def version_command(args):
    return "cloudmortem v0.1.0", 0
