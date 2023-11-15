

import "../styles/EnterPaylistPage.css";
import SpotifyLogo from "../assets/spotify-logo.png";

import BasicAccordion from "../components/BasicAccordian.jsx";
function EnterPlaylistPage() {
    return  (
        <div id="enter-playlist-page">
            <img className="title-logo" src={SpotifyLogo} alt="spotify logo" />
            <h1 className="title">Enter playlist link</h1>
            <input className="playlist-link-input" name="playlist-link" />
            <BasicAccordion />
        </div>
    )


}

export default EnterPlaylistPage;