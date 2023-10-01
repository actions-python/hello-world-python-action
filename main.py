#!/usr/bin/env python3
import datetime

from actions import core, github


def main():
    try:
        # `who-to-greet` input defined in action metadata file
        name_to_greet = core.get_input("who-to-greet")
        print(f"Hello {name_to_greet}!")
        time = datetime.datetime.now().isoformat()
        core.set_output("time", time)
        # Get the JSON webhook payload for the event that triggered the workflow
        payload = github.context.payload.model_dump_json(indent=2)
        print(f"The event payload: {payload}")
    except Exception as e:
        core.set_failed(e)

if __name__ == "__main__":
    main()
