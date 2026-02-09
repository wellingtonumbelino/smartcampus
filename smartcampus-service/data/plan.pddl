; --Plan #00001--------------------------
; -- Discretisation: 0.100----------------
; ---------------------------------------
0.100: ( start_campus_operating) [0.400]
0.301: ( turn_on_light_during_class bl1_sl1 bl1_sl1_light1) [0.200]
0.302: ( turn_on_light_during_class bl1_sl1 bl1_sl1_light2) [0.200]
0.303: ( turn_on_air_conditioner_during_class bl1_sl1 bl1_sl1_ac1) [0.200]
0.304: ( turn_on_air_conditioner_during_class bl1_sl1 bl1_sl1_ac2) [0.200]
0.405: ( turn_off_light_when_occupancy_zero bl1_sl1 bl1_sl1_light1) [0.100]
0.406: ( turn_off_light_when_occupancy_zero bl1_sl1 bl1_sl1_light2) [0.100]
0.407: ( turn_off_air_conditioner_when_occupancy_zero bl1_sl1 bl1_sl1_ac1) [0.100]
0.408: ( turn_off_air_conditioner_when_occupancy_zero bl1_sl1 bl1_sl1_ac2) [0.100]
; ---------------------------------------
; --Plan duration: 0.508, weight: 0005----
; ---------------------------------------