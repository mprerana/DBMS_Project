import  React, {Component} from 'react';
import { Link } from "react-router-dom";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { logout } from '../../actions/auth';

export class Header extends Component {

    static  propTypes = {
        auth: PropTypes.object.isRequired,
        logout: PropTypes.func.isRequired
    };

    render() {
        const { isAuthenticated, user } = this.props.auth;

        const authLinks = (
                     <ul className="navbar-nav ml-auto mt-2 mt-lg-0">
                         <li className="nav-item">
                             <Link to="/profile" className="nav-link">
                            <strong>
                                { user ? `Welcome ${user.username}` : ""}
                            </strong>
                             </Link>
                         </li>
                         <li className="nav-item">
                             <Link to="/follower" className="nav-link">
                                 Followers
                             </Link>
                         </li>
                         <li className="nav-item">
                             <Link to="/literature" className="nav-link">
                                 ReadingList
                             </Link>
                         </li>
                         <li className="nav-item">
                             <Link to="/upload" className="nav-link">
                                 Upload Book
                             </Link>
                         </li>
                         <li className="nav-item">
                             <button
                                 onClick={this.props.logout}
                                 className="nav-link btn btn-info btn-sm text-light">
                                 Logout
                             </button>
                         </li>
                     </ul>

        );

        const guestLinks = (
                    <ul className="navbar-nav ml-auto mt-2 mt-lg-0">
                         <li className="nav-item">
                             <Link to="/register" className="nav-link">
                                 Register
                             </Link>
                         </li>
                         <li className="nav-item">
                            <Link to="/login" className="nav-link">
                                 Login
                             </Link>
                         </li>
                     </ul>
        );

        return(
         <div>
             <nav className="navbar navbar-expand-sm navbar-dark bg-dark">
                 <a className="navbar-brand" href="#">OWL</a>
                 <button className="navbar-toggler" type="button" data-toggle="collapse"
                         data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false"
                         aria-label="Toggle navigation">
                     <span className="navbar-toggler-icon">whatt</span>
                 </button>
                 <div className="collapse navbar-collapse" id="navbarNavDropdown">
                     <ul className="navbar-nav">
                         <li className="nav-item active">
                             <a className="nav-link" href="#">Home <span className="sr-only">(current)</span></a>
                         </li>
                     </ul>

                 </div>
                 {isAuthenticated ? authLinks : guestLinks}
             </nav>
         </div>
        )
    }
}

const mapStateToProps = state => ({
    auth: state.auth
});

export default connect(mapStateToProps, { logout })(Header);