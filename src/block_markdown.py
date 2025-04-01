def markdown_to_blocks(markdown):
    list_of_blocks = markdown.split("\n\n")
    list_of_blocks = [x.strip() for x in list_of_blocks]
    index = 0
    for block in list_of_blocks:
        if block == "":
            list_of_blocks.pop(index)
        index += 1

    return list_of_blocks

