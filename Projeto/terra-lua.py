import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import animation

# constantes
ua = 1.495978E11 
distancia_terra_lua = 384400000
G = 6.67430E-11

# terra
m_t = 5.972E+24
r_t = np.array([ua, .0])
v_t = np.array([0., ua*2*np.pi/365/24/3600])

# lua
m_l = 0.073E+24
r_l = np.array([ua + distancia_terra_lua, 0])
v_l = np.array([0., ua*2*np.pi/365/24/3600-distancia_terra_lua*2*np.pi/27.3/24/3600])

# sol
m_s = 1.989E+30
r_s = np.array([0., 0])
# v_s = 0 --> repouso


# time --> simulacao
# dt --> grafico
t0 = 0.
dt = 360.  # teste
tf = 365*24*3600  # teste

trajetoria = []


while t0 < tf:
    R_lt = r_l - r_t     #vetor diferença terra-lua 
    mR_lt = np.sqrt((R_lt ** 2).sum())
    F_lt = ((G * m_t * m_l) / mR_lt ** 3) * R_lt   #força da lua exercida sob a terra
    F_tl = - ((G * m_t * m_l) / mR_lt ** 3) * R_lt    #força da terra exercida sob a lua  

    R_sl = r_s - r_l   #distancia do sol até a  lua 
    mR_sl = np.sqrt((R_sl ** 2).sum())
    F_sl = ((G * m_s * m_l) / mR_sl ** 3) * R_sl     #força do sol exercida sob a lua 

    R_st = r_s - r_t #distancia do sol até a terra
    mR_st = np.sqrt((R_st ** 2).sum())
    F_st = ((G * m_s * m_t) / mR_st ** 3) * R_st    #força do sol exercida sob a terra 

    # aceleração da lua
    a_l = (F_tl + F_sl)/m_l

    # aceleração da terra
    a_t = (F_lt + F_st)/m_t

    # movimento

    v_t += a_t*dt
    v_l += a_l*dt

    r_l += v_l*dt
    r_t += v_t*dt

    t0 += dt
    trajetoria.append([t0,r_t[0],r_t[1],v_t[0],v_t[1],r_l[0],r_l[1],v_l[0],v_l[1]])
    
trajetoria = np.array(trajetoria)    
trajetoria[:,0] /= 3600*24
plt.plot(trajetoria[:,0],trajetoria[:,1],label= "x terra")
plt.plot(trajetoria[:,0],trajetoria[:,2],label= "y terra")
plt.plot(trajetoria[:,0],trajetoria[:,5],label= "x lua")
plt.plot(trajetoria[:,0],trajetoria[:,6],label= "y lua")
plt.plot(trajetoria[:,0],(trajetoria[:,5]**2+trajetoria[:,6]**2)**0.5,label= "r lua")
plt.plot(trajetoria[:,0],(trajetoria[:,1]**2+trajetoria[:,2]**2)**0.5,label= "r terra")
plt.legend()
plt.show()

plt.plot(trajetoria[:,1],trajetoria[:,2],label = "terra")
plt.plot(trajetoria[:,5],trajetoria[:,6],label = "lua")
plt.legend()
plt.gca().set_aspect(1)
plt.show()
