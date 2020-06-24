my_text="[aaaaa text='kokodayo']"

my_fu_za_text="[abc='ssdsd' text='ののののの' character='时雨']"

my_test_3="[mianText='aasdas' text='のhello world' char='斯帝罗兰绿绿绿绿']"
#第二种处理方法 先切割text= ,分成两个字符串  先一刀两段 ,再取其后面的str
#input_var是要处理的字符串
def split_Text_methond(input_var):
#预处理
    pre_chu_li=input_var.split("text=")
    print("预处理>="+str(pre_chu_li))
    print("预处理后的索引1的值>="+pre_chu_li[1])
    print("预处理后索引1分割掉''的值>="+str(pre_chu_li[1].split("'")))
    
#预处理第二步
#再取text=后面的值 去掉 ] 符号
    pre_chu_2=pre_chu_li[1].split("'")
    print("细节处理>="+str(pre_chu_2))
#最后的text的值为索引1的值
    result=pre_chu_2[1]
    print("最终结果>="+result)
    #返回结果
    return result
    pass
    
    
#总结 首先找到要提取的字符串 使用split()方法分割字符串
#然后取索引为1的值 (text=) 后面的值
#然后再进行细节处理 去除多余的符号 得到纯净的字符串 
#得到的纯净字符串索引就变成了0 取索引为0的值就行

#简单测试
#split_Text_methond(my_text)

#测试复杂字符串是否能够提取出text=后面的消息
split_Text_methond(my_test_3)
"""
print("原始数据  >="+my_text)
my_out=my_text.split("[")
print("去掉'['符号结果  >="+str(my_out))
print("去掉[后的长度   >="+str(len(my_out)))
myout_2=my_out[1].split("]")
print("去掉右 ]符号结果"+str(myout_2))
print("最终结果  >="+str(myout_2[0]))
print(type(my_out))
myout_3=myout_2[0].split("text=")
print("去掉text=结果  >+"+str(myout_3))

print("选择text=后面的文字  >="+str(myout_3[1]))
"""
