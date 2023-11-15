

import "../styles/EnterPaylistPage.css";
import SpotifyLogo from "../assets/spotify-logo.png";

import BasicAccordion from "../components/BasicAccordian.jsx";
import {useState} from "react";

function EnterPlaylistPage() {
    const [link, setLink] = useState("");
    const onInputChange = (event) => {
        setLink(event.target.value);
        console.log(event.target.value);
    }
    return  (
        <div id="enter-playlist-page">
            <img className="title-logo" src={SpotifyLogo} alt="spotify logo" />
            <h1 className="title">Enter playlist link</h1>
            <input className="playlist-link-input" name="playlist-link" value={link} onChange={onInputChange}/>
            <button className="submit-button">Get Sentiment!</button>
            <BasicAccordion />
        </div>
    )


}

export default EnterPlaylistPage;