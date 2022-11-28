import React, { useRef } from "react";
import {
  Stack,
  Button,
  InputAdornment,
  List,
  ListItem,
  ListItemText,
  TextField,
  IconButton,
} from "@mui/material";
import { useValue } from "./../../context/ContextProvider";

import ArrowDownwardIcon from "@mui/icons-material/ArrowDownward";
import FormHeader from "./FormHeader";
import MailOutlineIcon from "@mui/icons-material/MailOutline";
import { createSession, scanSubmit } from "../../actions/scan";

const ScanForm = ({ scannedList, listDispatch, sessionId }) => {
  const {
    dispatch,
    state: { currentUser },
  } = useValue();
  const scanRef = useRef();
  const submitScan = async () => {
    if (!sessionId) {
      sessionId = await createSession(dispatch, listDispatch, currentUser);
    }
    const refVal = scanRef.current.value;
    await scanSubmit(refVal, sessionId, dispatch, listDispatch, currentUser);
    scanRef.current.value = "";
    scanRef.current.focus();
  };
  const nxtBtn = (
    <Button color="primary" variant="contained" endIcon={<MailOutlineIcon />}>
      Next
    </Button>
  );
  return (
    <Stack direction="column" spacing={2}>
      <FormHeader title="Sensors in this pack" button={nxtBtn} />
      <TextField
        autoFocus
        onKeyDown={(e) => {
          if (e.key == "Enter") submitScan();
        }}
        label="Scan Id"
        inputRef={scanRef}
        id="outlined-start-adornment"
        sx={{ m: 1, width: "25ch" }}
        InputProps={{
          endAdornment: (
            <InputAdornment position="end">
              <IconButton
                aria-label="toggle password visibility"
                edge="end"
                onClick={submitScan}
              >
                <ArrowDownwardIcon />
              </IconButton>
            </InputAdornment>
          ),
        }}
      />
      <List
        sx={{
          width: "100%",
          height: 325,
          minWidth: 400,
          overflow: "auto",
          bgcolor: "background.paper",
        }}
      >
        {scannedList.map((item, index) => {
          return (
            <ListItem key={index}>
              <ListItemText primary={item.retval} />
            </ListItem>
          );
        })}
      </List>
    </Stack>
  );
};

export default ScanForm;
