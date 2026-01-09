(define (domain smart_campus)
  (:requirements :strips :typing :fluents :durative-actions :negative-preconditions :timed-initial-literals)

  (:types
    room air-conditioner light
  )

  (:predicates
    (operating_hour)
    (start_class)
    (end_class_air ?r - room ?a - air-conditioner)
    (end_class_light ?r - room ?l - light)
    (air_conditioner_on ?r - room ?a - air-conditioner)
    (light_on ?r - room ?l - light)
  )

  (:functions
    (occupancy ?r - room)
  )

  (:durative-action start_campus_operating
    :parameters ()
    :duration (= ?duration 0)
    :condition (and
      (at start (operating_hour))
      (at start (not (start_class)))
      (over all (operating_hour))
    )
    :effect (and
      (at start (start_class))
    )
  )

  (:durative-action turn_on_air_conditioner_during_class
    :parameters (?r - room ?a - air-conditioner)
    :duration (= ?duration 0.2)
    :condition (and
      (at start (start_class))
      (at start (not (air_conditioner_on ?r ?a)))
      (at start (> (occupancy ?r) 0))
      (at start (operating_hour))
      (over all (operating_hour))
    )
    :effect (and
      (at start (air_conditioner_on ?r ?a))
      ; (at end (not (air_conditioner_on ?r ?a)))
      (at end (end_class_air ?r ?a))
      (at end (assign (occupancy ?r) 0))
    )
  )

  (:durative-action turn_on_light_during_class
    :parameters (?r - room ?l - light)
    :duration (= ?duration 0.2)
    :condition (and
      (at start (start_class))
      (at start (not (light_on ?r ?l)))
      (at start (> (occupancy ?r) 0))
      (at start (operating_hour))
      (over all (operating_hour))
    )
    :effect (and
      (at start (light_on ?r ?l))
      ; (at end (not (light_on ?r ?l)))
      (at end (end_class_light ?r ?l))
      (at end (assign (occupancy ?r) 0))
    )
  )

  (:durative-action turn_off_air_conditioner_when_occupancy_zero
    :parameters (?r - room ?a - air-conditioner)
    :duration (= ?duration 0)
    :condition (and
      (at start (start_class))
      (at start (= (occupancy ?r) 0))
      (at start (air_conditioner_on ?r ?a))
      (at start (operating_hour))
    )
    :effect (and
      (at start (not (air_conditioner_on ?r ?a)))
    )
  )

  (:durative-action turn_off_light_when_occupancy_zero
    :parameters (?r - room ?l - light)
    :duration (= ?duration 0)
    :condition (and
      (at start (start_class))
      (at start (= (occupancy ?r) 0))
      (at start (light_on ?r ?l))
      (at start (operating_hour))
    )
    :effect (and
      (at start (not (light_on ?r ?l)))
    )
  )
)