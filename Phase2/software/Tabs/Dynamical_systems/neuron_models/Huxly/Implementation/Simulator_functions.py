import Tabs.Dynamical_systems.neuron_models.Huxly.Implementation.variables as var
import numpy as np

def alpha_n(v):
    result = 0.32*(15-v+var.VT)/(np.exp((15-v+var.VT)/5) -1 )
    return result


def beta_n(v):
    result = 0.5* np.exp((10-v+var.VT)/40)
    return result

def alpha_m(v):
    result = 0.32*(13-v+var.VT)/(np.exp((13-v+var.VT)/4) -1 )
    return result

def beta_m(v):
    result = 0.28*(40-v+var.VT)/(np.exp((40-v+var.VT)/5) -1 )
    return result


def alpha_h(v):
    result = 0.128* np.exp((17-v+var.VT)/18)
    return result

def beta_h(v):
    result = 4/(np.exp((40-v+var.VT)/5)+1)
    return result


def v_dot(v, m, h, n, I):
    result = 1*var.g_l*(var.E_l-v) + var.g_na*m**3*h*(var.E_na - v) + var.g_k*n**4*(var.E_k - v) + I
    result /=  var.C_m

    return result

def n_dot(v, n):
    result = alpha_n(v)*(1-n) - beta_n(v)*n
    return result

def m_dot(v, m):
    result = alpha_m(v)*(1-m) - beta_m(v)*m
    return result

def h_dot(v, h):
    result = alpha_h(v)*(1-h) - beta_h(v)*h
    return result


def var_updater(var, var_dot_, dt):
    var += var_dot_ * dt
    return var


def experiment_run(v,n,m,h,I,t_total,dt):
    flag = -1
    v_list = []
    n_list = []
    m_list = []
    h_list = []
    spikes_number = 0

    for _ in range(50):

        hd = h_dot(v,h)
        h = var_updater(h, hd, dt)
        md = m_dot(v,m)
        m = var_updater(m, md, dt)
        nd = n_dot(v,n)
        n = var_updater(n, nd, dt)
        vd = v_dot(v,m,h,n,I)
        v = var_updater(v, vd, dt )
        v_list.append(v)
        n_list.append(n)
        m_list.append(m)
        h_list.append(h)




    for _ in range(50,int(t_total/dt)):

        hd = h_dot(v,h)
        h = var_updater(h, hd, dt)
        md = m_dot(v,m)
        m = var_updater(m, md, dt)
        nd = n_dot(v,n)
        n = var_updater(n, nd, dt)
        vd = v_dot(v,m,h,n,I)
        v = var_updater(v, vd, dt )
        v_list.append(v)
        n_list.append(n)
        m_list.append(m)
        h_list.append(h)
        if (v_list[-1] < v_list[-2]) and v_list[-1] > -40:
            flag = 1
            spikes_number += 1
            v  = -63
            #n=0
            m=0
            #h=0



    return v_list, n_list, m_list, h_list, spikes_number
