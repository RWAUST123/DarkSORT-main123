import matplotlib.pyplot as plt

# 文件路径
file_path = "merged_file.txt"

# 列索引，这里假设要读取第三列数据，索引从0开始
column_index = 0

# 存储读取的数据
training_losses = []

# 读取指定列数据
with open(file_path, "r") as file:
    for line in file:
        values = line.strip().split('\t')
        if len(values) > column_index:
            loss = float(values[column_index])
            training_losses.append(loss)

# x轴数据，可以根据需要自定义
epochs = range(1, len(training_losses) + 1)

# 绘制曲线图
plt.plot(epochs, training_losses, label="Training Loss", color="skyblue", linewidth=3)
plt.xticks(fontsize=14, fontname="Arial")
plt.yticks(fontsize=14, fontname="Arial")
plt.xlabel("Epochs",fontsize=14, fontname="Arial")
plt.ylabel("Loss",fontsize=14, fontname="Arial")
plt.title("Training Loss Curve",fontsize=14, fontname="Arial")
plt.legend()
plt.grid(True)

# 自定义保存图像格式和分辨率
plt.savefig("training_loss_curve0.png", dpi=1200, bbox_inches="tight")

# 显示图像
plt.show()
