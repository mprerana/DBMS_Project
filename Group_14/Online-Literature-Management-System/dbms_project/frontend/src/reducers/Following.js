import {DELETE_FOLLOWING, GET_FOLLOWING, ADD_FOLLOWING} from '../actions/types.js';

const initialState = {
    Following: {}
};

export default function (state = initialState, action) {
    switch (action.type) {

        case GET_FOLLOWING:
            return {
                ...state,
                Following: action.payload
            };

        case DELETE_FOLLOWING:
            return {
                ...state,
               // Following: state.Following.filter(Follower => Follower.id !== action.payload)
            };
        case ADD_FOLLOWING:
            return {
                ...state,
                //Following: [...state.Following, action.payload]
            };
        default:
            return state;
    }

}
