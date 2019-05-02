import { combineReducers } from "redux";
import moviesReducer from "./moviesReducer";
import specificmovieReducer from "./specificmovieReducer.js";
import errors from "./errors";
import messages from "./messages";
import auth from "./auth";
import userprofile from "./userprofile";
import genres from "./genres";
import languages from "./languages";
import formats from "./formats";
import snacks from "./snacks";
import theatres from "./theatre";
import ticketbookinghistory from "./tickethistory";
import cities from "./cities";
import showdetails from "./showdetails";
import seatsbooked from "./seatsbooked";
import selectedseats from "./selectedseats";

export default combineReducers({
  movies: moviesReducer,
  errors: errors,
  messages: messages,
  auth: auth,
  specificmovie: specificmovieReducer,
  userprofile: userprofile,
  genres: genres,
  languages: languages,
  formats: formats,
  snacks: snacks,
  theatres: theatres,
  ticketbookinghistory: ticketbookinghistory,
  cities: cities,
  showdetails: showdetails,
  seatsbooked: seatsbooked,
  selectedseats: selectedseats
});
