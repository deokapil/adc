import React, { useState, useMemo } from "react";
import { ThemeProvider } from "@mui/material/styles";
import { Box, createTheme, CssBaseline } from "@mui/material";

import Protected from "../../components/protected/Protected";
import Login from "../../components/user/Login";
import Main from "./main/Main";
import TopNav from "../../components/TopNav";
import { ScanProvider } from "../../context/ScanContext";

const drawerWidth = 240;

export default function Dashboard() {
  const [dark, setDark] = useState(true);

  const darkTheme = useMemo(
    () =>
      createTheme({
        palette: {
          mode: dark ? "dark" : "light",
        },
      }),
    [dark]
  );

  return (
    <ThemeProvider theme={darkTheme}>
      <Box sx={{ display: "flex" }}>
        <CssBaseline />
        <TopNav dark={dark} setDark={setDark} />
        <Protected>
          <ScanProvider>
            <Main />
          </ScanProvider>
        </Protected>
      </Box>
      <Login />
    </ThemeProvider>
  );
}
