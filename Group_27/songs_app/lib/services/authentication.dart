import 'dart:async';

import 'package:firebase_auth/firebase_auth.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class BaseAuth {
  static BaseAuth _baseAuth;
  static FirebaseAuth _firebaseAuth = FirebaseAuth.instance;
  static Firestore _db = Firestore.instance;

  BaseAuth._createInstance();

  factory BaseAuth() {
    if (_baseAuth == null) {
      _baseAuth = BaseAuth._createInstance();
    }
    return _baseAuth;
  }

  FirebaseAuth get firebaseAuth {
    return _firebaseAuth;
  }

  Firestore get firestoreDB {
    return _db;
  }

  Future<String> login(String email, String password) async {
      FirebaseUser user = await firebaseAuth.signInWithEmailAndPassword(
        email: email, password: password);
      return user.uid;
  }

  Future<String> signUp(String email, String password) async {
    FirebaseUser user = await firebaseAuth.createUserWithEmailAndPassword(
        email: email, password: password);
    return user.uid;
  }

  Future<FirebaseUser> getCurrentUser() async {
    FirebaseUser user = await firebaseAuth.currentUser();
    return user;
  }

  Future<void> signOut() async {
    return firebaseAuth.signOut();
  }

  Future<void> sendEmailVerification() async {
    FirebaseUser user = await firebaseAuth.currentUser();
    user.sendEmailVerification();
  }

  Future<bool> isEmailVerified() async {
    FirebaseUser user = await firebaseAuth.currentUser();
    return user.isEmailVerified;
  }

  Future<void> resetPassword(String email) async {
    await firebaseAuth.sendPasswordResetEmail(email: email);
  }
}
