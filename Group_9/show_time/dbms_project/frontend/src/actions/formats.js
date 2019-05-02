import axios from "axios";

import { GET_FORMATS } from "./types";

import { createMessage, returnErrors } from "./messages";

//GET GENRES

export const getFormats = () => dispatch => {
  axios
    .get("/movies/api/movies/format/")
    .then(res => {
      dispatch({
        type: GET_FORMATS,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
