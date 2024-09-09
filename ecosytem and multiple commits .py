from sqlite3.dbapi2 import _Parameters


def main():
    # Define UV parameters for the star (UV emitted by the star)
    uv_params = _Parameters(wavelength=300, intensity=1000)
    
    # Define planets with their gas layers
    planet1 = planet1(
        name="Planet A",
        distance_from_star=1.0,  # Earth-like distance
        gas_layer= GlobalGasLayer (gas_name="Ozone", concentration=500, absorption_rate=0.5) # type: ignore
    )
    
    planet2 = planet1(
        name="Planet B",
        distance_from_star=2.0,  # Further away from the star
        gas_layer= GlobalGasLayer(gas_name="Helium", concentration=300, absorption_rate=0.3) # type: ignore
    )
    
    # Create an ecosystem with a star and its planets
    ecosystem = ecosystem(
        star_name="Alpha Centauri",
        uv_parameters=uv_params,
        planets=[planet1, planet2]
    )
    
    # Run the simulation for multiple commits
    ecosystem.run_multiple_commits(num_commits=5)

if __name__ == "__main__":
    main()