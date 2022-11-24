import { Close, Send } from "@mui/icons-material";
import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
  IconButton,
  TextField,
  Typography,
} from "@mui/material";
import { useEffect, useRef, useState } from "react";
import { login } from "../../actions/user";
import { useValue } from "../../context/ContextProvider";
import PasswordField from "./PasswordField";

const Login = () => {
  const {
    state: { openLogin },
    dispatch,
  } = useValue();
  const usernameRef = useRef();
  const passwordRef = useRef();

  const handleClose = () => {
    dispatch({ type: "CLOSE_LOGIN" });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const username = usernameRef.current.value;
    const password = passwordRef.current.value;
    return login({ username, password }, dispatch);
  };

  return (
    <Dialog open={openLogin} onClose={handleClose}>
      <DialogTitle>
        Login
        <IconButton
          sx={{
            position: "absolute",
            top: 8,
            right: 8,
            color: (theme) => theme.palette.grey[500],
          }}
          onClick={handleClose}
        >
          <Close />
        </IconButton>
      </DialogTitle>
      <form onSubmit={handleSubmit}>
        <DialogContent dividers>
          <DialogContentText>
            Please fill your information in the fields below:
          </DialogContentText>
          <TextField
            autoFocus={true}
            margin="normal"
            variant="standard"
            id="usernme"
            label="usernme"
            type="text"
            fullWidth
            inputRef={usernameRef}
            required
          />
          <PasswordField {...{ passwordRef }} />
        </DialogContent>
        <DialogActions sx={{ px: "19px" }}>
          <Button type="submit" variant="contained" endIcon={<Send />}>
            Submit
          </Button>
        </DialogActions>
      </form>
    </Dialog>
  );
};

export default Login;
