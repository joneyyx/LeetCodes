# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))
#
# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         for v in values:
#             ans += v
#     print(ans)


# import  sys
# while True:
#     try:
#         line = sys.stdin.readline()
#         vals = list(map(int, line.replace("[", "").replace("]", "").strip().split(",")))
#         # find biggest
#
#         biggest = vals[0]
#         for i in range(1, len(vals)):
#             if vals[i] > biggest:
#                 biggest = vals[i]
#
#         full_list = [i for i in range(biggest+1)]
#
#         result_lst = set(full_list) - set(vals)
#
#         if len(result_lst) ==0:
#             print(biggest+1)
#         else:
#             print(result_lst.pop())
#
#     except:
#         break


# mxt=[[]]
# import sys
#
# while True:
#     try:
#         n, m = map(int, input().strip().split())
#         print(n, m)
#         mtx = [[]]
#         for i in range(n):
#             tmp = list(map(int, input().strip().split()))
#             print(type(tmp))
#             for j in range(m):
#                 mtx[i][j].append(tmp[j])
#                 print(mtx[i][j])
#
#
#     except:
#         break
# mxt[0][0]=1
# mxt