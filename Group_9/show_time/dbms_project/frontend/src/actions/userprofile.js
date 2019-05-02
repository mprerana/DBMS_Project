import axios from "axios";
import { GET_USERPROFILE, EDIT_USERPROFILE } from "./types";
import { createMessage, returnErrors } from "./messages";
import { tokenConfig } from "./auth";

// GET USERPROFILE

export const getUserProfile = id => (dispatch, getState) => {
  axios
    .get(`/accounts/api/auth/getuserprofile/${id}/`, tokenConfig(getState))
    .then(res => {
      dispatch({
        type: GET_USERPROFILE,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

// UPDATE USER PROFILE

export const UpdateUserProfile = (id, updatedprofile) => (
  dispatch,
  getState
) => {
  axios
    .put(
      `/accounts/api/auth/putuserprofile/${id}/`,
      updatedprofile,
      tokenConfig(getState)
    )
    .then(res => {
      dispatch({
        type: EDIT_USERPROFILE,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
