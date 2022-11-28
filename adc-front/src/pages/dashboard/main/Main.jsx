import { Box, Stack, Divider, Paper } from "@mui/material";
import React from "react";
import ScanForm from "../../../components/forms/ScanForm";
import ShipperForm from "../../../components/forms/ShipperForm";
import ShipperInfo from "../../../components/forms/ShipperInfo";
import { useScanList } from "../../../context/ScanContext";

const Main = () => {
  const {
    state: { scannedList, ...rest },
    dispatch: listDispatch,
  } = useScanList();

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
        <Stack
          direction="row"
          divider={<Divider orientation="vertical" flexItem />}
          spacing={2}
        >
          <ScanForm
            scannedList={scannedList}
            listDispatch={listDispatch}
            {...rest}
          />
          <ShipperForm scannedList={scannedList} listDispatch={listDispatch} />
          <ShipperInfo />
        </Stack>
      </Paper>
    </Box>
  );
};

export default Main;
