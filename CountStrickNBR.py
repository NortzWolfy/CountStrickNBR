#定义每个数字所需的灯管数目 0要6个，1要2个，2要5个...
StrickPreNumber=[6,2,5,5,4,5,6,3,7,6]
TargetTimeNumber=2
MaxNumber=0
AllTimes=0

#开始获得用户数据所需要的灯管(火柴)数目
def GetTargetNumber():
    global TargetTimeNumber
    try:
        TargetTimeNumber=int(input("键入火柴总数 (≥2)："))
    except:
        print("参数非法")
        GetTargetNumber()
    if TargetTimeNumber<2:
        print("参数非法")
        GetTargetNumber()

#开始获得用户数据数据区间
def GetMaxNumber():
    global MaxNumber
    try:
        MaxNumber=int(input("键入取舍范围：0~"))
    except:
        print("参数非法")
        GetMaxNumber()
    if MaxNumber<=0:
        print("参数非法")
        GetMaxNumber()
        
#进去一个数字，返回这个数字所需的灯管数目 如进去的数据为111则返回6
def JugeThisStrick(Number):
    if Number==0:
        return 6
    global StrickPreNumber
    list1=GetPreNBr(Number)
    ListLen=len(list1)-1
    #print(ListLen)
    Total=0
    while ListLen>=0:
        Total=Total+StrickPreNumber[list1[ListLen]]
        ListLen=ListLen-1
    return Total

#给JugeThisStrick函数用的，把多个数字拆分为单个数字如输入进的数据为111则返回[1,1,1]
def GetPreNBr(value):
    result=[]
    while value:
        result.append(value%10)
        value=value//10
    result.reverse()
    #print(result)
    return result

#处理到哪了
def Update():
    global MaxNumber
    global TargetTimeNumber
    global AllTimes
    this=0
    while this<=MaxNumber:
        #print("this=",this)
        nbr=JugeThisStrick(this)
        #print("nbr=",nbr)
        if nbr==TargetTimeNumber:
            print(this)
            AllTimes=AllTimes+1
        this=this+1

#程序开始
print("Designed by NortzWolfy")
print("您可使用Ctrl+C强制终止进程")
while True:
    AllTimes=0
    GetTargetNumber()
    GetMaxNumber()
    print("开始计算，参数过大可能需要一些时间")
    Update()
    print("火柴总数:",TargetTimeNumber,"取舍范围:0 ~",MaxNumber,"符合要求个数:",AllTimes)
    print("")
