import React, { Component } from "react";
import { Menu, Icon, Button, Drawer } from "antd";
import classes from "./Header.module.css";
import { NavLink } from "react-router-dom";

import { withRouter } from "react-router-dom";

import { connect } from "react-redux";
import { logout } from "../../store/actions/index";

const SubMenu = Menu.SubMenu;
const MenuItemGroup = Menu.ItemGroup;

class Navbar extends Component {
  state = {
    current: "mail",
    visible: false
  };

  documentStyle = document.documentElement.style;
  initalNavbarBackground =
    "linear-gradient(to bottom, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0))";
  scrolledNavbarBackground = "white";

  handleScroll = () => {
    if (window.scrollY === 0) {
      this.documentStyle.setProperty(
        "--navbar-background-color",
        this.initalNavbarBackground
      );
    } else {
      this.documentStyle.setProperty(
        "--navbar-background-color",
        this.scrolledNavbarBackground
      );
    }
  };

  componentDidMount() {
    window.addEventListener("scroll", this.handleScroll);
  }

  componentWillUnmount() {
    window.removeEventListener("scroll", this.handleScroll);
  }

  showDrawer = () => {
    this.setState({
      visible: true
    });
  };

  onClose = () => {
    this.setState({
      visible: false
    });
  };

  render() {
    return (
      <nav className={classes.menuBar} style={{ transition: "1s" }}>
        <div className="container">
          <div className={classes.logo}>
            <NavLink to="/">FlyHigh</NavLink>
          </div>

          <div className={classes.menuCon}>
            <div className={classes.leftMenu}>
              <Menu
                theme="light"
                mode="horizontal"
                overflowedIndicator={<Icon type="bars" />}
                style={{
                  lineHeight: "66px",
                  borderBottom: "0",
                  backgroundColor: "transparent"
                }}
              >
                <Menu.Item key="2">
                    <NavLink className="nav-link" to="/flights">
                      Flights
                    </NavLink>
                </Menu.Item>

                <Menu.Item key="dashboard">
                  {
                    this.props.isAuth ? 
                    <NavLink to="/dashboard">Dashboard</NavLink> :
                    null
                  }
                </Menu.Item>
                <Menu.Item key="alipay">
                  {
                    !this.props.isAuth ? 
                    <NavLink to="/authenticate">Login</NavLink> :
                    <NavLink className="nav-link" onClick={this.props.onLogout} to="/">LogOut</NavLink>
                  }
                </Menu.Item>
              </Menu>
            </div>
            <div className={classes.rightMenu}>
              <Menu
                theme="light"
                mode="horizontal"
                overflowedIndicator={<Icon type="bars" />}
                style={{
                  lineHeight: "66px",
                  borderBottom: "0",
                  backgroundColor: "transparent"
                }}
              >
                
              </Menu>
            </div>
            <Button
              className={classes.barsMenu}
              type="primary"
              onClick={this.showDrawer}
            >
              <span className={classes.barsBtn} />
            </Button>
            <Drawer
              title="side bar"
              placement="right"
              closable={false}
              onClose={this.onClose}
              visible={this.state.visible}
            >
              <Menu>
                <Menu.Item key="1">nav 1</Menu.Item>
                <Menu.Item key="2">nav 2</Menu.Item>
                <Menu.Item key="3">nav 3</Menu.Item>

                <Menu.Item key="mail">
                  <a href="/">Home</a>
                </Menu.Item>
                <SubMenu title={<span>Blogs</span>}>
                  <MenuItemGroup title="Item 1">
                    <Menu.Item key="setting:1">Option 1</Menu.Item>
                    <Menu.Item key="setting:2">Option 2</Menu.Item>
                  </MenuItemGroup>
                  <MenuItemGroup title="Item 2">
                    <Menu.Item key="setting:3">Option 3</Menu.Item>
                    <Menu.Item key="setting:4">Option 4</Menu.Item>
                  </MenuItemGroup>
                </SubMenu>
                <Menu.Item key="alipay">
                  <a href="/">Contact Us</a>
                </Menu.Item>

                <SubMenu
                  style={{ float: "right" }}
                  title={
                    <span>
                      <Icon type="setting" />
                      Navigation Three - Submenu
                    </span>
                  }
                >
                  <MenuItemGroup title="Item 1">
                    <Menu.Item key="setting:1">Option 1</Menu.Item>
                    <Menu.Item key="setting:2">Option 2</Menu.Item>
                  </MenuItemGroup>
                  <MenuItemGroup title="Item 2">
                    <Menu.Item key="setting:3">Option 3</Menu.Item>
                    <Menu.Item key="setting:4">Option 4</Menu.Item>
                  </MenuItemGroup>
                </SubMenu>
              </Menu>
            </Drawer>
          </div>
        </div>
      </nav>
    );
  }
}

const mapDispatchToProps = dispatch => {
    return {
        onLogout: () => dispatch(logout())
    };
};

export default withRouter(
  connect(
    null,
    mapDispatchToProps
  )(Navbar)
);
