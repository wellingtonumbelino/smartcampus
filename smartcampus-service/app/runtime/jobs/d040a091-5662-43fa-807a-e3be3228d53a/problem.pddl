(define (problem smart_campus_problem_day_plan)
  (:domain smart_campus)

(:requirements :strips :typing :fluents :durative-actions :negative-preconditions :timed-initial-literals)

  (:objects
    sala_1 - room
    ac1 - air_conditioner
    l1 l2 l3 l4 - light
   )

  (:init
(= (occupancy sala_1) 0)

  (at 0.1 (operating_hour))
  (at 0.6 (not (operating_hour)))
   )

  (:goal (and
    (not (operating_hour))
  ))
)