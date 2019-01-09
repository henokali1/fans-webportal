from django.shortcuts import render

# Base URL's
def cns_monthly_check(request):
    return render(request, 'cns_monthly_check/cns_monthly_check.html')

# vhf_ground_to_air_radios
def vhf_ground_to_air_radios(request):
    return render(request, 'cns_monthly_check/vhf_ground_to_air_radios.html')
