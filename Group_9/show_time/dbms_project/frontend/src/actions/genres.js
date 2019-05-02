import axios from "axios";

import { GET_GENRES } from "./types";

import { createMessage, returnErrors } from "./messages";

//GET GENRES

export const getGenres = () => dispatch => {
  axios
    .get("/movies/api/movies/genre/")
    .then(res => {
      dispatch({
        type: GET_GENRES,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
