#モジュールのインポート
import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix
import openpyxl


#Excelの読み込み
wb = openpyxl.load_workbook("隣接行列を作成したExcelファイルのパス")
ws = wb["シート名"]


#このリストに読み込んだデータをまとめる
row_list = []

#シートから1行ずつデータを読み込む
start_row = 1
for row in ws.iter_rows(min_row=start_row):
    if row[0].row > 3 and row[0].value is None:
        break
    value_list=[]
    for c in row:
        value_list.append(c.value)
    row_list.append(value_list)


#隣接行列の入力
l = row_list
print(l)

#csr_matrix形式で疎行列を生成・変換
csr = csr_matrix(l)
print(csr)

#形式の確認
print(type(csr))
print("ーーーーーーーーーーーーーーーーーーーー")

#ワーシャルフロイド法（有向グラフ,重み付き,経路復元）で解く
d, p = floyd_warshall(csr, directed=True, return_predecessors=True)
print(d)
print(p)
print("ーーーーーーーーーーーーーーーーーーーー")

#NumPyをCSV形式で出力
np.savetxt("C:/Users/skewe/Desktop/np_savetxt_最短距離.csv", d, delimiter=",")
np.savetxt("C:/Users/skewe/Desktop/np_savetxt_経路復元.csv", p, delimiter=",")
print("ーーーーーーーーーーーーーーーーーーーー")
