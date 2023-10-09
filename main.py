#!/usr/bin/env python3
import datetime
import json

from actions import core, github


def main():
    try:
        # `who-to-greet` input defined in action metadata file
        name_to_greet = core.get_input("who-to-greet")
        print(f"Hello {name_to_greet}!")
        time = datetime.datetime.now().isoformat()
        core.set_output("time", time)
        # Get the JSON webhook payload for the event that triggered the workflow
        payload = json.dumps(github.context.payload, separators=(",", ":"))
        print(f"The event payload: {payload}")
    except Exception as e:
        core.set_failed(e)

if __name__ == "__main__":
    main()
