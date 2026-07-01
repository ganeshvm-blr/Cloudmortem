import json


def format_output(result, json_mode: bool = False) -> str:
    if result.status == "success":
        message = result.value.message

        if json_mode:
            return json.dumps({"status": "success", "message": message})

        return message

    if result.status == "error":
        error = result.error

        if json_mode:
            return json.dumps({"status": "error", "error": error})

        return error

    if json_mode:
        return json.dumps({"status": "error", "error": "Unknown result"})

    return "Unknown result"
