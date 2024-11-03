import warnings
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')
# %matplotlib inline

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
df = pd.read_csv(r'C:\Users\Admin\OneDrive\Tài liệu\python\Bai_Tap_Lon\data\result.csv')


df.head(10)
df.shape
pd.set_option('display.max_columns', None)
df.info()
pd.set_option('display.max_rows',None)
df.isna().sum()
df['team'].value_counts()
df.describe().T


sse = []
silhouette_scores = []
X = df.select_dtypes(include=[float, int])
for k in range(2, 10):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    sse.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X, kmeans.labels_))
    plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(range(2, 10), sse, marker='o')
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.title("Elbow Method")

plt.subplot(1, 2, 2)
plt.plot(range(2, 10), silhouette_scores, marker='o')
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Score")
plt.show()
# nhìn đồ thị chọn số cluster=4


from sklearn.decomposition import PCA
import seaborn as sns

# Giảm số chiều với PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
kmeans = KMeans(n_clusters=4, random_state=42)
clusters = kmeans.fit_predict(X_pca)

# Vẽ biểu đồ
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=clusters, palette="viridis", legend='full')
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.title("K-means Clustering with PCA")
plt.show()


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv(r'C:\Users\Admin\OneDrive\Tài liệu\python\Bai_Tap_Lon\data\result.csv')

p1 = "Max Aarons"  # Thay tên cầu thủ 
p2 = "Tyler Adams"  # Thay tên cầu thủ 
attributes = ["npxG", "Long_Cmp", "Pass_Cmp_outcome"]  # Thay đổi danh sách các chỉ số muốn so sánh

# Trích xuất dữ liệu
data1 = df[df['name'] == p1][attributes].values.flatten()
data2 = df[df['name'] == p2][attributes].values.flatten()

# Thiết lập biểu đồ radar
labels = np.array(attributes)
num_vars = len(attributes)

# Tạo các góc cho biểu đồ radar
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
data1 = np.concatenate((data1, [data1[0]]))  # Vòng lại điểm đầu
data2 = np.concatenate((data2, [data2[0]]))  # Vòng lại điểm đầu
angles += angles[:1]

# Vẽ biểu đồ radar
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, data1, color='blue', alpha=0.25, label=p1)
ax.fill(angles, data2, color='red', alpha=0.25, label=p2)
ax.plot(angles, data1, color='blue', linewidth=2)
ax.plot(angles, data2, color='red', linewidth=2)

# Thiết lập các nhãn
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

# Thêm tiêu đề và chú thích
plt.title(f"So sánh cầu thủ {p1} và {p2}")
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.show()
