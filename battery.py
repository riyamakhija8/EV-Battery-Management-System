import time

# =========================
# BATTERY PARAMETERS
# =========================

capacity = 3.0          # Ah
soc = 100.0             # %
soh = 100.0             # %
current = 2.0           # A
temperature = 25.0      # °C

max_voltage = 4.2       # V
min_voltage = 3.0       # V
resistance = 0.02       # Ohm


# =========================
# SIMULATION
# =========================

for t in range(61):

    # SOC calculation
    charge_used = (current * 1) / 3600
    soc_used = (charge_used / capacity) * 100

    soc = soc - soc_used

    # Voltage based on SOC
    voltage = min_voltage + ((max_voltage - min_voltage) * soc / 100)

    # Heat generation
    heat = (current ** 2) * resistance

    # Temperature increase
    temperature = temperature + (heat / 500)

    # =========================
    # BMS PROTECTION
    # =========================

    if voltage > max_voltage:
        status = "OVER VOLTAGE"

    elif voltage < min_voltage:
        status = "UNDER VOLTAGE"

    elif temperature >= 60:
        status = "CRITICAL TEMPERATURE"

    elif temperature >= 45:
        status = "HIGH TEMPERATURE"

    else:
        status = "NORMAL"

    # =========================
    # DISPLAY
    # =========================

    print("--------------------------------")
    print("Time:", t, "sec")
    print("Voltage:", round(voltage, 2), "V")
    print("Current:", current, "A")
    print("SOC:", round(soc, 2), "%")
    print("SOH:", soh, "%")
    print("Temperature:", round(temperature, 2), "°C")
    print("BMS Status:", status)

    time.sleep(0.05)