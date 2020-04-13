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

def InputSjfNonPreemptive():
    NoOfProcesses = int(input())  # "Enter the no. of processes: "
    Process = []
    ArrivalT = []
    Burst = []
    for i in range(NoOfProcesses):
        data = input()  # Enter the process,arrival time,burst time
        X = data.split(',')
        Process.append(X[0])
        ArrivalT.append(X[1])
        Burst.append(X[2])
    return NoOfProcesses,Process,ArrivalT,Burst

def SJFNonPreemptive(NoOfProcesses,Process,ArrivalT,Burst):
    zyadat = []
    ProcessIn = []
    TimeIn = []
    flag = 0
    AA = 0
    while AA < NoOfProcesses:
        zyadat.append(1000)
        AA += 1
    mgmo3Elzyadat = 0
    TotalWaitingTime = 0
    for i in range(NoOfProcesses):
        for x in range(i + 1, NoOfProcesses):
            if (float(ArrivalT[i]) + float(Burst[i]) < float(ArrivalT[x])):
                if ((float(ArrivalT[x]) - (float(ArrivalT[i]) + float(Burst[i]))) < zyadat[i]):
                    zyadat[i] = float(ArrivalT[x]) - (float(ArrivalT[i]) + float(Burst[i]))

    for i in range(NoOfProcesses):
        if (zyadat[i] < 1000):
            mgmo3Elzyadat += zyadat[i]
    if float(ArrivalT[0]) > 0:
        mgmo3Elzyadat += float(ArrivalT[0])
    Time = 0
    TotalBurst = 0
    z = 0
    while z < NoOfProcesses:
        TotalBurst += float(Burst[z])
        z += 1
    TotalBurst += mgmo3Elzyadat
    TrueIndex = 0
    while Time <= TotalBurst:
        while i < 100000:
            if (CheckArrive(Time, float(ArrivalT[TrueIndex])) == True and flag == 1):
                TimeIn.append(Time1(Time))
                ProcessIn.append("Null")
                flag = 0
            elif (CheckArrive(Time, float(ArrivalT[TrueIndex])) == True):
                flag1 = 0
                counter = 0
                while counter < len(Process):
                    if (CheckArrive(Time, float(ArrivalT[counter])) == True and float(Burst[counter]) < float(Burst[TrueIndex])):
                        flag1 = 1
                        IndexProcessOfLeastBurst = counter
                        TrueIndex = IndexProcessOfLeastBurst
                    else:
                        if flag1 != 1:
                            IndexProcessOfLeastBurst = TrueIndex
                    counter += 1

                i += 1
                Time += float(Burst[TrueIndex])
                ProcessIn.append(Process[TrueIndex])
                TimeIn.append(Time1(Time))
                # print(Time)
                # print(Process[TrueIndex]+" is finshed")
                ProcessWaitingTime = (Time1(Time)) - round(float(ArrivalT[TrueIndex]), 1) - round(float(Burst[TrueIndex]), 1)                # print(("Process Waiting time is: ")+str(ProcessWaitingTime))
                TotalWaitingTime += ProcessWaitingTime
                del Process[TrueIndex]
                del ArrivalT[TrueIndex]
                del Burst[TrueIndex]
                TrueIndex = 0
                if (len(Process) == 0):
                    break
            elif (CheckArrive(Time, float(ArrivalT[TrueIndex])) == False):
                flag = 1
                Time += 0.1
                Time = Time1(Time)
        if (len(Process) == 0):
            break
    #for b in range(len(ProcessIn)):
        #print(ProcessIn[b])
        #print(TimeIn[b])
    AvgWaitingTime = TotalWaitingTime / NoOfProcesses
    #print(("total AVG waiting time: ") + str(AvgWaitingTime))
    return ProcessIn, TimeIn, AvgWaitingTime


def main():
    SchedularType=input()
    if SchedularType=="sjf non preemptive":
        NoOfProcesses, Process, ArrivalT, Burst = InputSjfNonPreemptive()
        ProcessIn, TimeIn, AvgWaitingTime = SJFNonPreemptive(NoOfProcesses, Process, ArrivalT, Burst)
        # --------------------------------For Testing Only---------------------------------

        for b in range(len(ProcessIn)):
            print(ProcessIn[b])
            print(TimeIn[b])
        print(("total AVG waiting time: ") + str(AvgWaitingTime))

        # ----------------------------------------------------------------------------------




if __name__ == '__main__': main()
