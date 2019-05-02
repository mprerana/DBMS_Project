import axios from 'axios';
import { GET_PROFILE , EDIT_PROFILE} from "./types";
import { createMessage, returnErrors } from "./messages";
import  { tokenConfig} from "./auth";

//GET Profile
export const getProfile = (id) => (dispatch, getState) => {
    axios.get(`/user/${id}/`, tokenConfig(getState))
        .then(res => {
            dispatch({
                type: GET_PROFILE,
                payload: res.data
            });
        }).catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
};

//UPDATE Profile
export const editProfile = (id, updatedprofile) => (dispatch, getState) => {
    axios.put(`/userput/${id}/`, updatedprofile, tokenConfig(getState))
        .then(res => {
            dispatch({
                type: EDIT_PROFILE,
                payload: res.data
            });
        }).catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
};
