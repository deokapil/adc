import React, { useRef } from "react";
import { Stack, List, ListItem, ListItemText, Button } from "@mui/material";
import { useValue } from "./../../context/ContextProvider";
import { useScanList } from "./../../context/ScanContext";
import FormHeader from "./FormHeader";
import AddTwoToneIcon from "@mui/icons-material/AddTwoTone";
const ShipperForm = () => {
  const shipList = [];
  const agBtn = (
    <Button color="secondary" variant="contained" endIcon={<AddTwoToneIcon />}>
      Aggregate
    </Button>
  );
  return (
    <Stack direction="column" spacing={2}>
      <FormHeader title="Envelope in sensor" button={agBtn} />
      <List
        sx={{
          width: "100%",
          height: 400,
          minWidth: 450,
          overflow: "auto",
          bgcolor: "background.paper",
        }}
      >
        {shipList.map((item, index) => {
          return (
            <ListItem key={index}>
              <ListItemText primary={item.info} />
            </ListItem>
          );
        })}
      </List>
    </Stack>
  );
};

export default ShipperForm;
