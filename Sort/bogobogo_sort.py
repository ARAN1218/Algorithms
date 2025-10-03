def bogobogo_sort(data):
  """
  ボゴボゴソート (O((n!)!) )
  リストを何度もシャッフルし、ソートされているかを確認する。
  ソートされていない場合は、再びシャッフルする。
  ソートが完了するまで宇宙の終わりまで続く可能性がある。

  Args:
    data (list): ソートする配列

  Returns:
    list: ソートされた配列
  """
  import random
  import itertools

  def is_sorted(data: list) -> bool:
      """リストがソート済みかを確認する関数"""
      return all(data[i] <= data[i+1] for i in range(len(data) - 1))

  n = len(data)
  
  # ベースケース: 要素が1つ以下なら、それはすでにソート済み
  if n <= 1:
      return data
  
  # ソート済みのコピーが完成するまで、永遠に試行するかもしれないループ
  sorted_data = list(data)
  print(f"現在のソート状況：{sorted_data}")
  while not is_sorted(sorted_data):
      
      # まず、リストの先頭からn-1個の要素を再帰的にソートする
      # この再帰呼び出しが終わる保証はどこにもない
      sub_list = sorted_data[:-1]
      sorted_sub_list = bogobogo_sort(sub_list)
      sorted_data[:-1] = sorted_sub_list
      
      # n-1個がソートされた結果、全体がソートされているかチェック
      # 最後の要素が最大値で、偶然正しい位置にあれば成功
      if not is_sorted(sorted_data):
          # ダメだった場合、すべてを無に帰してシャッフルし、再挑戦
          random.shuffle(sorted_data)

  return sorted_data


# テスト
import sys
# Pythonの再帰深度の上限を上げる（気休め）
sys.setrecursionlimit(2000)

data = [3, 2, 1, 4]
print("ボゴボゴソート開始...")
data_sorted = bogobogo_sort(data)
print("ソート結果:", data_sorted)
