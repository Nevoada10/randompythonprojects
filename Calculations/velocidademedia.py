# Defining the known values
distance = 100 # meters
time = 0*(60**2) + 0*60 + 51.25 # seconds

# Calculating the average speed in m/s
average_speed_m_s = distance / time

# Converting to km/h (1 m/s = 3.6 km/h)
average_speed_km_h = average_speed_m_s * 3.6

# Rounding to two decimal places
average_speed_m_s = round(average_speed_m_s, 2)
average_speed_km_h = round(average_speed_km_h, 2)


# Debugging
print(f"Distance: {distance} meters | Time: {time} seconds")
# Printing the results
print(f"Average speed: {average_speed_m_s} m/s or {average_speed_km_h} km/h")
