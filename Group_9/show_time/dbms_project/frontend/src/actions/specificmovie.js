import axios from "axios";
import { GET_SPECIFICMOVIE, ADD_COMMENT } from "./types";
import { createMessage, returnErrors } from "./messages";
import { tokenConfig } from "./auth";

//GET SPECIFIC MOVIE

export const getSpecificMovie = id => dispatch => {
  axios
    .get(`/movies/api/movies/${id}/`)
    .then(res => {
      dispatch({
        type: GET_SPECIFICMOVIE,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

//ADD COMMENT

export const addComment = rating => (dispatch, getState) => {
  axios
    .post("/movies/api/ratingamovie/", rating, tokenConfig(getState))
    .then(res => {
      dispatch(
        createMessage({ movieReview: "you rated the movie successfully" })
      );
      dispatch({
        type: ADD_COMMENT,
        payload: rating
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
