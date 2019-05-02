import axios from "axios";

import { GET_SHOW_DETAILS } from "./types";

import { createMessage, returnErrors } from "./messages";

//GET SHOW DETAILS

export const getShowDetails = showid => dispatch => {
  axios
    .get(`/movies/api/movies/specific_show/${showid}/`)
    .then(res => {
      dispatch({
        type: GET_SHOW_DETAILS,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
