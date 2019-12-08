with open('day8.txt') as f:
    data = [int(c) for c in f.read().strip()]
w, h = 25, 6
no_layers = len(data) // (w * h)

#data = [int(c) for c in "123456789012"]
#w, h = 3, 2

layers = []

#while layer in range(no_layers):
#    new = []
#    for i, layer in enumerate(layers):
#        for row in range(h):
#            layer.append(data[(i * w * h) + row * w: (i * w * h) + (row + 1) * w])
#    layers.append(new)

layers = [data[(w * h) * i:(w * h) * (i + 1)] for i in range(no_layers)]
min_zeros_layer = layers[0]
for layer in layers:
    if layer.count(0) < min_zeros_layer.count(0):
        min_zeros_layer = layer
print(min_zeros_layer.count(1) * min_zeros_layer.count(2))
