import 'package:flutter/material.dart';

class Product {
  final String product_id;
  final String title;
  final String description;
  final double price;
  final String image;
  final bool isFavorite;
  final String id;
  final String email;

  Product({
    @required this.product_id,
    @required this.title,
    @required this.description,
    @required this.image,
    @required this.price,
    @required this.email,
    @required this.id,
    this.isFavorite = false,
  });
}
