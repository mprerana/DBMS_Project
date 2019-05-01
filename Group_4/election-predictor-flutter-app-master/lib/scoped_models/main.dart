import 'package:scoped_model/scoped_model.dart';


import './connected_product.dart';


class MainModel extends Model with ConnectedModel, NewsModel,Eventmodel, UserModel, Utilitymodel, Analysismodel, Locationmodel {}