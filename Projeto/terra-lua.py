import numpy  as np

#constantes
ua = 1.5E10+9
distancia_terra_lua = 384400000
G = 6.67430E-11

#terra 
m_t = 5.972E+24
r_t = np.array([ua, 0])
v_t = np.array([0, 0])

#lua 
m_l = 0.073E+24
r_l = np.array([ua + distancia_terra_lua, 0])
v_l = np.array([0, 0])

#sol
m_s = 1.989E+30
r_s = np.array([0, 0])
#v_s = 0 --> repouso 


#time --> simulacao 
#dt --> grafico
t0 = 0
dt = 1   #teste 
tf = 5000   #teste

while t0 < tf:
	R_lt = r_l - r_t
	mR_lt = np.sqrt((R_lt**2).sum())
	F_tl = ((G*m_t*m_l)/mR_lt**3)*R_lt
	
	t0 += dt
