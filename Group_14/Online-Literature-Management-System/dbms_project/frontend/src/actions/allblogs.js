import axios from "axios";
import { GET_ALLBLOGS, GET_ERRORS } from "./types";
import { createMessage, returnErrors } from "./messages";
import { tokenConfig } from "./auth";

// GET ALL BLOGS
export const getallblogs = (id) => (dispatch, getState) => {
  axios
    .get(`literature/blogs/${id}/`, tokenConfig(getState))
    .then(res => {
      dispatch({
        type: GET_ALLBLOGS,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
