from django.shortcuts import render

# Base URL's
def cns_monthly_check(request):
    return render(request, 'cns_monthly_check/cns_monthly_check.html')

# aftn_and_cadas
def aftn_and_cadas(request):
    return render(request, 'cns_monthly_check/aftn_and_cadas.html')

# atis
def atis(request):
    return render(request, 'cns_monthly_check/atis.html')

# ats_radar_display_system
def ats_radar_display_system(request):
    return render(request, 'cns_monthly_check/ats_radar_display_system.html')

# ats_radar_display_system
def aws_rwy_11_29_ceilometer_29(request):
    return render(request, 'cns_monthly_check/aws_rwy_11_29_ceilometer_29.html')

# dgvox_recording_system
def dgvox_recording_system(request):
    return render(request, 'cns_monthly_check/dgvox_recording_system.html')

# dvor
def dvor(request):
    return render(request, 'cns_monthly_check/dvor.html')

# equipment_room_servers_pm
def equipment_room_servers_pm(request):
    return render(request, 'cns_monthly_check/equipment_room_servers_pm.html')

# glidepath
def glidepath(request):
    return render(request, 'cns_monthly_check/glidepath.html')

# hp_dme
def hp_dme(request):
    return render(request, 'cns_monthly_check/hp_dme.html')

# jotron_tx_rx_vhf
def jotron_tx_rx_vhf(request):
    return render(request, 'cns_monthly_check/jotron_tx_rx_vhf.html')

# localizer
def localizer(request):
    return render(request, 'cns_monthly_check/localizer.html')

# lp_dme
def lp_dme(request):
    return render(request, 'cns_monthly_check/lp_dme.html')

# rdd
def rdd(request):
    return render(request, 'cns_monthly_check/rdd.html')

# remote_monitors_workshop
def remote_monitors_workshop(request):
    return render(request, 'cns_monthly_check/remote_monitors_workshop.html')

# schmid_report
def schmid_report(request):
    return render(request, 'cns_monthly_check/schmid_report.html')

# uhf_base_radio_vhf
def uhf_base_radio_vhf(request):
    return render(request, 'cns_monthly_check/uhf_base_radio_vhf.html')

# vhf_ground_to_air_radios
def vhf_ground_to_air_radios(request):
    return render(request, 'cns_monthly_check/vhf_ground_to_air_radios.html')