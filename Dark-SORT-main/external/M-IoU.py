import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

mean = [0, 0]
cov = [[1, 0.7], [0.7, 1]]
# 生成2D高斯分布样本
x, y = np.random.multivariate_normal(mean, cov, 500).T
# 计算Mahalanobis距离
inverse_cov = np.linalg.inv(cov)
mahalanobis_distance = []
for point in zip(x, y):
    mahalanobis_distance.append(np.sqrt(np.dot(np.dot(point - mean, inverse_cov), point - mean)))
# 绘制散点图
plt.scatter(x, y, c=mahalanobis_distance, cmap='viridis', label='')
# 绘制Mahalanobis距离等高线
confidence_interval = chi2.ppf(0.95, df=2)  # 95%置信区间
mahalanobis_contours = plt.contour(x, y, mahalanobis_distance, levels=[confidence_interval], colors='r', linestyles='dashed', label='Mahalanobis距离')
plt.legend()
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Mahalanobis')
plt.show()
