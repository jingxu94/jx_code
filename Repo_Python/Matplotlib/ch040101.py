#__author:  "Jing Xu"
#date:  2018/2/3

import numpy as np
import matplotlib.pyplot as plt
import io

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,4))

plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)
plt.plot(x, z, "b--", label="$cos(x^2)$")

plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-1.2, 1.2)
plt.legend()
buf = io.BytesIO()
plt.savefig(buf, fmt="png")
buf.getvalue()[:20]