def list_dot(x1, x2):
  """
  2つのリストを受け取り、その内積を計算する関数。
  """
  dot = 0.0
  for i in range(len(x1)):
      dot += x1[i]*x2[i] # x += y は、x に x+y を代入することを表す。
  return dot # return 文で計算した値を返す。
