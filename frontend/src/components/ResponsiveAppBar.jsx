import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import MenuIcon from '@mui/icons-material/Menu';
import Container from '@mui/material/Container';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
import AdbIcon from '@mui/icons-material/Adb';
import AudiotrackIcon from '@mui/icons-material/Audiotrack';
import EmojiEmotionsIcon from '@mui/icons-material/EmojiEmotions';
import SpotifyLogo from "../assets/spotify-logo.png";

import { useNavigate } from "react-router-dom";

const pages = ['Enter Playlist Link', 'About'];


function ResponsiveAppBar() {
    const [anchorElNav, setAnchorElNav] = React.useState(null);
    const [anchorElUser, setAnchorElUser] = React.useState(null);
    const navigate = useNavigate();

    const handleOpenNavMenu = (event) => {
        setAnchorElNav(event.currentTarget);
    };
    const handleOpenUserMenu = (event) => {
        setAnchorElUser(event.currentTarget);
    };

    const handleCloseNavMenu = () => {
        setAnchorElNav(null);
    };

    const handleCloseUserMenu = () => {
        setAnchorElUser(null);
    };

    const navigateToAboutPage = () => {
        navigate('/about');
        handleCloseNavMenu();
    }

    const navigateToHomePage = () => {
        navigate('/');
        handleCloseNavMenu();
    }


    return (
        <AppBar position="static" sx={{backgroundColor: "dimgray"}}>
            <Container maxWidth="xl">
                <Toolbar disableGutters>
                    <EmojiEmotionsIcon sx={{ display: { xs: 'none', md: 'flex' } }} />
                    <AudiotrackIcon sx={{ display: { xs: 'none', md: 'flex' }, mr: 1 }}/>
                    <Typography
                        variant="h6"
                        noWrap
                        component="a"
                        sx={{
                            mr: 2,
                            display: { xs: 'none', md: 'flex' },
                            fontFamily: 'monospace',
                            fontWeight: 700,
                            letterSpacing: '.1rem',
                            color: 'inherit',
                            textDecoration: 'none',
                        }}
                    >
                        Sentimentify
                    </Typography>

                    <Box sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' }}}>
                        <IconButton
                            size="large"
                            aria-label="account of current user"
                            aria-controls="menu-appbar"
                            aria-haspopup="true"
                            onClick={handleOpenNavMenu}
                            color="inherit"
                        >
                            <MenuIcon />
                        </IconButton>
                        <Menu
                            id="menu-appbar"
                            anchorEl={anchorElNav}
                            anchorOrigin={{
                                vertical: 'bottom',
                                horizontal: 'left',
                            }}
                            keepMounted
                            transformOrigin={{
                                vertical: 'top',
                                horizontal: 'left',
                            }}
                            open={Boolean(anchorElNav)}
                            onClose={handleCloseNavMenu}
                            sx={{
                                display: { xs: 'block', md: 'none' }
                            }}
                        >
                            <MenuItem key="Enter Playlist" onClick={navigateToHomePage}>
                                <Typography textAlign="center" sx={{fontFamily: "verdana, serif"}}>Enter Playlist</Typography>
                            </MenuItem>
                            <MenuItem key="About" onClick={navigateToAboutPage}>
                                <Typography textAlign="center" sx={{fontFamily: "verdana, serif"}}>About</Typography>
                            </MenuItem>

                        </Menu>
                    </Box>
                    <EmojiEmotionsIcon sx={{ display: { xs: 'flex', md: 'none' }}} />
                    <AudiotrackIcon sx={{ display: { xs: 'flex', md: 'none' }, mr: 1 }} />

                    <Typography
                        variant="h5"
                        noWrap
                        component="a"
                        sx={{
                            mr: 2,
                            display: { xs: 'flex', md: 'none' },
                            flexGrow: 1,
                            fontFamily: 'monospace',
                            fontWeight: 700,
                            letterSpacing: '.1rem',
                            color: 'inherit',
                            textDecoration: 'none',
                        }}
                    >
                        Sentimentify
                    </Typography>
                    <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
                        <MenuItem key="Enter Playlist" onClick={navigateToHomePage}>
                            <Typography textAlign="center" sx={{fontFamily: "verdana, serif"}} >Enter Playlist</Typography>
                        </MenuItem>
                        <MenuItem key="About" onClick={navigateToAboutPage}>
                            <Typography textAlign="center" sx={{fontFamily: "verdana, serif"}}>About</Typography>
                        </MenuItem>
                    </Box>

                </Toolbar>
            </Container>
        </AppBar>
    );
}
export default ResponsiveAppBar;