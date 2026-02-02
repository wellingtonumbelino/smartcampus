(define (problem turn-on-bl1-sl1)
  (:domain smart_campus)

  (:requirements :strips :typing :fluents :durative-actions :negative-preconditions :timed-initial-literals)

  (:objects
    bl1_sl1 - room
    bl1_sl1_ac1 bl1_sl1_ac2 - air-conditioner
    bl1_sl1_light1 bl1_sl1_light2 - light
  )

  (:init
    (= (work_time_duration) 0) ; 0 equivale a 0h

    (at 0.1
      (operating_hour)) ; 0.1 equivale a 2h

    (at 0.2
      (people_in_room bl1_sl1))

    (at 0.4
      (not (people_in_room bl1_sl1))) ; 0.3 equivale a 6h
  )

  (:goal
    (and
      (end_class_air bl1_sl1 bl1_sl1_ac1)
      (end_class_air bl1_sl1 bl1_sl1_ac2)
      (end_class_light bl1_sl1 bl1_sl1_light1)
      (end_class_light bl1_sl1 bl1_sl1_light2)
      (finish_class_time)
    )
  )
)