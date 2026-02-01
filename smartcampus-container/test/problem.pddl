(define (problem turn-on-bl1-sl1)
  (:domain smart_campus)

  (:requirements :strips :typing :fluents :durative-actions :negative-preconditions :timed-initial-literals)

  (:objects
    bl1_sl1 - room
    bl1_sl1_ac1 bl1_sl1_ac2 - air_conditioner
    bl1_sl1_light1 bl1_sl1_light2 - light
  )

  (:init
    (= (occupancy bl1_sl1) 10)

    (at 0.1
      (operating_hour))
    (at 0.6
      (not (operating_hour)))
  )

  (:goal
    (and
      (end_class_air bl1_sl1 bl1_sl1_ac1)
      (end_class_air bl1_sl1 bl1_sl1_ac2)
      (end_class_light bl1_sl1 bl1_sl1_light1)
      (end_class_light bl1_sl1 bl1_sl1_light2)
      (not (light_on bl1_sl1 bl1_sl1_light1))
      (not (light_on bl1_sl1 bl1_sl1_light2))
      (not (air_conditioner_on bl1_sl1 bl1_sl1_ac1))
      (not (air_conditioner_on bl1_sl1 bl1_sl1_ac2))
    )
  )
)