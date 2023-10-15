weather1 = [43, 54, 56]
weather2 = [49, 24, 56]
weather3 = [41, 54, 36]
w1 = 0.1
w2 = 0.3
w3 = 0.2
weight = [w1, w2, w3]


def crop_hearwest(region, weight):
    result = 0
    for x, v in zip(region, weight):
        result += x * v
    return result


print(crop_hearwest(weather1, weight))
