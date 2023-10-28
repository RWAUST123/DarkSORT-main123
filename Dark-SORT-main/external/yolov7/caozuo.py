# 读取原始的txt文件
original_file_path = "merged_file.txt"

# 读取包含新列数据的txt文件
new_column_file_path = "data1.txt"

# 打开原始文件和新列数据文件
with open(original_file_path, "r") as original_file, open(new_column_file_path, "r") as new_column_file:
    original_lines = original_file.readlines()
    new_column_lines = new_column_file.readlines()

# 获取新数据的行数
new_data_rows = len(new_column_lines)

# 合并原始文件和新列数据，然后保存到一个新文件
merged_file_path = "merged_file.txt"
with open(merged_file_path, "w") as merged_file:
    for i in range(new_data_rows):
        original_line = original_lines[i].strip()
        new_column_data = new_column_lines[i].strip()
        merged_line = f"{original_line}\t{new_column_data}\n"
        merged_file.write(merged_line)

print(f"New column data added to the original file for {new_data_rows} rows and saved as 'merged_file.txt'.")
