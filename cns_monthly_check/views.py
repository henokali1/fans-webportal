from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Base URL's
@login_required
def cns_monthly_check(request):
    return render(request, 'cns_monthly_check/cns_monthly_check.html')

# AFTN AND CADAS
@login_required
def aftn_and_cadas(request):
    return render(request, 'cns_monthly_check/aftn_and_cadas.html')

# ATIS
@login_required
def atis(request):
    return render(request, 'cns_monthly_check/atis.html')

# ATS RADAR DISPLAY SYSTEM
@login_required
def ats_radar_display_system(request):
    return render(request, 'cns_monthly_check/ats_radar_display_system.html')

# AWS RWY 11 29 CEILOMETER 29
@login_required
def aws_rwy_11_29_ceilometer_29(request):
    return render(request, 'cns_monthly_check/aws_rwy_11_29_ceilometer_29.html')

# DGVOX RECORDING SYSTEM
@login_required
def dgvox_recording_system(request):
    return render(request, 'cns_monthly_check/dgvox_recording_system.html')

# DVOR
@login_required
def dvor(request):
    return render(request, 'cns_monthly_check/dvor.html')

# EQUIPMENT ROOM SERVERS PM
@login_required
def equipment_room_servers_pm(request):
    return render(request, 'cns_monthly_check/equipment_room_servers_pm.html')

# GLIDEPATH
@login_required
def glidepath(request):
    return render(request, 'cns_monthly_check/glidepath.html')

# HP DME
@login_required
def hp_dme(request):
    return render(request, 'cns_monthly_check/hp_dme.html')

# JOTRON TX RX VHF
@login_required
def jotron_tx_rx_vhf(request):
    return render(request, 'cns_monthly_check/jotron_tx_rx_vhf.html')

# LOCALIZER
@login_required
def localizer(request):
    return render(request, 'cns_monthly_check/localizer.html')

# LP DME
@login_required
def lp_dme(request):
    return render(request, 'cns_monthly_check/lp_dme.html')

# RDD
@login_required
def rdd(request):
    return render(request, 'cns_monthly_check/rdd.html')

# REMOTE MONITORS WORKSHOP
@login_required
def remote_monitors_workshop(request):
    return render(request, 'cns_monthly_check/remote_monitors_workshop.html')

# SCHMID REPORT
@login_required
def schmid_report(request):
    return render(request, 'cns_monthly_check/schmid_report.html')

# UHF BASE RADIO VHF
@login_required
def uhf_base_radio_vhf(request):
    return render(request, 'cns_monthly_check/uhf_base_radio_vhf.html')

# VHF GROUND TO AIR RADIOS
@login_required
def vhf_ground_to_air_radios(request):
    return render(request, 'cns_monthly_check/vhf_ground_to_air_radios.html')
