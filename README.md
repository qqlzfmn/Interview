问题如下：  
二．Python 编程  
1.输入文件中包含1000万条记录，内容如下：  
2753：’Sunday’  
6732:27  
8730:’Chris’  
1293:Null  
请将数据按冒号后的数值类型分文件存放,并以冒号后的值排序  
如Num.txt包含6732:27；String.txt包含8730：’Chris’ 2753:’Sunday’。  
  
  
解答如下：  
  
DataCleaning.py 文件是数据处理文件，问题的解在这个文件里  
  
DataGenerator.py 文件是数据生成文件  
NameGenerator.py 文件是英文名生成文件  
NumGenerator.py 文件是数字生成文件  
  
Data.txt 文件是待处理的一万条数据（一千万条数据也测试过，能正确运行）  
Num.txt 文件是排序后的值为数字的数据  
String.txt 文件是排序后的值为字符串的数据  
Null.txt 文件是值为Null的数据  
