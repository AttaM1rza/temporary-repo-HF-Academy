""" """


def main():
    filepath = input(
        "Enter filepath, which contains terminal output (EXAMPLE: `/Users/atta/code/hf/scripts/session.txt`): "
    )
    terminal_command_line_start = input(
        "Enter terminal command line start (can be seperated by comma) (EXAMPLE:`(.venv) atta@ubuntuvm:~$,atta@ubuntuvm:~$)`: "
    )

    command_starts = terminal_command_line_start.split(",")
    with open(filepath, "r") as file:
        terminal_output = file.read()

    executed_commands = []
    for line in terminal_output.splitlines():
        for prefix in command_starts:
            prefix = prefix.strip()
            if line.startswith(prefix):
                command = line[len(prefix) :].strip()
                executed_commands.append(command)
                break

    with open("commands.txt", "w") as file:
        for command in executed_commands:
            file.write(command + "\n")
    print("Commands extracted and saved to commands.txt")
    return


if __name__ == "__main__":
    main()
