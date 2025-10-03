def quantum_bogosort(data):
  """
  量子ボゴソート (O(n))
  ボゴソートを一度実行し、揃ってなかった場合は宇宙を破壊する。
  揃っていた場合、その宇宙は生き残るため確実に一度で揃う。

  Args:
    data (list): ソートする配列

  Returns:
    data_sorted (list): ソートされた配列 (仮に元の配列を返す)
  """
  import random

  def BIGBANG():
    """
    宇宙を破壊する (Big Bang)

    Args:
      nothing

    Returns:
      nothing
    """
    print("THE END")
    while True:
      pass

  # 通常のボゴソートを実行する
  random.shuffle(data)
  data_sorted = data

  # データがソートされているか確認する
  def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

  if not is_sorted(data_sorted):
    BIGBANG()
    
  return data_sorted


# テスト
data = [5, 2, 4, 6, 1, 3]
data_sorted = quantum_bogosort(data)
print(data_sorted)
