COLOR_CODE = {"aliceblue": "#f0f8ff", "thistle1": "#ffe1ff", "rosybrown1": "#ffc1c1", "red2": "#ee0000",
              "pink": "#ffc0cb", "maroon": "#b03060", "mediumpurple": "#9370db", "palegreen": "#98fb98",
              "palevioletred": "#db7093", "yellow1": "#ffff00"}

color_name = input("Enter color name: ")
if color_name in COLOR_CODE:
    print(color_name, "is", COLOR_CODE[color_name])
else:
    print("Invalid color name")
    state_code  input("Enter color name: ")

