import json

from cloudmortem.service import Success, Failure


def format_output(result, json_mode: bool = False):
    """
    Formats CLI output for both text and JSON modes.
    """

    # FAILURE
    if isinstance(result, Failure):
        if json_mode:
            return json.dumps(
                {
                    "status": "error",
                    "error": result.error,
                }
            )
        return result.error

    # SUCCESS
    if isinstance(result, Success):
        message = result.value.message

        if json_mode:
            return json.dumps(
                {
                    "status": "success",
                    "message": message,
                }
            )

        return message

    # SAFETY FALLBACK
    if json_mode:
        return json.dumps(
            {
                "status": "error",
                "error": "Unknown result type",
            }
        )

    return "Unknown result type"
