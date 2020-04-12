from tkinter import *
from tkinter import ttk
root=Tk()


def CheckArrive(Time,ArriveTime):
     if ArriveTime<=Time:
        return True
     else:
         return False



def main():
     scheduler =input("Enter the type: ")
     NoOfProcesses=int (input("Enter the no of processes: "))
     if scheduler=="sjf non preemptive":
         Process=[]
         ArrivalT=[]
         Burst=[]
         TotalWaitingTime=0
         for i in range(NoOfProcesses):
             data=input("Enter the process,arrival time,burst time \n")
             X=data.split(',')
             Process.append(X[0])
             ArrivalT.append(float(X[1]))
             Burst.append(float(X[2]))

         Time=0
         TotalBurst = 0
         z=0
         while z < NoOfProcesses:
             TotalBurst += Burst[z]
             z += 1
         TrueIndex = 0
         while Time<=TotalBurst:
             while i<100000:
                 if(CheckArrive(Time,ArrivalT[TrueIndex])==True):
                     flag1=0
                     counter=0
                     while counter<len(Process):
                         if(CheckArrive(Time,ArrivalT[counter])==True and Burst[counter]<Burst[TrueIndex]):
                             flag1=1
                             IndexProcessOfLeastBurst=counter
                             TrueIndex=IndexProcessOfLeastBurst
                         else:
                             if flag1!=1:
                                 IndexProcessOfLeastBurst=TrueIndex
                         counter+=1

                     i+=1
                     Time+=Burst[TrueIndex]
                     print(Time)
                     print(Process[TrueIndex]+" is finshed")
                     ProcessWaitingTime=(Time-ArrivalT[TrueIndex]-Burst[TrueIndex])
                     print(("Process Waiting time is: ")+str(ProcessWaitingTime))
                     TotalWaitingTime+=ProcessWaitingTime
                     del Process[TrueIndex]
                     del ArrivalT[TrueIndex]
                     del Burst[TrueIndex]
                     TrueIndex=0
                     if(len(Process)==0):
                         break
             if(len(Process)==0):
                 break
         AvgWaitingTime = TotalWaitingTime / NoOfProcesses
         print(("total AVG waiting time: ") + str(AvgWaitingTime))


if __name__ == '__main__': main()
