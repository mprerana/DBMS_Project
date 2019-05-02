import {GET_BLOG, DELETE_BLOG, ADD_BLOG} from '../actions/types.js';

const initialState = {
    Blog: []
};

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_BLOG:
            return {
                ...state,
                Blog: action.payload
            };
        
        case DELETE_BLOG:
            return {
                ...state,
                Blog: state.Blog.filter(Blog => Blog.id !== action.payload)
            };    

        case ADD_BLOG:
            return {
            ...state,
            Blog: [...state.Blog, action.payload]
        };        

        default:
            return state;
    }
}