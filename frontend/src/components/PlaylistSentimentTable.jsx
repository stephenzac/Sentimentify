import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

import InsertEmoticonRoundedIcon from '@mui/icons-material/InsertEmoticonRounded';
import SentimentNeutralRoundedIcon from '@mui/icons-material/SentimentNeutralRounded';
import SentimentDissatisfiedRoundedIcon from '@mui/icons-material/SentimentDissatisfiedRounded';
import BatteryChargingFullRoundedIcon from '@mui/icons-material/BatteryChargingFullRounded';
import BatteryCharging50RoundedIcon from '@mui/icons-material/BatteryCharging50Rounded';
import Battery1BarRoundedIcon from '@mui/icons-material/Battery1BarRounded';
import "../styles/TableStyles.css";
import nullData from "../assets/NullData.jsx";

export default function PlaylistSentimentTable(data) {
    let fullData = data.table;
    if (fullData === null) { fullData = nullData }
    const playlist = fullData.playlist;
    const imgURL = fullData.imgURL;


    return ( 
        <>
            <img src={imgURL} style={{width: "50%", margin: "0 auto 3em auto"}} alt="Playlist cover image" />
            <TableContainer component={Paper} className="space-below-table">

                <Table sx={{ minWidth: 20 }} aria-label="simple table">
                    <TableHead>
                        <TableRow className="category-row">
                            <TableCell sx={{fontWeight: "bold", fontSize: "1em", fontFamily: "verdana, arial"}}>Playlist name</TableCell>
                            <TableCell sx={{fontWeight: "bold", fontSize: "1em", fontFamily: "verdana, arial"}} align="right">Mood</TableCell>
                            <TableCell sx={{fontWeight: "bold", fontSize: "1em", fontFamily: "verdana, arial"}} align="right">Energy</TableCell>


                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {Object.entries(playlist).map(([name, analysis]) => (
                            <TableRow
                                key={name}
                                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                            >
                                <TableCell component="th" scope="row" sx={{fontFamily: "verdana, arial", fontSize: "1em"}}>
                                    {name}
                                </TableCell>

                                {analysis.mood === "Positive" && <TableCell align="right"><InsertEmoticonRoundedIcon sx={{color: "green"}}/></TableCell> }
                                {analysis.mood === "Neutral" && <TableCell align="right"><SentimentNeutralRoundedIcon sx={{color: "orange"}}/></TableCell> }
                                {analysis.mood === "Negative" && <TableCell align="right"><SentimentDissatisfiedRoundedIcon sx={{color: "red"}}/></TableCell> }

                                {analysis.energy === "High" && <TableCell align="right"><BatteryChargingFullRoundedIcon sx={{color: "green"}}/></TableCell> }
                                {analysis.energy === "Medium" && <TableCell align="right"><BatteryCharging50RoundedIcon sx={{color: "orange"}}/></TableCell> }
                                {analysis.energy === "Low" && <TableCell align="right"><Battery1BarRoundedIcon sx={{color: "red"}}/></TableCell> }


                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </>
    );
}