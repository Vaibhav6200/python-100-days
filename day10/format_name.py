def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    formatted_name = f"{formatted_f_name} {formatted_l_name}"
    return formatted_name

new_name = format_name("vAiBHaV", "PALiwaL")
print(new_name)