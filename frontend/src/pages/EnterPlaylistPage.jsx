

import "../styles/EnterPaylistPage.css";
import SpotifyLogo from "../assets/spotify-logo.png";

import BasicAccordion from "../components/BasicAccordian.jsx";
import {useState} from "react";

function EnterPlaylistPage() {
    const [link, setLink] = useState("");
    const [hasResults, setHasResults] = useState(0);
    const onInputChange = (event) => {
        setLink(event.target.value);
        console.log(event.target.value);
    }

    const sendLink = () => {
        setLink("");
        console.log(link)
    }


    return  (
        <div id="enter-playlist-page">

            {hasResults === 0 && <img className="title-logo" src={SpotifyLogo} alt="spotify logo" /> }
            {hasResults === 0 && <h1 className="title">Enter playlist link</h1> }
            {hasResults === 0 && <input className="playlist-link-input" name="playlist-link" value={link} onChange={onInputChange}/> }
            {hasResults === 0 && <button className="submit-button" onClick={sendLink}>Get Sentiment!</button> }
            {hasResults === 0 && <BasicAccordion /> }

        </div>
    )


}

export default EnterPlaylistPage;