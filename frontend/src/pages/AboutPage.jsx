
import "../styles/AboutPage.css";
import usPhoto from "../assets/us.jpeg"
function AboutPage() {
    return (
        <div className="about-page">
            <h3>About Us</h3>
            <img className="creators-photo" src={usPhoto} alt="A photo of creators" />
            <h3>Who we are</h3>
            <p>We are all UC Irvine studying Computer Science. We play the same instrument (the trombone).</p>
        </div>
    )

}


export default AboutPage;