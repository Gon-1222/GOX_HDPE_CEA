import numpy as np
import matplotlib.pyplot as plt
from rocketcea.cea_obj import  add_new_fuel, add_new_oxidizer
from rocketcea.cea_obj_w_units import CEA_Obj

HDPE_card = """
fuel HDPE C 2 H 4 wt%=100. 
h.kj/mol=-54.97 t(K)=298.15 rho.g/cc=0.96
"""
add_new_fuel('HDPE', HDPE_card )


ceaObj = CEA_Obj(propName='', oxName='GOX', fuelName="HDPE", cstar_units='m/s', pressure_units='MPa',temperature_units="K")

pcArr = [0.5,1,1.5,2]

for Pc in pcArr:
    mrArr = np.arange(0.1, 10.0, 0.05)
    cstarArr = [ceaObj.get_Cstar(Pc=Pc, MR=MR) for MR in mrArr]
    plt.plot(mrArr, cstarArr, label='Pc=%g MPa' % Pc)

plt.legend(loc='best')
plt.grid(True)
plt.title(ceaObj.desc)
plt.xlabel('O/F')
plt.ylabel('C* (m/s)')
plt.show()