import 'dart:math';

import 'package:flutter/material.dart';

class Loader extends StatefulWidget {
  final double radius;
  final double dotradius;

  Loader({this.radius = 20.0,this.dotradius=5.0});

  @override
  State<StatefulWidget> createState() {
    return _LoaderState();
  }
}

class _LoaderState extends State<Loader> with SingleTickerProviderStateMixin {
  AnimationController animationController;
  Animation<double> animationRotation;
  Animation<double> animationRadiusIn;
  Animation<double> animationRadiusOut;

  double offsetRadius;
  double dotRadius;

  @override
  void initState() {
    
    offsetRadius = widget.radius;
    dotRadius = widget.dotradius;

    animationController = AnimationController(
        lowerBound: 0.0,
        upperBound: 1.0,
        duration: const Duration(milliseconds: 2000),
        vsync: this);
    
    animationRotation = Tween<double>(
      begin: 0.0,
      end: 1.0,
    ).animate(CurvedAnimation(
      parent: animationController,
      curve: Interval(0.0, 1.0, curve: Curves.linear)
    ));

    animationRadiusIn = Tween<double>(
      begin: 1.0,
      end: 0.0,
    ).animate(CurvedAnimation(
        parent: animationController,
        curve: Interval(0.65, 1.0, curve: Curves.elasticIn)));
    
    animationRadiusOut = Tween<double>(
      begin: 0.0,
      end: 1.0,
    ).animate(CurvedAnimation(
        parent: animationController,
        curve: Interval(0.0, 0.35, curve: Curves.elasticOut)));

    animationController.addListener(() {
      setState(() {
        if (animationController.value >= 0.75 && animationController.value <= 1.0)
          offsetRadius = widget.radius * animationRadiusIn.value; 
        else if (animationController.value >= 0.0 && animationController.value <= 0.25)
          offsetRadius = widget.radius * animationRadiusOut.value;
      });
    });

    animationController.repeat();
    super.initState();
  }

  @override
  void dispose() {
    animationController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 500.0,
      height: 500.0,
      child: Center(
        child: RotationTransition(
          turns: animationRotation,
          child: Stack(
          children: <Widget>[
            Dot(
              radius: offsetRadius,
              color: Colors.black45,
            ),
            Transform.translate(
              offset: Offset(this.offsetRadius * cos(pi / 4),
                  this.offsetRadius * sin(pi / 4)),
              child: Dot(
                radius: dotRadius,
                color: Colors.blueAccent,
              ),
            ),
            Transform.translate(
              offset: Offset(this.offsetRadius * cos(2 * pi / 4),
                  this.offsetRadius * sin(2 * pi / 4)),
              child: Dot(
                radius: dotRadius*2,
                color: Colors.redAccent,
              ),
            ),
            Transform.translate(
              offset: Offset(this.offsetRadius * cos(3 * pi / 4),
                  this.offsetRadius * sin(3 * pi / 4)),
              child: Dot(
                radius: dotRadius,
                color: Colors.blueAccent,
              ),
            ),
            Transform.translate(
              offset: Offset(this.offsetRadius * cos(4 * pi / 4),
                  this.offsetRadius * sin(4 * pi / 4)),
              child: Dot(
                radius: dotRadius*2,
                color: Colors.redAccent,
              ),
            ),
            Transform.translate(
              offset: Offset(this.offsetRadius * cos(5 * pi / 4),
                  this.offsetRadius * sin(5 * pi / 4)),
              child: Dot(
                radius: dotRadius,
                color: Colors.blueAccent,
              ),
            ),
            Transform.translate(
              offset: Offset(this.offsetRadius * cos(6 * pi / 4),
                  this.offsetRadius * sin(6 * pi / 4)),
              child: Dot(
                radius: dotRadius*2,
                color: Colors.redAccent,
              ),
            ),
            Transform.translate(
              offset: Offset(this.offsetRadius * cos(7 * pi / 4),
                  this.offsetRadius * sin(7 * pi / 4)),
              child: Dot(
                radius: dotRadius,
                color: Colors.blueAccent,
              ),
            ),
            Transform.translate(
              offset: Offset(this.offsetRadius * cos(8 * pi / 4),
                  this.offsetRadius * sin(8 * pi / 4)),
              child: Dot(
                radius: dotRadius*2,
                color: Colors.redAccent,
              ),
            ),
          ],
        ),
        ),
      ),
    );
  }
}

class Dot extends StatelessWidget {
  final double radius;
  final Color color;

  // constructor for this class
  Dot({this.radius, this.color});

  @override
  Widget build(BuildContext context) {
    return Center(
        child: Container(
      width: this.radius,
      height: this.radius,
      decoration: BoxDecoration(
        color: this.color,
        shape: BoxShape.circle,
      ),
    ));
  }
}


