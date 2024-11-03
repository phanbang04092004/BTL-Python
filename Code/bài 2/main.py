#Tìm top 3 cầu thủ có chỉ số cao nhất và thấp nhất
import pandas as pd

# Đọc file CSV, bỏ qua 2 hàng đầu và giữ hàng thứ 3 làm tiêu đề
input_file = r'C:\Users\Admin\OneDrive\Tài liệu\python\Bai_Tap_Lon\data\result.csv'
output_file = r'C:\Users\Admin\OneDrive\Tài liệu\python\Bai_Tap_Lon\data\top_bottom_results.csv'

df = pd.read_csv(input_file)
# Loại bỏ khoảng trắng trong tên cột
df.rename(columns=lambda x: x.strip(), inplace=True)

# Kiểm tra nếu cột 'Name' tồn tại
if 'name' not in df.columns:
    print("Cột 'name' không tồn tại! Danh sách cột hiện tại:", df.columns.tolist())
    exit()

print("Tên các cột:", df.columns.tolist())

# Danh sách để lưu kết quả
results = []

def collect_top_bottom(df, column, n=3):
    valid_data = df[['name', column]].dropna()

    if len(valid_data) < n:
        print(f"Lỗi: Không đủ dữ liệu trong cột '{column}' để lấy top/bottom {n}.")
        return

    top = valid_data.nlargest(n, column)
    bottom = valid_data.nsmallest(n, column)

    results.append({'Type': 'Top', 'name': '', 'Score': '', 'Metric': column})
    for _, row in top.iterrows():
        results.append({'Type': 'Top', 'name': row['name'], 'Score': row[column], 'Metric': column})

    results.append({'Type': '', 'name': '', 'Score': '', 'Metric': ''})  # Dòng trống
    results.append({'Type': 'Bottom', 'name': '', 'Score': '', 'Metric': column})
    for _, row in bottom.iterrows():
        results.append({'Type': 'Bottom', 'name': row['name'], 'Score': row[column], 'Metric': column})

    results.append({'Type': '', 'name': '', 'Score': '', 'Metric': ''})  # Dòng trống

# Duyệt qua các cột dạng số từ cột thứ 5 trở đi
for col in df.columns[4:]:
    if pd.api.types.is_numeric_dtype(df[col]):
        collect_top_bottom(df, col)

if results:
    results_df = pd.DataFrame(results)
    results_df.to_csv(output_file, index=False)
    print(f"Kết quả đã được lưu vào {output_file}")
else:
    print("Không có dữ liệu để lưu.")







# Tìm trung vị của mỗi chỉ số. 
import pandas as pd

# Đọc tệp CSV với một hàng tiêu đề
df = pd.read_csv(r'C:\Users\Admin\OneDrive\Tài liệu\python\Bai_Tap_Lon\data\result.csv')

# Tạo một DataFrame để lưu kết quả cuối cùng
final_results = []

# Duyệt qua các attribute (bắt đầu từ cột thứ 4 trong bảng)
for col_index in range(4, df.shape[1]):
    column = df.iloc[:, col_index]
    column_numeric = pd.to_numeric(column, errors='coerce')  # Chuyển cột về dạng số

    # Tính toán median, mean, và std cho toàn giải
    median_value_all = round(column_numeric.median(), 2)
    mean_value_all = round(column_numeric.mean(), 2)
    std_value_all = round(column_numeric.std(), 2)

    # Thêm kết quả cho toàn giải
    if col_index == 4:  # Nếu là attribute đầu tiên
        final_results.append(['All', median_value_all, mean_value_all, std_value_all])
    else:  # Các attribute khác
        final_results[0].extend([median_value_all, mean_value_all, std_value_all])

    # Tính toán cho từng đội
    for team_name, team_data in df.groupby('team'):
        team_column = pd.to_numeric(team_data.iloc[:, col_index], errors='coerce')  # Cột của từng đội
        team_median = round(team_column.median(), 2)
        team_mean = round(team_column.mean(), 2)
        team_std = round(team_column.std(), 2)

        # Kiểm tra nếu đội đã có trong final_results
        found = False
        for row in final_results:
            if row[0] == team_name:
                # Cập nhật hàng của đội với các chỉ số mới
                row.extend([team_median, team_mean, team_std])
                found = True
                break

        if not found:
            # Nếu đội chưa có trong final_results, thêm mới
            final_results.append([team_name, team_median, team_mean, team_std])

# Chuyển đổi danh sách kết quả cuối cùng thành DataFrame
final_df = pd.DataFrame(final_results)

# Cập nhật tiêu đề cột để bao gồm tên chỉ số cho mỗi attribute
column_titles = ['team']
for col_index in range(4, df.shape[1]):
    column_titles.extend([f'Median of {df.columns[col_index]}',
                          f'Mean of {df.columns[col_index]}',
                          f'Std of {df.columns[col_index]}'])

final_df.columns = column_titles

# Ghi kết quả ra file results3.csv
print(final_df)
final_df.to_csv(r'C:\Users\Admin\OneDrive\Tài liệu\python\Bai_Tap_Lon\data\results2.csv', index=False)







# Vẽ historgram phân bố của mỗi chỉ số của các cầu thủ trong toàn giải và mỗi đội.
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Đọc dữ liệu
df = pd.read_csv(r'C:\Users\Admin\OneDrive\Tài liệu\python\Bai_Tap_Lon\data\result.csv')

# Làm sạch tên cột
df.columns = [col.replace("Unnamed:", "").strip() for col in df.columns]

# Kiểm tra tên cột
print(df.columns)

# Lọc các cột số (float và int)
numeric_cols = df.select_dtypes(include=['float', 'int']).columns

# Đếm số biểu đồ đã vẽ
cnt = 0

# Vẽ histogram theo thuộc tính của toàn giải
for att in numeric_cols:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x=att, kde=True, bins=20)
    title = f"Histogram of {att} for All Players in the League"
    plt.title(title)
    plt.xlabel(att)
    plt.ylabel("Frequency")
    plt.show()

# Vẽ biểu đồ cho các thuộc tính số theo từng đội
for att in numeric_cols:
    cnt += 1
    print("Histogram:", cnt)

    # Tạo biểu đồ FacetGrid theo từng đội
    g = sns.FacetGrid(df, col='team', col_wrap=4, height=3, sharex=True, sharey=True)
    g.map_dataframe(sns.histplot, x=att, bins=20, kde=True)
    
    # Đặt nhãn và tiêu đề cho biểu đồ với tên đội
    g.set_axis_labels(att, "Frequency")  # Đặt tên cột `att` làm nhãn x
    g.set_titles("{col_name}")  # Tiêu đề cho mỗi biểu đồ nhỏ theo tên đội
    
    # Căn chỉnh và hiển thị biểu đồ
    plt.tight_layout()
    plt.show()


# Tìm đội bóng có chỉ số điểm cao nhất ở mỗi chỉ số
import pandas as pd

# Đọc file CSV vào DataFrame
file_path = r'C:\Users\Admin\OneDrive\Tài liệu\python\Bai_Tap_Lon\data\results2.csv'
df = pd.read_csv(file_path)

# Lọc bỏ hàng 'All' nếu có
df = df[df['team'] != 'All']

# Tạo dictionary để lưu kết quả
max_scores = {}

# Duyệt qua từng cột chỉ số (bỏ qua cột 'team')
for col in df.columns[1:]:
    max_team = df.loc[df[col].idxmax()]['team']
    max_value = df[col].max()
    max_scores[col] = (max_team, max_value)

# In ra kết quả
for metric, (team, value) in max_scores.items():
    print(f"Đội có {metric} cao nhất là: {team} với giá trị {value}")