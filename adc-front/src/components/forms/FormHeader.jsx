import { Stack, Typography, Box } from "@mui/material";

const FormHeader = ({ title, button = null }) => {
  return (
    <Box mb="30px" textAlign={"left"}>
      <Stack justifyContent="space-between" direction="row">
        <Typography variant="p" fontWeight="bold" sx={{ m: "0 0 5px 0" }}>
          {title}
        </Typography>
        {button}
      </Stack>
    </Box>
  );
};

export default FormHeader;
