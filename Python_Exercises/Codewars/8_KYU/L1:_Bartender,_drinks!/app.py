def get_drink_by_profession(param):
    dict = {
        "jabroni": "Patron Tequila",
        "school counselor": "Anything with Alcohol",
        "programmer": "Hipster Craft Beer",
        "politician": "Your tax dollars",
        "bike gang member": "Moonshine",
        "rapper": "Cristal" 
    }
    return dict[param.lower()] if param.lower() in dict else "Beer"