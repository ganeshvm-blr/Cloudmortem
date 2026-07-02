from cloudmortem.formatter import format_output
from cloudmortem.service import CloudMortemService, Success
from cloudmortem.models import ServiceResult
from cloudmortem.inventory.provider import InventoryProvider


def run_command(args):
    service = CloudMortemService(should_fail=args.fail)
    result = service.run()
    output = format_output(result, json_mode=args.json)
    return result, output


def version_command(args):
    from cloudmortem._version import __version__

    result = Success(value=ServiceResult(message=f"cloudmortem v{__version__}"))

    output = format_output(result, json_mode=args.json)
    return result, output


def inventory_command(args):
    provider = InventoryProvider()

    snapshot = provider.collect()

    result = Success(
        value=ServiceResult(
            message=f"Inventory collected: {len(snapshot.items)} resources"
        )
    )

    output = format_output(result, json_mode=args.json)

    return result, output
