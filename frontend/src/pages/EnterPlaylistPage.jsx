

import "../styles/EnterPaylistPage.css";
import SpotifyLogo from "../assets/spotify-logo.png";

import DescriptionAccordion from "../components/DescriptionAccordian.jsx";
import {useState} from "react";
import axios from "axios";

import LinearIndeterminate from "../components/LinearIndeterminate.jsx";
import SongsSentimentTable from "../components/SongsSentimentTable.jsx";
import PlaylistSentimentTable from "../components/PlaylistSentimentTable.jsx";
import PercentagesTable from "../components/PercentagesTable.jsx";
import exampleData from "../assets/example.jsx";

function EnterPlaylistPage() {
    const [link, setLink] = useState("");
    const [status, setStatus] = useState(0);
    const [data, setData] = useState(exampleData);
    const onInputChange = (event) => {
        setLink(event.target.value);
        console.log(event.target.value);
    }



    const sendLink = async () => {
        try {
            // Set loading to true while fetching data
            setStatus(1);

            // Make a request using Axios
            const response = await axios.post('http://localhost:5000/send-playlist', {"link": link});
            setLink("");
            console.log("The response received was...")
            console.log(response)
            if (response.status === 200) {
                console.log("Received a response of 200")
                setStatus(3);
                setData(response.data);
            }
            else {
                console.log(`Response was not 200. Received  ${response.status}`)
                setStatus(2)
            }

        } catch (error) {
            // Set an error if the request fails
            if (error.response) {
                console.log(`Error: A response was received but it was not 200. It was ${error.response.status}`)
                if (error.response.status === 400) {
                    setStatus(2);
                }
                else {
                    setStatus(-1);
                }

            }
            else if (error.request) {
                console.log("Error: No response was received")
                setStatus(-1);
            }
            else {
                console.log("Error: Didn't even make the request")
                setStatus(-1);
            }


        }
    }

    const returnHome = () => {
        setStatus(0);
    }

    function enterKey(event) {
        if (event.key === "Enter") {
            sendLink();
        }
    }

    return  (
        <div id="enter-playlist-page">

            {status === 0 && <img className="title-logo" src={SpotifyLogo} alt="spotify logo" /> }
            {status === 0 && <h1 className="title">Enter playlist link</h1> }
            {status === 0 && <input className="playlist-link-input" name="playlist-link" value={link} onChange={onInputChange} onKeyDown={enterKey}/> }
            {status === 0 && <button className="submit-button" onClick={sendLink}>Get Sentiment!</button> }
            {status === 0 && <DescriptionAccordion /> }

            {status === 1 && <img className="title-logo" src={SpotifyLogo} alt="spotify logo" /> }
            {status === 1 && <h1 className="title">Processing...</h1>}
            {status === 1 && <LinearIndeterminate />}
            {status === 1 && <DescriptionAccordion /> }

            {status === -1 && <img className="title-logo" src={SpotifyLogo} alt="spotify logo" /> }
            {status === -1 && <h1 className="title">Oops something went wrong</h1>}
            {status === -1 && <button className="submit-button" onClick={returnHome}>Back to start!</button> }

            {status === 2 && <img className="title-logo" src={SpotifyLogo} alt="spotify logo" /> }
            {status === 2 && <h1 className="title">Spotify playlist does not exist</h1>}

            {status === 2 && <button className="submit-button" onClick={returnHome}>Back to start!</button> }
            {status === 3 && <button className="submit-button" onClick={returnHome}>Back to start!</button> }
            {status === 3 && <PlaylistSentimentTable table={data} />}
            {status === 3 && <PercentagesTable table={data} /> }
            {status === 3 && <SongsSentimentTable table={data} /> }

            {status === 3 && <button className="submit-button" onClick={returnHome}>Back to start!</button> }



        </div>
    )


}

export default EnterPlaylistPage;