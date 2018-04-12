# Proyecto 4: Graficas por computadora 
> Puerto de Barcos en donde se encuentra un barco (que se traslada, rota y escala) y carga diferentes cajas, una grua, olas...etc.

> Universidad del Valle de Guatemala 
> Graficas por computadora 
> Primer Ciclo año 2018  






## Installation

Open in FireFox con WebGl habilitado

```sh
index.html
```

## Controles
  Se describira acontinuacion los siguientes objetos
## Submarino
mover con mouse ya sea la posicion, grados o tamano. 
Se muestran a continuacion los siguientes Keyboards:
```sh
    W: translate
    E: rotate
    R: Sheer
```
Para poder transportar cajas se describen las siguientes instrucciones
```sh
    SHIFT + click: jalar caja a barco
    double click o clik izquierdo: sacar caja
```
## Animaciones
  Las animaciones fueron creadas directamente desde WebGl con la grua donde se realizo un parseo desde:
  https://github.com/rdiankov/collada_robots
  En donde se creo un Collada Controler y se realizo la info como:
  ```sh
    function setupTween() {

				var duration = THREE.Math.randInt( 1000, 5000 );

				var target = {};

				for ( var prop in kinematics.joints ) {

					if ( kinematics.joints.hasOwnProperty( prop ) ) {

						if ( ! kinematics.joints[ prop ].static ) {

							var joint = kinematics.joints[ prop ];

							var old = tweenParameters[ prop ];

							var position = old ? old : joint.zeroPosition;

							tweenParameters[ prop ] = position;

							target[ prop ] = THREE.Math.randInt( joint.limits.min, joint.limits.max )

						}

					}

				}

				kinematicsTween = new TWEEN.Tween( tweenParameters ).to( target, duration ).easing( TWEEN.Easing.Quadratic.Out );

				kinematicsTween.onUpdate( function() {

					for ( var prop in kinematics.joints ) {

						if ( kinematics.joints.hasOwnProperty( prop ) ) {

							if ( ! kinematics.joints[ prop ].static ) {

								kinematics.setJointValue( prop, this[ prop ] );

							}

						}

					}

				} );

				kinematicsTween.start();

				setTimeout( setupTween, duration );

			}

			function onWindowResize() {

				camera.aspect = window.innerWidth / window.innerHeight;
				camera.updateProjectionMatrix();

				renderer.setSize( window.innerWidth, window.innerHeight );

			}

```
## Video del proyecto
  accede a la pagina:

## Members

* Ana Lucía Diaz Leppe  

## NO FUNCIONA
  Si el programa no te esta corriendo es porque no lo estas abriendo de la manera correcta. El programa se corrio en FireFox por lo que es necesario tener habilitado Webgl en Firefox. Si no te funciona prueba el siguiente video:
  https://www.youtube.com/watch?v=IqdMzHSSIZ0
## AUN NO FUNCIONA: REALIZA UNA CONSULTA
  correo: dia151378@uvg.edu.gt



<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[wiki]: https://github.com/yourname/yourproject/wiki
