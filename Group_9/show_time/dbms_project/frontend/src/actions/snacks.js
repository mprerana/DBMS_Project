import axios from "axios";

import { GET_SNACKS } from "./types";

import { createMessage, returnErrors } from "./messages";

//GET SNACKS

export const getSnacks = () => dispatch => {
  axios
    .get("/movies/api/movies/snacks/")
    .then(res => {
      dispatch({
        type: GET_SNACKS,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
