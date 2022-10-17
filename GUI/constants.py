# {
# 'sensor1': value1,
# 'sensor2': value2,
# 'sensor3': value3,
# 'sensor4': value4,
# 'sensor5': value5,
# 'Thermistor': [value1, value2, value3, value4, value5]
# }
# {
# 'sensor1': value1,
# 'Pressure': value1
# }
# {
# 'sensor1': value1,
# 'Distance: value1
# }
# {
# 'sensor1': value1,
# ‘Sensor2’: value2
# 'Angular Rate': value1
# ‘Acceleration’: value2
# }

# FSM Data
CURRENT_STATE = "Deceleration"
STATES = {
    'Stop': 'state_icons/stop.png',
    'Crawl': 'state_icons/crawl.png',
    'Deceleration': 'state_icons/deceleration.png',
    'Cruise': 'state_icons/cruise.png',
    'Emergency': 'state_icons/emergency.png',
    'Verification': 'state_icons/verification.png',
    'Pre-Acceleration': 'state_icons/pre_acceleration.png',
    'Acceleration': 'state_icons/acceleration.png',
    'Overheating': 'state_icons/overheating.png',
    'Extreme Overheating': 'state_icons/extreme_overheating.png'
}

# Battery Pack Data
BATTERY_CURRENT_TEMP = 0
BATTERY_MAXIMUM_TEMP = 100
BATTERY_1 = 40
BATTERY_2 = 82
BATTERY_3 = 100
BATTERY_4 = 0
BATTERY_5 = 67
VOLTAGE_BATT_1 = 40
VOLTAGE_BATT_2 = 82
VOLTAGE_BATT_3 = 100
VOLTAGE_BATT_4 = 0
VOLTAGE_BATT_5 = 67
CURRENT_BATT_1 = 40
CURRENT_BATT_2 = 82
CURRENT_BATT_3 = 100
CURRENT_BATT_4 = 0
CURRENT_BATT_5 = 67
# BATTERY_6 = 72
# BATTERY_7 = 94
# BATTERY_8 = 89

# Inductive Proximity Sensor Data
PROXIMITY_INPUT1 = 2
PROXIMITY_LED1 = 13
PROXIMITY_SENSOR_STATE1 = "high"
PROXIMITY_INPUT2 = 2
PROXIMITY_LED2 = 13
PROXIMITY_SENSOR_STATE2 = "high"
PROXIMITY_INPUT3 = 2
PROXIMITY_LED3 = 13
PROXIMITY_SENSOR_STATE3 = "high"
PROXIMITY_INPUT4 = 2
PROXIMITY_LED4 = 13
PROXIMITY_SENSOR_STATE4 = "high"

# Vibration Sensor Data
VIBRATIONLEVEL = "low"

# Inertial Measurement Unit Data
CURRENT_VELOCITY = 50
ACCELERATION = 70
VELOCITY_THRESHOLD = 60
ACCELERATION_THRESHOLD = 60
PITCH = [90, -132, 54, 2]
YAW = [129, 0, -83, 324]
ROLL = [-12, 55, 39, 360]

# Pressure Sensor Data
ABSOLUTE_PRESSURE = 30.29
RELATIVE_PRESSURE = 29.80
ALTITUDE = 33000

# Long Distance Range Finder Data
DISTANCE = 30

# Progress Bar Data
LABEL_STYLE_SHEET = "color: blue; background-color: grey; selection-color: grey; selection-background-color: blue;"
PBAR_LOW_PROGRESS = "QProgressBar::chunk {background-color: red;}"
PBAR_MED_PROGRESS = "QProgressBar::chunk {background-color: gold;}"
PBAR_HIGH_PROGRESS = "QProgressBar::chunk {background-color: green;}"
