import React from "react";
import Button from "@material-ui/core/Button";
import Menu from "@material-ui/core/Menu";
import MenuItem from "@material-ui/core/MenuItem";
import IconButton from "@material-ui/core/IconButton";
import AccountCircle from "@material-ui/icons/AccountCircle";
import LoginPage from "./LoginPage";
import SignUpPage from './SignUpPage';

class AccountMenu extends React.Component {
  state = {
    anchorEl: null,
    open: false
  };

  handleClick = event => {
    this.setState({ anchorEl: event.currentTarget });
  };

  handleMenuClose = () => {
    this.setState({
      anchorEl: null,
      open:true
    });
  };
  loadLogin = () => {
    console.log("object");
    return <LoginPage open={true} />;
  };

  render() {
    const { anchorEl } = this.state;
    let login = null;
    /* if (this.state.open) {
        console.log(this.state.open)
        login = (<LoginPage buttonClicked='login' />)
    } */
    return (
      <div>
        <IconButton
          aria-owns={anchorEl ? "simple-menu" : undefined}
          aria-haspopup="true"
          onClick={this.handleClick}
        >
          <AccountCircle color="secondary" />
        </IconButton>
        <Menu
          id="simple-menu"
          anchorEl={anchorEl}
          open={Boolean(anchorEl)}
          onClose={this.handleMenuClose}
        >
          {/* <LoginPage
            buttonClicked="login"
            handleMenuClose={this.handleMenuClose}
          /> */}
          <LoginPage handleMenuClose={this.handleMenuClose} buttonClicked='login'/>
          {/* <MenuItem onClick={this.handleMenuClose}>Login</MenuItem> */}
          {/* <MenuItem onClick={this.handleMenuClose}>Sign Up</MenuItem> */}
          <SignUpPage handleMenuClose={this.handleMenuClose} buttonClicked='sign up' />
        </Menu>
        {/* {this.state.open?(<LoginPage buttonClicked='login'/>):null} */}
      </div>
    );
  }
}

export default AccountMenu;
