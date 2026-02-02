(define (problem smart_campus_problem_day_plan)
  (:domain smart_campus)

(:requirements :strips :typing :fluents :durative-actions :negative-preconditions :timed-initial-literals)

  (:objects
    sala_1 - room
    ac1 - air_conditioner
    l1 l2 l3 l4 - light
   )

  (:init
    (= (work_time_duration) 0)

    (at 0.1 (operating_hour))

   (at 0.2 (people_in_room sala_1))

   (at 0.4 (not (people_in_room sala_1)))

  )

  (:goal (and
   (end_class_air sala_1 ac1)
   (end_class_light sala_1 l1)
   (end_class_light sala_1 l2)
   (end_class_light sala_1 l3)
   (end_class_light sala_1 l4)
      (finish_class_time))
  )
)