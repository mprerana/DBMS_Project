import 'dart:async';
import 'dart:io';
import 'dart:typed_data';

import 'package:flutter/services.dart' show rootBundle;
import 'package:firebase_storage/firebase_storage.dart';

class StorageIO {
  /// creating a static instance of class
  static StorageIO _storageIO = StorageIO._createInstance();

  /// creates a instance of class
  StorageIO._createInstance();

  /// singleton instance of class
  factory StorageIO() => _storageIO;

  /// downloads image file into temp directory with location as file name and returns file location in temp directory
  Future<File> downloadImage(String location) async {
    print('Downloading image with location: $location');
    final Directory tempDir = Directory.systemTemp;
    final File file = File('${tempDir.path}/$location');

    final StorageReference ref = FirebaseStorage.instance.ref().child('Images/$location');
    final StorageFileDownloadTask task = ref.writeToFile(file);
    final int fileSize = (await task.future).totalByteCount;
    print('Downloaded image of size: $fileSize');

    return file;
  }

  /// downloads song file into temp directory with location as file name and returns file location in temp directory
  Future<File> downloadSong(String location) async {
    print('Downloading Song with location: $location');
    final Directory tempDir = Directory.systemTemp;
    final File file = File('${tempDir.path}/$location');

    final StorageReference ref = FirebaseStorage.instance.ref().child('Songs/$location');
    final StorageFileDownloadTask task = ref.writeToFile(file);
    final int fileSize = (await task.future).totalByteCount;
    print('Downloaded song of size: $fileSize');

    return file;
  }

  /// upload image file to firebase storage and returns downloaduri string
  Future<String> uploadImage(String fileName, String path, String folder) async {
    final ByteData bytes = await rootBundle.load(path);
    Directory tempDir = Directory.systemTemp;
    String filePath = '${tempDir.path}/$fileName}';

    File newFile = File(filePath);
    newFile = await newFile.writeAsBytes(bytes.buffer.asInt8List(), mode: FileMode.write);

    StorageReference ref = FirebaseStorage.instance.ref().child('Images/$folder/$fileName');
    StorageUploadTask task = ref.putFile(newFile);
    StorageTaskSnapshot snapshot = await task.onComplete;
    String downloadUri = await snapshot.ref.getDownloadURL();
    print('Uploaded image :$fileName and its url is :$downloadUri');
    return downloadUri;
  }

  /// upload song to firebase storage
  Future<String> uploadSong(String fileName, String path, String folder) async {
    final ByteData bytes = await rootBundle.load(path);
    Directory tempDir = Directory.systemTemp;
    String filePath = '${tempDir.path}/$fileName}';

    File newFile = File(filePath);
    newFile = await newFile.writeAsBytes(bytes.buffer.asInt8List(), mode: FileMode.write);

    StorageReference ref = FirebaseStorage.instance.ref().child('Songs/$folder/$fileName');
    StorageUploadTask task = ref.putFile(newFile);
    StorageTaskSnapshot snapshot = await task.onComplete;
    String downloadUri = await snapshot.ref.getDownloadURL();
    print('Uploaded Song :$fileName and its url is :$downloadUri');
    return downloadUri;
  }

  Future<String> getLink(String location) async {
    final StorageReference ref = FirebaseStorage.instance.ref().child('Songs/$location');
    String link = await ref.getDownloadURL();
    return link;
  }

  Future<String> getImageLink(String location) async {
    final StorageReference ref = FirebaseStorage.instance.ref().child('Images/$location');
    String link = await ref.getDownloadURL();
    return link;
  } 
}