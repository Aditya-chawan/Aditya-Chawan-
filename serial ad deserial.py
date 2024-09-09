from os import system


def save_simulation_to_json(ecosystem: system, filename: str):
    with open(filename, 'w') as f:
        f.write(ecosystem.json())

def load_simulation_from_json(filename: str) -> system:
    with open(filename, 'r') as f:
        return system.parse_raw(f.read())