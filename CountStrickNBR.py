StrickPreNumber=[6,2,5,5,4,5,6,3,7,6]
TargetTimeNumber=2
MaxNumber=0
AllTimes=0


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

def JugeThisStrick(Number):#55642
    if Number==0:
        return 6
    global StrickPreNumber
    list1=GetPreNBr(Number)
    ListLen=len(list1)-1
    print(ListLen)
    Total=0
    while ListLen>=0:
        Total=Total+StrickPreNumber[list1[ListLen]]
        ListLen=ListLen-1
    return Total

def GetPreNBr(value):
    result=[]
    while value:
        result.append(value%10)
        value=value//10
    result.reverse()
    print(result)
    return result


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

print("Designed by World Functions")
print("您可使用Ctrl+C强制终止进程")
while True:
    AllTimes=0
    GetTargetNumber()
    GetMaxNumber()
    print("开始计算，参数过大可能需要一些时间")
    Update()
    print("火柴总数:",TargetTimeNumber,"取舍范围:0 ~",MaxNumber,"符合要求个数:",AllTimes)
    print("")
