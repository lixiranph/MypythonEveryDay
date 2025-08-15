'''
try:

except 异常 as 变量:
else:
    没有异常，执行的代码
finally:
    最终一定要执行的代码
'''
# try:
#     file=open('123.txt','w',encoding='utf-8')
#     file.write('<UNK>1')
#     file.write('<UNK>2')
#     file.write('写入完毕')
#     # #write只可以写入字符串
#     # file.write([1,2,3])
#     print('写入完毕')
# except Exception as e:
#     print(f'写入失败报错为{e.args}')
# else:
#     print('没有异常，操作成功')
# finally:
#     file.close()
#     print('关闭文件，谢谢使用')

# try:
#     with open('123.txt', 'w', encoding='utf-8') as file:
#         file.write('<UNK>1\n')
#         file.write('<UNK>2\n')
#         file.write('写入完毕\n')
#         # #write只可以写入字符串
#         # file.write([1,2,3])
#         print('写入完毕')
# except Exception as e:
#     print(f'写入失败，报错为: {e}')
# else:
#     print('没有异常，操作成功')
# finally:
#     print('文件操作结束，谢谢使用')

try:
    with open('123.txt', 'w', encoding='utf-8') as file:
        lines = ['<UNK>1\n', '<UNK>2\n', '写入完毕\n']
        file.writelines(lines)#writelines可以写入字符串
        print('写入完毕')
except Exception as e:
    print(f'写入失败，报错为: {e}')
else:
    print('没有异常，操作成功')
finally:
    print('文件操作结束，谢谢使用')