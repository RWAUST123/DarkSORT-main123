import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
file_path = "data.xlsx"
data = pd.read_excel(file_path)

# 提取数据
epochs = data.iloc[:, 0]
y1 = data.iloc[:, 1]
y2 = data.iloc[:, 2]
y3 = data.iloc[:, 3]

# 绘制曲线图
plt.figure(figsize=(10, 6))
plt.plot(epochs, y1, label="Y1")
plt.plot(epochs, y2, label="Y2")
plt.plot(epochs, y3, label="Y3")
plt.xlabel("Epoch")
plt.ylabel("Values")
plt.title("Curves")
plt.grid(True)
plt.legend()

# 显示曲线图
plt.show()


# 显示曲线图
plt.show()
