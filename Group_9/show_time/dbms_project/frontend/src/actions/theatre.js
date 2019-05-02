import axios from "axios";
import { GET_THEATRE_LIST } from "./types";

//Get Theatre Lists

export const getTheatres = (movie_id, city_id) => dispatch => {
  axios
    .get(`/movies/api/movies/city_theatre/${movie_id}/${city_id}/`)
    .then(res => {
      console.log(res.data);
      dispatch({
        type: GET_THEATRE_LIST,
        payload: res.data
      });
    })
    .catch(err => console.log(err));
};
