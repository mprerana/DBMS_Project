import { combineReducers } from "redux";
import Users from "./Users";
import errors from "./errors";
import messages from "./messages";
import auth from "./auth";
import uploads from "./uploads";
import lists from "./lists";
import works from "./works";
import Profile from "./Profile";
import allworks from "./allworks";
import workdetails from "./workdetails";
import Followers from "./Followers";
import Following from "./Following";
import feed from "./feed";
import Blog from "./Blog";
import allblogs from "./allblogs";

export default combineReducers({
  Users,
  Followers,
  Following,
  errors,
  messages,
  auth,
  feed,
  lists,
  works,
  uploads,
  Profile,
  allworks,
  allblogs,
  workdetails,
  Blog
});
