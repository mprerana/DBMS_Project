import axios from "axios";
import { returnErrors } from "./messages";

import {
  USER_LOADED,
  USER_LOADING,
  AUTH_ERROR,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  LOGOUT_SUCCESS,
  REGISTER_SUCCESS,
  REGISTER_FAIL
} from "./types";

// CHECK    TOKEN & LOAD USER

export const loadUser = () => (dispatch, getState) => {
  //User Loading

  dispatch({ type: USER_LOADING });

  axios
    .get("/accounts/api/auth/loggedinuser", tokenConfig(getState))
    .then(res => {
      dispatch({
        type: USER_LOADED,
        payload: res.data
      });
    })
    .catch(err => {
      dispatch(returnErrors(err.response.data, err.response.status));
      dispatch({
        type: AUTH_ERROR
      });
    });
};

//LOGIN USER

export const login = (username, password) => dispatch => {
  //headers

  const config = {
    headers: {
      "Content-Type": "application/json"
    }
  };

  //Request Body
  const body = JSON.stringify({ username, password });

  axios
    .post("/accounts/api/auth/login", body, config)
    .then(res => {
      dispatch({
        type: LOGIN_SUCCESS,
        payload: res.data
      });
    })
    .catch(err => {
      dispatch(returnErrors(err.response.data, err.response.status));
      dispatch({
        type: LOGIN_FAIL
      });
    });
};

//REGISTER USER

export const register = ({
  username,
  password,
  email,
  first_name,
  last_name,
  dob,
  city,
  phone,
  image
}) => dispatch => {
  //headers

  const config = {
    headers: {
      "Content-Type": "application/json"
    }
  };

  //Request Body

  const user = {
    username,
    first_name,
    last_name,
    email,
    password
  };
  const body = JSON.stringify({
    user,
    dob,
    city,
    phone,
    image
  });

  axios
    .post("/accounts/api/getuserregister/", body, config)
    .then(res => {
      dispatch({
        type: REGISTER_SUCCESS,
        payload: res.data
      });
    })
    .catch(err => {
      dispatch(returnErrors(err.response.data, err.response.status));
      dispatch({
        type: REGISTER_FAIL
      });
    });
};

// LOGOUT USER

export const logout = () => (dispatch, getState) => {
  axios
    .post("/accounts/api/auth/logout", null, tokenConfig(getState))
    .then(res => {
      dispatch({
        type: LOGOUT_SUCCESS
      });
    })
    .catch(err => {
      dispatch(returnErrors(err.response.data, err.response.status));
    });
};

//SetUp config with token -- helper function

export const tokenConfig = getState => {
  //get token from the state
  const token = getState().auth.token;

  //headers

  const config = {
    headers: {
      "Content-Type": "application/json"
    }
  };

  // If token, add to headers config

  if (token) {
    config.headers["Authorization"] = `Token ${token}`;
  }

  return config;
};
