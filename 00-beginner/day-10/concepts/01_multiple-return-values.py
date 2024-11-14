# Create a function with multiple return values
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide one or both of the inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

# Call the format name function for name
format_name(f_name="Henry",l_name="Fasakin")