# /// VERSION v0.2 ///
# based on 2022-06-05
import simacro
#Local versionCODE
versionCODE = "v0.3"
def Copyright():
    t = '{}'.format("//SIMACRO//MADE BY D6CHECKER//")
    return t
def simacro_CHECKversion():
    print(simacro.title,"-",versionCODE)
if __name__=='__main__':
    simacro_CHECKversion()