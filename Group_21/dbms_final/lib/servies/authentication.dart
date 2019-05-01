import 'dart:async';

import 'package:firebase_auth/firebase_auth.dart';

class BaseAuth {
  static BaseAuth _baseAuth;
  static FirebaseAuth _firebaseAuth;

  BaseAuth._createInstance();

  factory BaseAuth() {
    if (_baseAuth == null) {
      _baseAuth = BaseAuth._createInstance();
    }
    return _baseAuth;
  }

  FirebaseAuth get firebaseAuth {
    if(_firebaseAuth == null) {
      _firebaseAuth = FirebaseAuth.instance;
    }
    return _firebaseAuth;
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

}
