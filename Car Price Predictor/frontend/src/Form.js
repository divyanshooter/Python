import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { Select ,MenuItem } from '@mui/material';

function Copyright(props) {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
      {'Copyright © '}
      <Link color="inherit" href="https://mui.com/">
        DC
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

// TODO remove, this demo shouldn't need to reset the theme.

const defaultTheme = createTheme();

export default function SignIn() {
    let price=0; 
    const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    console.log({
      email: data.get('email'),
      password: data.get('password'),
      age:data.age
    });
  };

  return (
    <ThemeProvider theme={defaultTheme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Price Predictor
          </Typography>
          <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
            {/* <Select
                    labelId="Select the Company"
                    id="Company"
                    label="Age"
                    fullWidth 
                    autoFocus>
                <MenuItem value={10}>Ten</MenuItem>
                <MenuItem value={20}>Twenty</MenuItem>
                <MenuItem value={30}>Thirty</MenuItem>
            </Select> */}
          <TextField
              margin="normal"
              required
              fullWidth
              id="company"
              label="Select the Company"
              name="company"
              autoComplete="company"
              autoFocus
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="Model"
              label="Select the Model"
              id="model"
              autoComplete="model"
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="Model"
              label="Select Year of Purchase"
              id="model"
              autoComplete="model"
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="Model"
              label="Select Fuel Type"
              id="model"
              autoComplete="model"
            />

             <TextField
              margin="normal"
              required
              fullWidth
              name="Model"
              label="Enter number of Kilometers that the car travelled"
              id="model"
              autoComplete="model"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Predict
            </Button>
              <Typography component="h1" variant="h4" align='center'>
            {price}
          </Typography>
          </Box>
        </Box>
        <Copyright sx={{ mt: 8, mb: 4 }} />
      </Container>
    </ThemeProvider>
  );
}