import {GET_FOLLOWERS} from '../actions/types.js';

const initialState = {
    Followers: {}

};

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_FOLLOWERS:
            return {
                ...state,
                Followers: action.payload
            };

        default:
            return state;
    }
}
