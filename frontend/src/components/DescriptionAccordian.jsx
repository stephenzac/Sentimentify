import * as React from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';


export default function DescriptionAccordion() {

    return (
        <div>
            <Accordion sx={{
                backgroundColor: "rgb(128, 128, 128)",
                border: "1px solid dimgray"}}>
                <AccordionSummary
                    expandIcon={<ExpandMoreIcon />}
                    aria-controls="panel1a-content"
                    id="panel1a-header"
                >
                    <Typography sx={{
                        fontFamily: "verdana, serif",
                        fontWeight: "bold",
                        color: "whitesmoke"
                    }}>Description</Typography>
                </AccordionSummary>
                <AccordionDetails>
                    <Typography sx={{
                        fontFamily: "verdana, serif",
                        fontWeight: "bold",
                        color: "whitesmoke"}}>
                        Welcome to Sentimentify! This is a software that takes your spotify playlist link and puts all your songs through a sentiment tester. Then, we will tell you the mood of the songs.
                    </Typography>
                </AccordionDetails>
            </Accordion>

        </div>
    );
}