import numpy  as np

ua = 1.5E10+9
distancia_terra_lua = 384400000

#terra 
m_t = 5.972E+24
r_t = np.array([ua, 0])
v_t = np.array([29800, 0])

#lua 
m_l = 0.073E+24
r_l = np.array([ua + distancia_terra_lua, 0])
v_l = np.array([1000, 0])

#sol
m_s = 1.989E+30
r_s = np.array([0, 0])
#v_s = 0 --> repouso 


#time --> simulacao 
#dt --> grafico
t0 = 0
dt = 0.01
