""" """

import datetime


def main():
    while True:
        print("\n--- Extract commands from terminal session window ---")
        print(
            "Paste the complete content of a terminal window [Command+V and Command+C] into a new text file"
        )
        try:
            terminal_content = input("Refernce the path of that file here: ")
            terminal_command_line_starts = input(
                "Enter terminal command line starts [comma separated, for example: `(.venv) atta@ubuntuvm:~$,atta@ubuntuvm:~$`]: "
            )
            command_starts = [prefix.strip() for prefix in terminal_command_line_starts.split(",")]

            if not terminal_content:
                raise ValueError("No terminal content was provided.")
            if not command_starts:
                raise ValueError(
                    "To identify all commands entered by the user, the start of each command in the terminal is required. Please provide this information."
                )

            with open(terminal_content, "r") as file:
                terminal_output = file.read()
            extracted_commands_file = f"commands-{datetime.datetime.now()}.txt"
            with open(extracted_commands_file, "w") as file:
                for line in terminal_output.splitlines():
                    for prefix in command_starts:
                        if line.startswith(prefix):
                            command = line[len(prefix) :].strip()
                            file.write(command + "\n")

            print(f"Commands extracted and saved to {extracted_commands_file}")
        except FileNotFoundError:
            print("Error: The session file was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
