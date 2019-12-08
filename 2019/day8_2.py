with open('day8.txt') as f:
    data = [int(c) for c in f.read().strip()]
w, h = 25, 6

#data = [int(c) for c in "0222112222120000"]
#w, h = 2, 2

layers = []
no_layers = len(data) // (w * h)

#while layer in range(no_layers):
#    new = []
#    for i, layer in enumerate(layers):
#        for row in range(h):
#            layer.append(data[(i * w * h) + row * w: (i * w * h) + (row + 1) * w])
#    layers.append(new)

layers = [data[(w * h) * i:(w * h) * (i + 1)] for i in range(no_layers)]
out = []
for i in range(w * h):
    for layer in layers:
        if layer[i] == 0 or layer[i] == 1:
            out.append(layer[i])
            break
print(out)
s = ""
for i, n in enumerate(out):
    if i % w == 0:
        s+='\n'
    s += u'\u2588' if n == 1 else " "
    s += " "
print(s)
