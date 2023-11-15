import * as React from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';

export default function BasicAccordion() {
    const accordianStyle = {
        backgroundColor: "gray",
        border: "1px solid dimgray"
    }

    return (
        <div>
            <Accordion style={accordianStyle}>
                <AccordionSummary
                    expandIcon={<ExpandMoreIcon />}
                    aria-controls="panel1a-content"
                    id="panel1a-header"
                >
                    <Typography>Software Description</Typography>
                </AccordionSummary>
                <AccordionDetails>
                    <Typography>
                        Welcome to Sentimentify! This is a software that takes your spotify playlist link and puts all your songs through a sentiment tester. Then, we will tell you the mood of the songs.
                    </Typography>
                </AccordionDetails>
            </Accordion>

        </div>
    );
}