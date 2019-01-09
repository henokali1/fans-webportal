from django.urls import path
from . import views


urlpatterns = [
    path('', views.cns_monthly_check, name='cns_monthly_check.html'),
    path('aftn_and_cadas/', views.aftn_and_cadas, name='aftn_and_cadas.html'),
    path('atis/', views.atis, name='atis.html'),
    path('ats_radar_display_system/', views.ats_radar_display_system, name='ats_radar_display_system.html'),
    path('aws_rwy_11_29_ceilometer_29/', views.aws_rwy_11_29_ceilometer_29, name='aws_rwy_11_29_ceilometer_29.html'),
    path('dgvox_recording_system/', views.dgvox_recording_system, name='dgvox_recording_system.html'),
    path('dvor/', views.dvor, name='dvor.html'),
    path('equipment_room_servers_pm/', views.equipment_room_servers_pm, name='equipment_room_servers_pm.html'),
    path('glidepath/', views.glidepath, name='glidepath.html'),
    path('hp_dme/', views.hp_dme, name='hp_dme.html'),
    path('jotron_tx_rx_vhf/', views.jotron_tx_rx_vhf, name='jotron_tx_rx_vhf.html'),
    path('localizer/', views.localizer, name='localizer.html'),
    path('lp_dme/', views.lp_dme, name='lp_dme.html'),
    path('rdd/', views.rdd, name='rdd.html'),
    path('remote_monitors_workshop/', views.remote_monitors_workshop, name='remote_monitors_workshop.html'),
    path('schmid_report/', views.schmid_report, name='schmid_report.html'),
    path('uhf_base_radio_vhf/', views.uhf_base_radio_vhf, name='uhf_base_radio_vhf.html'),
    path('vhf_ground_to_air_radios/', views.vhf_ground_to_air_radios, name='vhf_ground_to_air_radios.html'),
]
