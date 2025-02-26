import sys
import shutil
import os

builtins = ["exit", "echo", "type"]

def shell_type(args):
    if args[0] in builtins:
        sys.stdout.write(f"{args[0]} is a shell builtin\n")

    elif path := shutil.which(args[0]):
        sys.stdout.write(f"{args[0]} is {path}\n")

    else:
        sys.stdout.write(f"{args[0]}: not found\n")


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")

    # Wait for user input

    command = input()

    if command == "exit 0":
        command_parts = command.split()
        exit(int(command_parts[1]))

    elif "type" in command:
        command_parts = command.split()
        shell_type(command_parts[1:])

    elif "echo" in command:
        command_parts = command.split()
        sys.stdout.write(f"{' '.join(command_parts[1:])}\n")

    else:
        if shutil.which(command.split(" ")[0]):
            os.system(command)
        else:
            sys.stdout.write(f"{command}: not found\n")

    main()


if __name__ == "__main__":
    main()
