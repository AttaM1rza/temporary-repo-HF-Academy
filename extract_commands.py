""" """


def main():
    filepath = input(
        "Enter filepath, which contains terminal output (EXAMPLE: `/Users/atta/code/hf/scripts/session.txt`): "
    )
    terminal_command_line_starts = input(
        "Enter terminal command line starts (can be seperated by comma) (EXAMPLE:`(.venv) atta@ubuntuvm:~$,atta@ubuntuvm:~$)`: "
    )

    command_starts = terminal_command_line_starts.split(",")
    with open(filepath, "r") as file:
        terminal_output = file.read()

    extracted_commands_file = "commands.txt"
    with open(extracted_commands_file, "a") as file:
        for line in terminal_output.splitlines():
            for prefix in command_starts:
                prefix = prefix.strip()
                if line.startswith(prefix):
                    command = line[len(prefix) :].strip()
                    file.write(command + "\n")

    print(f"Commands extracted and saved to {extracted_commands_file}")
    return


if __name__ == "__main__":
    main()
