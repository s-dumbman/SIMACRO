import simacro
def printingCHECK(a):
    if a == 0:
        print("<", simacro.title, ">", "닫힘")
    if a == 1:
        print("<", simacro.title, ">", "실행됨")
    if a == 2:
        print("매크로 실행 대기중..")
    if a == 3:
        print("매크로 실행됨")
    if a == 4:
        print("매크로 중지됨")
        print("///------------------------///")