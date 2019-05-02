import axios from "axios";

import { GET_SEATS_BOOKED, IN_BOOKING } from "./types";

import { createMessage, returnErrors } from "./messages";

//GET SEATS BOOKED

export const getSeatsBooked = showid => dispatch => {
  axios
    .get(`/movies/api/movies/bookedseats/${showid}/`)
    .then(res => {
      dispatch({
        type: GET_SEATS_BOOKED,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

export const bookaSeat = seat => dispatch => {
  axios
    .post(`/movies/api/movies/yettobook/`, seat)
    .then(res => {
      dispatch({
        type: IN_BOOKING,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
