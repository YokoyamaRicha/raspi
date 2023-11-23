import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def epsilon_greedy_selection(epsilon, values, a, b, c):
    """
        epsilon-greedy 行動選択
    """
    nb_values = len(values)
    values[1]=values[1]+b
    values[2]=values[2]+c
    if np.random.uniform() < epsilon:   # 探索(epsilonの確率で)
        action = np.random.randint(0, nb_values)
    else:                               # 知識利用(1-epsilonの確率で)
        action = np.argmax(values)

    return action

nb_steps = 1000 
values = [1, 1, 1]
epsilon = 0.4        # 探索率(epsilon)

results = []
# 複数回行動選択
a=0
b=0
c=0
for _ in range(nb_steps):
    b+=1
    c+=3
    selected_action = epsilon_greedy_selection(epsilon, values, a, b, c)
    results.append(selected_action)

# ヒストグラムのプロット
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))   # x軸のメモリを整数に
ax.set_xticklabels(["", "A", "B", "C"])
ax.set_ylim(0, 1000)
ax.hist(results)
plt.savefig("result.jpg")
plt.show()