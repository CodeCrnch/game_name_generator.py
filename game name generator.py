import random

for i in range(20):
    prefixes = ["arc", "bran", "cy", "dru", "el", "fay", "gor", "hel", "il",
                      "jor", "kai", "lum", "myth", "nyx", "or", "pry", "qua", "ry",
                      "sil", "tyr", "ul", "vyr", "wyn", "xan", "ygg", "zor"]
    suffixes = ["agon", "bane", "core", "dor", "eth", "fire", "gorn",
                     "heart", "ian", "jade", "kith", "lance", "mor", "nir", "on",
                     "pax", "quill", "rune", "soul", "thorn", "ulon", "vex", "ward",
                     "xen", "yss", "zane"]

    def generate_name():
        prefix = random.choice(prefixes)
        suffix = random.choice(suffixes)
        return prefix + suffix

    name = generate_name()
    print(name)
