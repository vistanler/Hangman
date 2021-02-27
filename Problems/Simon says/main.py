def what_to_do(instructions):
    if str(instructions).startswith("Simon says"):
        return "I " + str(instructions[11:])
    elif str(instructions).endswith("Simon says"):
        return "I " + str(instructions[: - 11])
    else:
        return "I won't do it!"
