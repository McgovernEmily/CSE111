# I added another function that calculates kPa to psi and I added a testing
# for that function. 


# Function that will use calculations to find the column height.
def water_column_height(tower_height, tank_height):
    """Calculates and returns the height of a column of water.
    Column of water is 3 multiplied by height of the walls of the tank
    divided by four, then add the height of the tower.
    
    Parameters
        tower_height: height of the tower
        tank_height: height of the walls of the tank
          that is on top of the tower
    Return: height of a column of water
    """

    # Calculating the water column height.
    height_of_column = tower_height + ((3 * tank_height) / 4)

    return height_of_column

# Function that will use calculations to find the pressure caused by Earth.
def pressure_gain_from_water_height(height):
    """Calculates and returns the pressure caused by Earth's 
    gravity pulling on the water stored in an elevated tank.
    Pressure gained is the density of water multiplied by acceleration from Earths
    gravity multiplied again by height of the water column, then all of that divided
    by 1000.

    Parameters
        height: height of the water column in meters
    Return: pressure in kilopascals
    """


    d = 998.2 # Density of water in kg/m^3
    g = 9.80665 # Acceleration from Earths gravity m/sec^2

    # Finding the pressure in kilopascals.
    pressure = (d * g * height) / 1000

    return pressure

# Function that will calculate the water pressure lost.
def pressure_loss_from_pipe(pipe_diameter,
    pipe_length, friction_factor, fluid_velocity):
    """Calculates and returns the water pressure lost because of the 
    friction between the water and the walls of a pipe that it flows through.
    Pressure lost is - pipe's friction multiplied by both length of pipe, 
    density of water, and velocity of water flowing squared, then all of it divided by
    2000 multiplied by diameter of the pipe.

    Parameters
        pipe_diameter: diameter of the pipe in meters
        pipe_length: length of the pipe in meters
        friction_factor: pipe's friction factor
        fluid_velocity: velocity of the water flowing through the pipes in meters/second
    Return: lost of pressure in kilopascals
    """

    d = 998.2 # Density of water in kg/m^3

    # Calculating the lost pressure.
    lost_pressure = ((-friction_factor) * pipe_length * d * (fluid_velocity**2)) / (2000 * pipe_diameter)
    
    return lost_pressure

# Function that will calculate the pressure lost from fittings.
def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """calculates the water pressure lost because of fittings such as 45° 
    and 90° bends that are in a pipeline.
    Pressure lost from fittings is found by -0.04 multiplied by both density of water,
    velocity of water squared, and quantity of fittings, then divided by 2000.

    Parameters
        fluid_velocity: velocity of the water flowing through the pipe in meters/second
        quantity_fittings: quantity of fittings
    Return: lost of pressure in kilopascals
    """
    
    d = 998.2 # Density of water in kg/m^3

    # Calculating the pressure lost from fittings.
    lost_pressure_fittings = (-0.04 * d * (fluid_velocity ** 2) * quantity_fittings) / 2000

    return lost_pressure_fittings

# Function will calculate the Reynolds number for a pipe.
def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calculates and returns the Reynolds number for a pipe with water flowing through it.
    Reynolds number is density of water multiplied by hydraulic diameter of a pipe and velocity 
    of water flowing through a pipe, then divided by dynamic viscosity of water.

    Parameters
        hydraulic_diameter: hydraulic diameter of a pipe in meters
        fluid_velocity: velocity of the water flowing through the pipe in meters/second
    Return: lost of pressure in kilopascals
    """

    d = 998.2 # Density of water in kg/m^3.
    dynamic_visc = 0.0010016 # Dynamic viscosity of water in pascal seconds.

    # Calculating the Reynolds number.
    reynolds_num = (d * hydraulic_diameter * fluid_velocity) / dynamic_visc

    return reynolds_num

# Function will calculate the water pressure lost from water moving from a 
# big pipe to a small pipe.
def pressure_loss_from_pipe_reduction(larger_diameter,
    fluid_velocity, reynolds_number, smaller_diameter):
    """Calculates the water pressure lost because of water moving from a pipe 
    with a large diameter into a pipe with a smaller diameter.

    Parameters
        larger_diameter: diameter of the larger pipe in meters
        fluid_velocity: velocity of the water flowing through the pipe in meters/second
        reynolds_number: Reynolds number that corresponds to the pipe with the larger diameter
        smaller_diameter: diameter of the smaller pipe in meters
    Return: lost pressure in kilopascals
    """

    d = 998.2 # Density of water in kg/m^3.

    # Calculating the constant.
    constant = (0.1 + (50/reynolds_number)) * (((larger_diameter / smaller_diameter) ** 4) -1)

    # Calculating the lost pressure in kilopascals.
    large_small_pipe_pressure_lost = (-constant * d * (fluid_velocity**2)) / 2000

    return large_small_pipe_pressure_lost

# Function will convert kPa to psi.
def kilopascals_to_pounds_per_square_inch(pressure_kpa):
    """Converts kilopascals to pounds per square inch.
    
    Parameters
        pressure_kpa: the pressure in kilopascals
    Return: the pressure in pounds per square inch
    """
    
    # Calculating the psi pressure.
    pressure_psi = pressure_kpa * 0.1450377377
    pressure_psi = round(pressure_psi, 4)

    return pressure_psi


PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    # Converting the pressure to psi instead of kPa.
    psi_pressure = kilopascals_to_pounds_per_square_inch(pressure)

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {psi_pressure:.1f} pounds per square inch (psi)")


if __name__ == "__main__":
    main()