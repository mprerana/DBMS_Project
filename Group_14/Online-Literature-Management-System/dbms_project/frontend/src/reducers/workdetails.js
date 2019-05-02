import {GET_WORKDETAILS, ADD_RATING, ADD_REVIEW} from "../actions/types";

const initialState = {
    workdetails: {}
};

export default function(state = initialState, action) {
    switch(action.type) {
        case GET_WORKDETAILS:
            return{
                ...state,
                workdetails : action.payload
            };
        case ADD_RATING:
              return {
                ...state
              };
        case ADD_REVIEW:
              return {
                ...state
              };
        default:
                return state;
    }
}