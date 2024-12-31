# Another play around input practice - make a layered cake! Print this and see what you get!

i = int(input("Enter the number of layers for the cake: "))
m = []

# Top layer
m.append("+" + "-" * (i * 4 + 1) + "+")
m.append("|" + " " * (i * 4 + 1) + "|")

# Middle layers
for v in range(i, 1, -1):
    m.append(" " * (i - v) * 2 + "+" + "-" * (v * 4 + 1) + "+")
    m.append(" " * (i - v + 1) * 2 + "|" + " " * ((v - 1) * 4 + 1) + "|")

# Base of the cake
m.append(" " * (i - 1) * 2 + "|" + " " * 5 + "|")
m.append(" " * (i - 1) * 2 + " _|_|_")

# Print the cake
print("\n".join(m[::-1]))
