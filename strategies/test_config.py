import yaml

with open("example.yml", "r") as file:
    config_data = yaml.safe_load(file)
print(config_data)

indicators = config_data["strategy"]["indicators"].keys()

if "moving_average" in indicators:
    print(config_data["strategy"]["indicators"]["moving_average"])
if "rsi" in indicators:
    print(config_data["strategy"]["indicators"]["rsi"])
