import axios from "axios";
import { APIKEY } from "../../Keys/GoogleApiKey";

import * as actionTypes from "./actionTypes";

export const authStart = () => {
  return {
    type: actionTypes.AUTH_START
  };
};

export const authSuccess = (token, userId) => {
  return {
    type: actionTypes.AUTH_SUCCESS,
    userId: userId,
    idToken: token
  };
};

export const authFailure = error => {
  return {
    type: actionTypes.AUTH_FAILURE,
    error: error
  };
};

export const logout = () => {
  localStorage.removeItem("token");
  localStorage.removeItem("expirationTime");
  localStorage.removeItem("userId");
  return {
    type: actionTypes.AUTH_LOGOUT
  };
};

export const authCheckTimeout = expirationTime => {
  return dispatch => {
    setTimeout(() => dispatch(logout()), expirationTime * 1000);
  };
};

export const auth = (email, password, isSignUp) => {
  return dispatch => {
    dispatch(authStart());
    const authData = {
      email,
      password,
      returnSecureToken: true
    };

    let url =
      "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=";

    if (isSignUp) {
      url =
        "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=";
    }


    axios.post(`${url}${APIKEY}`, authData)
      .then(response => {
        const expirationTime = new Date(
          new Date().getTime() + response.data.expiresIn * 1000
        );
        
        localStorage.setItem("token", response.data.idToken);
        localStorage.setItem("expirationTime", expirationTime);
        localStorage.setItem("userId", response.data.localId);
        dispatch(authSuccess(response.data.idToken, response.data.localId));
        dispatch(authCheckTimeout(response.data.expiresIn));
      })
      .catch(err => {
        console.log(err.response);
        dispatch(authFailure(err));
      });
  };
};

// This utility function automatically logs in user when you have a valid token
export const authCheckStatus = () => {
  return dispatch => {
    const token = localStorage.getItem("token");
    if (!token) {
      dispatch(logout());
    } else {
      const expirationTime = new Date(localStorage.getItem("expirationTime"));
      if (expirationTime > new Date()) {
        console.log(
          "time remaining is " + expirationTime.getTime() - new Date().getTime()
        );
        const userId = localStorage.getItem("userId");
        dispatch(authSuccess(token, userId));
        dispatch(
          authCheckTimeout(expirationTime.getTime() - new Date().getTime())
        );
      } else {
        dispatch(logout());
      }
    }
  };
};
