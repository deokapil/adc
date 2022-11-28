import React from "react";
import {
  Box,
  AppBar,
  Toolbar,
  Typography,
  IconButton,
  Tooltip,
} from "@mui/material";
import {
  Brightness4,
  Brightness7,
  Home,
  LogoutOutlined,
} from "@mui/icons-material";
import LockRoundedIcon from "@mui/icons-material/LockRounded";
import { useValue } from "../context/ContextProvider";
import { logout } from "../actions/user";

const TopNav = ({ dark, setDark }) => {
  const {
    state: { currentUser },
    dispatch,
  } = useValue();
  const handleLogout = () => {
    logout(dispatch);
  };
  return (
    <AppBar position="fixed">
      <Toolbar>
        <Tooltip title="Go back to home page">
          <IconButton sx={{ mr: 1 }}>
            <Home />
          </IconButton>
        </Tooltip>
        <Typography variant="h6" noWrap component="div" sx={{ flexGrow: 1 }}>
          Dashboard
        </Typography>
        <Box sx={{ display: { md: "flex" } }}>
          <IconButton onClick={() => setDark(!dark)}>
            {dark ? <Brightness7 /> : <Brightness4 />}
          </IconButton>
          {!currentUser ? (
            <IconButton onClick={() => dispatch({ type: "OPEN_LOGIN" })}>
              <LockRoundedIcon />
            </IconButton>
          ) : (
            <IconButton onClick={handleLogout}>
              <LogoutOutlined />
            </IconButton>
          )}
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default TopNav;
