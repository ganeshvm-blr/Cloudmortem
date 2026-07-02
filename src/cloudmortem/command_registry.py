from cloudmortem.commands import run_command, version_command, inventory_command


def handle_run(args):
    return run_command(args)


def handle_version(args):
    return version_command(args)


def handle_inventory(args):
    return inventory_command(args)


COMMANDS = {
    "run": handle_run,
    "version": handle_version,
    "inventory": handle_inventory,
}
