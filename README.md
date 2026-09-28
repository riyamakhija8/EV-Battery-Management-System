# EV Battery Management System (BMS) Simulation

A Python-based Battery Management System (BMS) simulation for a Lithium-Ion battery pack used in Electric Vehicles (EVs).

## Project Overview

The Battery Management System is responsible for monitoring and managing important battery parameters to ensure safe and efficient battery operation.

This project simulates a BMS dashboard that monitors:

- State of Charge (SOC)
- State of Health (SOH)
- Battery Voltage
- Charging/Discharging Current
- Battery Temperature
- Individual Cell Voltage
- Cell Balancing
- Thermal Management
- Fault Detection

## Project Objectives

The main objectives of this project are:

1. To simulate monitoring of a Lithium-Ion EV battery pack.
2. To estimate the State of Charge (SOC).
3. To estimate the State of Health (SOH).
4. To monitor battery voltage, current and temperature.
5. To detect abnormal battery conditions.
6. To simulate cell balancing.
7. To visualize battery parameters through an interactive dashboard.

## Key Features

### SOC Estimation

State of Charge represents the remaining charge available in the battery.

The project uses a Coulomb Counting based approach:

\[
SOC_{new} = SOC_{old} - \frac{I \times \Delta t}{Q} \times 100
\]

where:

- `I` = Battery current
- `Δt` = Time interval
- `Q` = Battery capacity

### SOH Estimation

State of Health represents the current health of the battery compared with its original rated capacity.

\[
SOH = \frac{Available\ Capacity}{Rated\ Capacity} \times 100
\]

### Thermal Management

Battery heat generation is simulated using:

\[
P_{heat} = I^2R
\]

where:

- `P` = Heat generation
- `I` = Battery current
- `R` = Internal resistance

### Cell Monitoring

The battery pack is simulated using a 4S1P configuration.

Each individual cell voltage is monitored to identify voltage differences between cells.

### Cell Balancing

The BMS detects voltage differences between cells and indicates when balancing is required.

### Fault Detection

The system monitors abnormal conditions such as:

- Over Voltage
- Under Voltage
- Over Current
- Over Temperature
- Cell Imbalance

### Charging and Discharging

The dashboard supports both:

- Charging mode
- Discharging mode

The SOC changes according to the selected operating mode and battery current.

## Battery Pack Configuration

| Parameter | Value |
|---|---|
| Battery Type | Lithium-Ion |
| Configuration | 4S1P |
| Number of Cells | 4 |
| Rated Capacity | 3 Ah |
| Cell Voltage | ~3.7 V nominal |
| Maximum Cell Voltage | 4.2 V |
| Minimum Cell Voltage | 3.0 V |

## System Architecture

```text
                 Battery Pack
                      |
          +-----------+-----------+
          |           |           |
       Voltage      Current    Temperature
       Monitoring   Monitoring   Monitoring
          |           |           |
          +-----------+-----------+
                      |
                     BMS
                      |
        +-------------+-------------+
        |             |             |
       SOC           SOH        Thermal
    Estimation    Estimation    Management
        |             |             |
        +-------------+-------------+
                      |
               Safety Monitoring
                      |
          +-----------+-----------+
          |           |           |
      Over Voltage  Over Current  Over Temperature
                      |
               Cell Monitoring
                      |
               Cell Balancing
                      |
              BMS Dashboard
