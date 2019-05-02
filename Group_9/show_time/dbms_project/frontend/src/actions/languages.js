import axios from "axios";

import { GET_LANGUAGES } from "./types";

import { createMessage, returnErrors } from "./messages";

//GET GENRES

export const getLanguages = () => dispatch => {
  axios
    .get("/movies/api/movies/language/")
    .then(res => {
      dispatch({
        type: GET_LANGUAGES,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
