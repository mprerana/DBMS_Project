import axios from "axios";
import { createMessage, returnErrors } from "./messages";

import { GET_MOVIES } from "./types";

//GET_MOVIES

export const getMovies = cityid => dispatch => {
  // var cityid = 1;

  // if (city == "hyderabad") {
  //   cityid = 1;
  // } else if (city == "mumbai") {
  //   cityid = 2;
  // } else if (city == "chennai") {
  //   cityid = 3;
  // }

  axios
    .get(`/movies/api/movies/city/${cityid}/`)
    .then(res => {
      dispatch(createMessage({ movieLoad: "movies loaded successfully" }));
      dispatch({
        type: GET_MOVIES,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
