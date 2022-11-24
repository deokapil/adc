import {
  Avatar,
  Box,
  Stack,
  Divider,
  InputAdornment,
  List,
  ListItem,
  ListItemText,
  Paper,
  TextField,
  Typography,
  IconButton,
} from "@mui/material";
import React from "react";
import { useValue } from "../../../context/ContextProvider";
import ImageIcon from "@mui/icons-material/Image";
import WorkIcon from "@mui/icons-material/Work";
import BeachAccessIcon from "@mui/icons-material/BeachAccess";
import ArrowDownwardIcon from "@mui/icons-material/ArrowDownward";

const Main = () => {
  const {
    state: { currentUser },
    dispatch,
  } = useValue();

  return (
    <Box
      sx={{
        display: { xs: "flex", md: "grid" },
        gridAutoRows: "minmax(100px, auto)",
        gap: 3,
        textAlign: "center",
        flexDirection: "column",
        alignItems: "center",
      }}
    >
      <Paper elevation={3} sx={{ p: 2 }}>
        <Stack direction="column" spacing={2}>
          <TextField
            label="Scan Id"
            id="outlined-start-adornment"
            sx={{ m: 1, width: "25ch" }}
            InputProps={{
              endAdornment: (
                <InputAdornment position="end">
                  <IconButton
                    aria-label="toggle password visibility"
                    edge="end"
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
              minHeight: 250,
              maxHeight: 300,
              overflow: "auto",
              bgcolor: "background.paper",
            }}
          >
            <ListItem>
              <ListItemText primary="Photos Jan 9, 2014" />
            </ListItem>
            <ListItem>
              <ListItemText primary="Photos Jan 9, 2014" />
            </ListItem>
            <ListItem>
              <ListItemText primary="Photos Jan 9, 2014" />
            </ListItem>
            <ListItem>
              <ListItemText primary="Photos Jan 9, 2014" />
            </ListItem>
            <ListItem>
              <ListItemText primary="Photos Jan 9, 2014" />
            </ListItem>
            <ListItem>
              <ListItemText primary="Work Jan 7, 2014" />
            </ListItem>
            <ListItem>
              <ListItemText primary="Vacation July 20, 2014" />
            </ListItem>
          </List>
        </Stack>
      </Paper>
    </Box>
  );
};

export default Main;
