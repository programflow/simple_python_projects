import colorgram


def generate_colors():
    colors = colorgram.extract('image.jpg', 30)

    # create a list of colors represented as rgb tuples
    rgb_colors = []
    for color in colors:
        rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

    rgb_colors = rgb_colors[3:]
    return rgb_colors
