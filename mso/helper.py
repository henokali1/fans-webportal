from users.models import CustomUser


# Returns full name of a give user(emal)
def get_full_name(email):
    first_name = CustomUser.objects.values_list('first_name', flat=True).filter(email=email)[0].lower()
    last_name = CustomUser.objects.values_list('last_name', flat=True).filter(email=email)[0].lower()    
    return first_name.capitalize() + ' ' + last_name.capitalize()
