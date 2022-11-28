import { Chip, Grid, Stack, Typography, Divider } from "@mui/material";
import React from "react";
import FormHeader from "./FormHeader";

const ShipperInfo = () => {
  return (
    <Stack direction="column" spacing={2}>
      <FormHeader title="Shipper Class" />
      <Grid container spacing={2}>
        <Grid item xs={12}>
          <Stack
            spacing={2}
            direction="row"
            divider={<Divider orientation="vertical" flexItem />}
            justifyContent={"center"}
          >
            <div>
              <Typography>A</Typography>
              <Chip label="23" color="primary" />
            </div>
          </Stack>
        </Grid>
        <Grid item md={6}>
          <Stack
            spacing={2}
            direction="row"
            divider={<Divider orientation="vertical" flexItem />}
            justifyContent={"center"}
          ></Stack>
        </Grid>
        <Grid item ms={6}>
          <Stack
            spacing={2}
            direction="row"
            divider={<Divider orientation="vertical" flexItem />}
            justifyContent={"center"}
          ></Stack>
        </Grid>
      </Grid>
    </Stack>
  );
};

export default ShipperInfo;
