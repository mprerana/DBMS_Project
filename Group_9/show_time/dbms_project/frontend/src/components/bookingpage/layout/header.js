import React, { Component, Fragment } from "react";
import { Link } from "react-router-dom";
import { getTheatres } from "../../../actions/theatre";

import { connect } from "react-redux";
import PropTypes from "prop-types";

export default props => {
  console.log(props.movie);
  const movie_name = props.movie.movie;
  const duration = props.movie.time_duration;
  const image = props.movie.image_source;
  const castslist = props.movie.castDetails;
  const genreslist = props.movie.genreDetails;

  const casts = castslist.map(cast => cast.castname);
  const genres = genreslist.map(genre => genre.genre);
  return (
    <div>
      <img
        className="image2"
        src={image}
        style={{
          border: "1px solid black",
          position: "absolute",
          width: "100%",
          height: "100%"
        }}
      />
      <h1>Genres</h1>
      <table className="table">
        <tbody>
          <tr>
            {genres.map(genre => (
              <td>
                <i>{genre}</i>
              </td>
            ))}
          </tr>
        </tbody>
      </table>
      <h1>Casts and Crews</h1>
      <table className="table">
        <tbody>
          <tr>
            {casts.map(cast => (
              <td>
                <i>{cast}</i>
              </td>
            ))}
          </tr>
        </tbody>
      </table>
    </div>
  );
};

// export class Header extends Component {
//   static propTypes = {
//     theatres: PropTypes.object.isRequired
//   };

//   render() {
//     console.log(this.props.theatres.movie);
//     return (
//       <div>
//         <h1>Hello World.</h1>
//       </div>
//     );
//   }
// }
// const mapStateToProps = state => ({
//   movie: state.theatres.theatres
// });

// export default connect(
//   mapStateToProps,
//   { getTheatres }
// )(Header);
