(require 2htdp/image)
(overlay (circle 10 "solid" "red")
         (circle 20 "solid" "white")
         (circle 30 "solid" "red"))


# how to define a function
(define (bulb c)
  (circle 40 "solid" c))

(above (bulb "red")
       (bulb "yellow")
       (bulb "green"))

(and (> (image-height I1) (image-height I2))
     (< (image-width I1) (image-width I2)))