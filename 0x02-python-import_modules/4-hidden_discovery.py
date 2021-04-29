#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = sorted(dir(hidden_4))
    for n in range(1, len(names)):
        if "__" in names[n]:
            continue
        print(names[n])
