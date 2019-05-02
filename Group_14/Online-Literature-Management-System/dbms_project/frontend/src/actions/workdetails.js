import axios from "axios";
import {GET_WORKDETAILS, ADD_RATING, ADD_REVIEW} from "./types";
import { createMessage, returnErrors } from "./messages";
import  { tokenConfig } from "./auth";


// GET WORK DETAILS
export const  getworkdetails = (id) => (dispatch, getState) => {
    axios
        .get(`literature/workdetails/${id}/`, tokenConfig(getState))
        .then(res => {
           dispatch({
               type: GET_WORKDETAILS,
               payload: res.data
           });
        }).catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
};

//ADD RATING

export const addRating = (id,rating) => (dispatch, getState) => {
  axios
    .post(`opinion/ratingpost/${id}`, rating, tokenConfig(getState))
    .then(res => {
      dispatch({
        type: ADD_RATING,
        payload: rating
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

//ADD REVIEW
export const addReview = (id,review) => (dispatch, getState) => {
  axios
    .post(`opinion/reviewpost/${id}`, review, tokenConfig(getState))
    .then(res => {
      dispatch({
        type: ADD_REVIEW,
        payload: review
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};


