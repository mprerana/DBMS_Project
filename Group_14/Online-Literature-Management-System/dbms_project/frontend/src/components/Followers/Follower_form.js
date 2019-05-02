// import React, {Component} from 'react'
// import {connect} from 'react-redux';
// import PropTypes from 'prop-types';
// import {addFollowers} from '../../actions/Followers';
//
//
// export class Follower_Form extends Component {
//     state = {
//         user: '',
//         follower: '',
//     };
//
//     static propTypes = {
//         addFollowers: PropTypes.func.isRequired
//     };
//
//     onChange = e => this.setState({[e.target.name]: e.target.value});
//
//     onSubmit = e => {
//         e.preventDefault();
//         const {user, follower} = this.state;
//         const Follower = {user, follower};
//         this.props.addFollowers(Follower);
//     };
//
//
//     render() {
//         const {user, follower} = this.state;
//         return (
//             <div className="card">
//
//                 <h1 className="card-header info-color white-text text-center py-4">
//                     Add a Follower
//                 </h1>
//
//                 <div className="card-body px-lg-5 pt-0">
//                     <form onSubmit={this.onSubmit} className="text-center" style={{"color": "#757575"}}>
//
//                         <div className="md-form">
//                             <input type="text"
//                                    className="form-control"
//                                    name="user"
//                                    onChange={this.onChange}
//                                    value={user}/>
//                             <label>User</label>
//                         </div>
//
//                         <div className="md-form">
//                             <input type="text"
//                                    className="form-control"
//                                    name="follower"
//                                    onChange={this.onChange}
//                                    value={follower}/>
//                             <label>Follower</label>
//                         </div>
//
//                         <button className="btn btn-outline-info btn-rounded btn-block my-4 waves-effect z-depth-0"
//                                 type="submit">ADD
//                         </button>
//
//                     </form>
//                 </div>
//             </div>
//         )
//     }
// }
//
// export default connect(null, {addFollowers})(Follower_Form);
