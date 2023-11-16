
import "../styles/AboutPage.css";
import usPhoto from "../assets/us.jpeg"
function AboutPage() {
    return (
        <div className="about-page">
            <h3>About Us</h3>
            <img className="creators-photo" src={usPhoto} alt="A photo of creators" />
            <h3>Who we are</h3>
            <p>We are all students at UC Irvine studying Computer Science.
                We play the same instrument (the trombone).
                We are participating in ICSSC's 2023 WebJam as a group</p>
        </div>
    )

}


export default AboutPage;