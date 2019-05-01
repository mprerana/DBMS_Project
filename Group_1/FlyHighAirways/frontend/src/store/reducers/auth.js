import * as actionTypes from '../actions/actionTypes';

const initialState = {
    token: null,
    userId: null,
    error: null,
    loading: false
};

const reducer = (state = initialState, action) => {
    switch(action.type) {
        case actionTypes.AUTH_START:
            return {
                ...state,
                loading: true
            }
        case actionTypes.AUTH_FAILURE:
            return {
                ...state,
                error: action.error,
                loading: false
            }
        case actionTypes.AUTH_SUCCESS:
            return {
                ...state,
                userId: action.userId,
                token: action.idToken,
                loading: false,
                error:null
            }
        case actionTypes.AUTH_LOGOUT:
            return {
                ...state,
                token: null,
                userId: null,
            }

        default:
            return state;
    }   
};

export default reducer;