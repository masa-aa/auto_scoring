from auto_scoring import all_execution, equal

# 実行まで
outputs = all_execution(folder="sample_c", arg="2 2", save="sample.txt")
# 比較
equal(folder="sample_txt", outputs=outputs, save="sample_equal.txt")
