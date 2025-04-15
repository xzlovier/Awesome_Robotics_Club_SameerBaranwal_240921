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
def test_inverse_kinematics():
    test_cases = [
        {"name": "Test 1 - Typical", "coords": (10, 5, -5)},
        {"name": "Test 2 - Near base", "coords": (1, 1, -1)},
        {"name": "Test 3 - Near max reach", "coords": (25, 0, 0)},
        {"name": "Test 4 - Unreachable", "coords": (50, 50, 50)},
        {"name": "Test 5 - Deep negative Z", "coords": (5, 0, -25)},
    ]

    for test in test_cases:
        print(f"\n{test['name']}")
        x, y, z = test["coords"]
        print(f"Target Position: x={x}, y={y}, z={z}")
        try:
            alpha_deg, beta_deg, gamma_deg = inverse_kinematics(x, y, z)
            print(f"Joint Angles: α = {alpha_deg:.2f}°, β = {beta_deg:.2f}°, γ = {gamma_deg:.2f}°")
            print("Result: ✅ Reachable")
        except ValueError as e:
            print(f"Result: ❌ Unreachable — {e}")
test_inverse_kinematics()
