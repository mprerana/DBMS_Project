import { GET_FEED} from "../actions/types";

const initialState = {
    feed: []
};

export default function(state = initialState, action) {
    switch(action.type) {
        case GET_FEED:
            return{
                ...state,
                feed : action.payload
            };
             default:
                return state;
    }
}