import math

print("\n🚀 Rocket Trajectory Simulator\n")

angle = float(input("Launch Angle (degrees): "))
velocity = float(input("Initial Velocity (m/s): "))

g = 9.81

theta = math.radians(angle)

max_height = (velocity ** 2 * math.sin(theta) ** 2) / (2 * g)

flight_time = (2 * velocity * math.sin(theta)) / g

horizontal_range = (velocity ** 2 * math.sin(2 * theta)) / g

print("\n===== Results =====")
print(f"Maximum Height: {max_height:.2f} m")
print(f"Flight Time: {flight_time:.2f} s")
print(f"Horizontal Range: {horizontal_range:.2f} m")
