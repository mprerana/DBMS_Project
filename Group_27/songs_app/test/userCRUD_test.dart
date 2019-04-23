import 'package:test/test.dart';

void main() {
  test('Added sample test', () {
    String str = 'boo,fee,hee';
    expect(str.split(','), equals(['boo','fee','hee']));
  });
}