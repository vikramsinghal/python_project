rivers = {
    'nile':'egypt',
    'thames':'london',
    'mississippi river':'minneasota',
    'missouri':'missouri',
}
for river_name, location in rivers.items():
    print(f"{river_name.title()} runs in {location.title()}.")

for river_name in rivers.keys():
    print(river_name.title())

for location in rivers.values():
    print(location.title())
