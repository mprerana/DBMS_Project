import React from "react";
import PropTypes from "prop-types";
import { withStyles, MuiThemeProvider } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import IconButton from "@material-ui/core/IconButton";
import red from "@material-ui/core/colors/red";
/* eslint-disable react/jsx-handler-names */
import Menu from "@material-ui/core/Menu";
import MenuItem from "@material-ui/core/MenuItem";
import PopupState, {
  bindTrigger,
  bindMenu
} from "material-ui-popup-state/index";
import List from "@material-ui/core/List";
import Divider from "@material-ui/core/Divider";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import InboxIcon from "@material-ui/icons/MoveToInbox";
import MailIcon from "@material-ui/icons/Mail";
import Home from "@material-ui/icons/Home";
import ContactSupport from "@material-ui/icons/ContactSupport";
import { createMuiTheme } from "@material-ui/core/styles";
import purple from "@material-ui/core/colors/purple";
import { blue, grey } from "@material-ui/core/colors";
import InputBase from "@material-ui/core/InputBase";
import SearchIcon from "@material-ui/icons/Search";
import { fade } from "@material-ui/core/styles/colorManipulator";
import Drawer from "./Drawer";
import LoginPage from "./LoginPage";
import AccountMenu from "./AccountMenu";
import Logo from "./images/LogoBlackTransparent.png";

// TODO: add popover to buttons

const theme = createMuiTheme({
  palette: {
    primary: {
      main: "#fff"
    },
    secondary: {
      main: "#212121"
    }
  },
  shadows: ["none"]
});

const styles = {
  root: {
    flexGrow: 1,
    padding: "35px",
    backgroundColor: "transparent"
  },
  grow: {
    flexGrow: 1
  },
  logo: {
    position: "relative",
    paddingLeft: "0%",
    paddingRight: "90%"
  },
  menuButton: {
    position: "relative",
    marginLeft: -12,
    marginRight: 20
  },
  accountButton: {
    marginLeft: 0,
    marginRight: 0
  },
  search: {
    position: "relative",
    borderRadius: theme.shape.borderRadius,
    backgroundColor: fade(theme.palette.common.white, 0.15),
    "&:hover": {
      backgroundColor: fade(theme.palette.common.white, 0.25)
    },
    marginLeft: 0,
    width: "100%",
    [theme.breakpoints.up("sm")]: {
      marginLeft: theme.spacing.unit,
      width: "auto"
    }
  },
  searchIcon: {
    width: theme.spacing.unit * 9,
    height: "100%",
    color: "#fff",
    position: "absolute",
    pointerEvents: "none",
    display: "flex",
    alignItems: "center",
    justifyContent: "center"
  },
  inputRoot: {
    color: "inherit",
    width: "100%"
  },
  inputInput: {
    color: "secondary",
    paddingTop: theme.spacing.unit,
    paddingRight: theme.spacing.unit,
    paddingBottom: theme.spacing.unit,
    paddingLeft: theme.spacing.unit * 10,
    transition: theme.transitions.create("width"),
    width: "100%",
    [theme.breakpoints.up("sm")]: {
      width: 120,
      "&:focus": {
        width: 200
      }
    }
  }
};

const loadLoginPage = () => {
  console.log("loadLoginPage run");
  return <LoginPage LoginButtonClicked={true} />;
};

function ButtonAppBar(props) {
  const { classes } = props;
  let clicked = false;
  if (clicked) {
    console.log("clicked");
  }
  return (
    <div className={classes.root}>
      <MuiThemeProvider theme={theme}>
        <AppBar position="fixed">
          <Toolbar>
            <Drawer />
            <div id="navLogo">
              <a href="/">
                <img
                  src={Logo}
                  style={{
                    marginLeft: "-10px",
                    width: "50px",
                    height: "auto"
                  }}
                />
              </a>
            </div>
            <div
              id="pagetitle"
              style={{
                paddingLeft: "20px",
                textAlign: "center"
              }}
            />
            {/* <Typography variant="h6" color="inherit" className={classes.grow}>
              <span className={classes.logo}> Quizapp!</span>
            </Typography> */}
            <div className={classes.grow} />
            <div className={classes.search}>
              <div className={classes.searchIcon}>
                <SearchIcon color="secondary" />
              </div>
              <InputBase
                placeholder="Search…"
                color="secondary"
                classes={{
                  root: classes.inputRoot,
                  input: classes.inputInput
                }}
              />
            </div>
            <IconButton
              className=""
              color="secondary"
              aria-label="Home"
              href="/profile"
            >
              <Home />
            </IconButton>
            <IconButton
              className=""
              color="secondary"
              aria-label="ContactSupport"
            >
              <ContactSupport />
            </IconButton>
            <AccountMenu />
          </Toolbar>
        </AppBar>
      </MuiThemeProvider>
    </div>
  );
}

ButtonAppBar.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(ButtonAppBar);
