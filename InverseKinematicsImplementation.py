
import math
def inverse_kinematics(x, y, z):
    L1 = 5.0  
    L2 = 10.0  
    L3 = 15.0  

    
    r = math.sqrt(x**2 + y**2)
    alpha = math.atan2(y, x) 
    
    dx = r - L1  
    dz = z
    d = math.sqrt(dx**2 + dz**2)

    
    if d > (L2 + L3):
        raise ValueError("Target is unreachable")

    
    cos_gamma = (L2**2 + L3**2 - d**2) / (2 * L2 * L3)
    gamma = math.acos(cos_gamma) 
    gamma = math.pi - gamma  

    
    cos_beta = (L2**2 + d**2 - L3**2) / (2 * L2 * d)
    beta_offset = math.acos(cos_beta)
    leg_angle = math.atan2(dz, dx)
    beta = leg_angle + beta_offset


    alpha_deg = math.degrees(alpha)
    beta_deg = math.degrees(beta)
    gamma_deg = math.degrees(gamma)

    return alpha_deg, beta_deg, gamma_deg

a =int(input('er x-component of final location'))
b =int(input('er y-component of final location'))
c=int(input("ter z-component of final location"))
target = (a,b, c)
angles = inverse_kinematics(*target)
if angles:
    print(f"Joint Angles (degrees): alpha = {angles[0]:.2f}, beta = {angles[1]:.2f}, gamma = {angles[2]:.2f}")

