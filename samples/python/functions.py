#功能页面
import random

# 90 * rp = p2
# 90 * (1-rp) = p3
def randomExm(list, weight):
    new_list = []
    for i, val in enumerate(list):
        new_list.extend(val * weight[i])
    return random.choice(new_list)
