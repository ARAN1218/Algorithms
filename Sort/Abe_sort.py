def abe_sort(data):
  """
  Abeソート (O(n))
  現在見つかっている最大値に都度改ざんしていく。

  Args:
    data (list): ソートする配列

  Returns:
    data_sorted (list): ソートされた配列 (仮に元の配列を返す)
  """

  if not data:
    return []

  data_sorted = [data[0]]
  for item in data[1:]:
    if item >= data_sorted[-1]:
      data_sorted.append(item)
    else:
      data_sorted.append(data_sorted[-1])
  return data_sorted


# テスト
data = [5, 2, 4, 6, 1, 3]
data_sorted = abe_sort(data)
print(data_sorted)

data = [1, 2, 3, 4, 5, 6]
data_sorted = abe_sort(data)
print(data_sorted)

data = [6, 5, 4, 3, 2, 1]
data_sorted = abe_sort(data)
print(data_sorted)
