animationRange = (interval 0f 899f)
rotazionesbarra = eulerangles 0 90 0
foo = Cylinder name:"sbarra_1_1" radius:1.0 height:100.0 heightsegs:1 sides:16
rotate foo rotazionesbarra
foo.position = $hlp_origine_sbarre.position
foo = Cylinder name:"sbarra_1_2" radius:1.0 height:100.0 heightsegs:1 sides:16
rotate foo rotazionesbarra
foo.position = $hlp_origine_sbarre.position
foo = Cylinder name:"sbarra_1_3" radius:1.0 height:100.0 heightsegs:1 sides:16
rotate foo rotazionesbarra
foo.position = $hlp_origine_sbarre.position
foo = Cylinder name:"sbarra_1_4" radius:1.0 height:100.0 heightsegs:1 sides:16
rotate foo rotazionesbarra
foo.position = $hlp_origine_sbarre.position
foo = Cylinder name:"sbarra_1_5" radius:1.0 height:100.0 heightsegs:1 sides:16
rotate foo rotazionesbarra
foo.position = $hlp_origine_sbarre.position
foo = Cylinder name:"sbarra_1_6" radius:1.0 height:1.0 heightsegs:1 sides:16
rotate foo rotazionesbarra
foo.position = $hlp_origine_sbarre.position
foo.visibility = 0.0
foo = Cylinder name:"sbarra_1_7" radius:1.0 height:1.0 heightsegs:1 sides:16
rotate foo rotazionesbarra
foo.position = $hlp_origine_sbarre.position
foo.visibility = 0.0
foo = Cylinder name:"sbarra_1_8" radius:1.0 height:400.0 heightsegs:1 sides:16
rotate foo rotazionesbarra
foo.position = $hlp_origine_sbarre.position
foo = Cylinder name:"sbarra_1_9" radius:1.0 height:400.0 heightsegs:1 sides:16
rotate foo rotazionesbarra
foo.position = $hlp_origine_sbarre.position
foo = Cylinder name:"sbarra_1_10" radius:1.0 height:400.0 heightsegs:1 sides:16
rotate foo rotazionesbarra
foo.position = $hlp_origine_sbarre.position
maxOps.setDefaultTangentType #slow #slow
select $catenaria
at time 0 animate on move $ [0, 0, 0]
at time 49 animate on move $ [0, -20.0, 0]
select $sbarra_1_1
at time 50 animate on move $ [0, 0, 0]
maxOps.setDefaultTangentType #slow #linear
at time 74 animate on $.position = $hlp_sbarre_origine_catenaria.position
maxOps.setDefaultTangentType #slow #slow
select $catenaria
selectMore $sbarra_1_1
at time 75 animate on move $ [0, 0, 0]
at time 124 animate on move $ [0, -20.0, 0]
select $sbarra_1_2
at time 125 animate on move $ [0, 0, 0]
maxOps.setDefaultTangentType #slow #linear
at time 149 animate on $.position = $hlp_sbarre_origine_catenaria.position
maxOps.setDefaultTangentType #slow #slow
select $catenaria
selectMore $sbarra_1_1
selectMore $sbarra_1_2
at time 150 animate on move $ [0, 0, 0]
at time 199 animate on move $ [0, -20.0, 0]
select $sbarra_1_3
at time 200 animate on move $ [0, 0, 0]
maxOps.setDefaultTangentType #slow #linear
at time 224 animate on $.position = $hlp_sbarre_origine_catenaria.position
maxOps.setDefaultTangentType #slow #slow
select $catenaria
selectMore $sbarra_1_1
selectMore $sbarra_1_2
selectMore $sbarra_1_3
at time 225 animate on move $ [0, 0, 0]
at time 274 animate on move $ [0, -20.0, 0]
select $sbarra_1_4
at time 275 animate on move $ [0, 0, 0]
maxOps.setDefaultTangentType #slow #linear
at time 299 animate on $.position = $hlp_sbarre_origine_catenaria.position
maxOps.setDefaultTangentType #slow #slow
select $catenaria
selectMore $sbarra_1_1
selectMore $sbarra_1_2
selectMore $sbarra_1_3
selectMore $sbarra_1_4
at time 300 animate on move $ [0, 0, 0]
at time 349 animate on move $ [0, -20.0, 0]
select $sbarra_1_5
at time 350 animate on move $ [0, 0, 0]
maxOps.setDefaultTangentType #slow #linear
at time 374 animate on $.position = $hlp_sbarre_origine_catenaria.position
maxOps.setDefaultTangentType #slow #slow
select $catenaria
selectMore $sbarra_1_1
selectMore $sbarra_1_2
selectMore $sbarra_1_3
selectMore $sbarra_1_4
selectMore $sbarra_1_5
at time 375 animate on move $ [0, 0, 0]
at time 424 animate on move $ [0, -20.0, 0]
select $sbarra_1_6
at time 425 animate on move $ [0, 0, 0]
maxOps.setDefaultTangentType #slow #linear
at time 449 animate on $.position = $hlp_sbarre_origine_catenaria.position
maxOps.setDefaultTangentType #slow #slow
select $catenaria
selectMore $sbarra_1_1
selectMore $sbarra_1_2
selectMore $sbarra_1_3
selectMore $sbarra_1_4
selectMore $sbarra_1_5
selectMore $sbarra_1_6
at time 450 animate on move $ [0, 0, 0]
at time 499 animate on move $ [0, -20.0, 0]
select $sbarra_1_7
at time 500 animate on move $ [0, 0, 0]
maxOps.setDefaultTangentType #slow #linear
at time 524 animate on $.position = $hlp_sbarre_origine_catenaria.position
maxOps.setDefaultTangentType #slow #slow
select $catenaria
selectMore $sbarra_1_1
selectMore $sbarra_1_2
selectMore $sbarra_1_3
selectMore $sbarra_1_4
selectMore $sbarra_1_5
selectMore $sbarra_1_6
selectMore $sbarra_1_7
at time 525 animate on move $ [0, 0, 0]
at time 574 animate on move $ [0, -20.0, 0]
select $sbarra_1_8
at time 575 animate on move $ [0, 0, 0]
maxOps.setDefaultTangentType #slow #linear
at time 599 animate on $.position = $hlp_sbarre_origine_catenaria.position
maxOps.setDefaultTangentType #slow #slow
select $catenaria
selectMore $sbarra_1_1
selectMore $sbarra_1_2
selectMore $sbarra_1_3
selectMore $sbarra_1_4
selectMore $sbarra_1_5
selectMore $sbarra_1_6
selectMore $sbarra_1_7
selectMore $sbarra_1_8
at time 600 animate on move $ [0, 0, 0]
at time 649 animate on move $ [0, -20.0, 0]
select $sbarra_1_9
at time 650 animate on move $ [0, 0, 0]
maxOps.setDefaultTangentType #slow #linear
at time 674 animate on $.position = $hlp_sbarre_origine_catenaria.position
maxOps.setDefaultTangentType #slow #slow
select $catenaria
selectMore $sbarra_1_1
selectMore $sbarra_1_2
selectMore $sbarra_1_3
selectMore $sbarra_1_4
selectMore $sbarra_1_5
selectMore $sbarra_1_6
selectMore $sbarra_1_7
selectMore $sbarra_1_8
selectMore $sbarra_1_9
at time 675 animate on move $ [0, 0, 0]
at time 724 animate on move $ [0, -20.0, 0]
select $sbarra_1_10
at time 725 animate on move $ [0, 0, 0]
maxOps.setDefaultTangentType #slow #linear
at time 749 animate on $.position = $hlp_sbarre_origine_catenaria.position
select $catenaria
selectMore $sbarra_1*
maxOps.setDefaultTangentType #slow #slow
at time 750 animate on move $ [0, 0, 0]
at time 899 animate on move $ [0, -60.0, 0]
