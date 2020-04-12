from tkinter import *
from tkinter import ttk
root=Tk()
def Time1(time):
    Q=round(time,1)
    return Q


def CheckArrive(Time,ArriveTime):
     if ArriveTime<=Time:
        return True
     else:
         return False

def main():
    scheduler = input("Enter the type: ")
    NoOfProcesses = int(input("Enter the no. of processes: "))
    if scheduler == "sjf preemptive":
        Process = []
        ArrivalT = []
        Burst = []
        RemainingTime=[]
        TotalWaitingTime=0
        for i in range(NoOfProcesses):
            data = input("Enter the process,arrival time,burst time \n")
            X = data.split(',')
            Process.append(X[0])
            ArrivalT.append(X[1])
            Burst.append(X[2])
            RemainingTime.append(round(float(Burst[i]),1))

        Time =0
        TimeAfter=0
        extra=0
        i=0
        z=0
        TotalBurst=0
        while z<NoOfProcesses:
            TotalBurst+=float(Burst[z])
            z+=1
        TrueIndex =0
        while Time1(Time)<=TotalBurst:
            while i<100000   :

                if (CheckArrive(TimeAfter,float(ArrivalT[TrueIndex])))==True and (RemainingTime[TrueIndex]>0.11):
                    flag1=0
                    counter = 0
                    while counter<(len(Process)):
                        if (CheckArrive(Time1(Time),float(ArrivalT[counter]))==True ) and (RemainingTime[counter]<RemainingTime[TrueIndex]) and(RemainingTime[counter]>0) :
                            flag1=1
                            IndexProcessOfLeastBurst=counter
                            TrueIndex = IndexProcessOfLeastBurst
                            TimeAfter=Time1(Time)
                        elif (CheckArrive(Time1(Time),float(ArrivalT[counter]))!=True) or (RemainingTime[counter]>RemainingTime[TrueIndex] or (len(Process)==1)) :
                            if flag1 !=1 :
                                IndexProcessOfLeastBurst=TrueIndex

                        counter += 1
                    RemainingTime[IndexProcessOfLeastBurst] -= 0.1
                    RemainingTime1 = ['%.1f' % elem for elem in RemainingTime]
                    print(RemainingTime1[IndexProcessOfLeastBurst])
                    Time+=round(0.1,1)



                    i+=1

                elif(CheckArrive(TimeAfter,float(ArrivalT[TrueIndex])))==TRUE and (-0.1<=RemainingTime[TrueIndex]<=0.12):
                    print(Process[TrueIndex]+" is finished")
                    extra+=0.1
                    ProcessWaitingTime =(Time1(Time)+extra)-round(float(ArrivalT[TrueIndex]),1)-round(float(Burst[TrueIndex]),1)
                    print(("Process Waiting time is: ")+str(ProcessWaitingTime))
                    TotalWaitingTime+=ProcessWaitingTime
                    del Process[TrueIndex]
                    del ArrivalT[TrueIndex]
                    del Burst[TrueIndex]
                    del RemainingTime[TrueIndex]
                    i+=1
                    TrueIndex=0
                    if (len(Process)==0):
                        break
            if (len(Process)==0):
                        break

        AvgWaitingTime=TotalWaitingTime/NoOfProcesses
        print(("total AVG waiting time: ")+str(AvgWaitingTime))








if __name__ == '__main__': main()