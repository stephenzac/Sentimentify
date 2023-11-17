
import "../styles/AboutPage.css";
import usPhoto from "../assets/us.jpeg"
function AboutPage() {
    return (
        <div className="about-page">
            <h3>About Us</h3>
            <img className="creators-photo" src={usPhoto} alt="A photo of creators" />
            <h3>Who we are</h3>
            <p>Welcome to our web application for ICSSC's 2023 WebJam. In the picture 
                above, from left to right, we are Stanley Liu, Michelle Lee, and 
                Stephen Zacarias. The three of us are all majoring in Computer Science.
                Since we are all musicians (trombone players), we
                decided it would be fun to make a web application that analyzes songs on
                Spotify.
                </p>
        </div>
    )

}


export default AboutPage;