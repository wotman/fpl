import lang

while True:
    text = input("> ")
    result, error = lang.run("<stdin>",text)

    if error: print(error.as_string())
    else: print(result)