import axios from 'axios';
import { GET_USERS } from "./types";
import { createMessage, returnErrors } from "./messages";
import  { tokenConfig} from "./auth";

//GET USERS
export const getUsers = () => (dispatch, getState) => {
    axios.get("/appuser/", tokenConfig(getState))
        .then(res => {
            dispatch({
                type: GET_USERS,
                payload: res.data
            });
        }).catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
};
