v = [int(input()) for i in range(4)]
print("    " + " ".join([str(n).ljust(3) for n in range(v[0], v[1] + 1)]), *[str(i).ljust(3) + " ".join([str(n * i).rjust(3) for n in range(v[0], v[1] + 1)]) for i in range(v[2], v[3] + 1)], sep = '\n')
