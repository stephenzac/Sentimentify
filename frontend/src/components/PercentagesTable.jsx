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


export default function PercentagesTable(data) {
    let fullData = data.table;
    const moodPercentages = fullData.moodPercentages;
    const energyPercentages = fullData.energyPercentages;
    console.log(moodPercentages);

    const categoryRowStyle = {
        backgroundColor: "lightgray"
    }

    return (
        <TableContainer component={Paper} >
            <Table sx={{ minWidth: 20 }} aria-label="simple table">
                <TableHead>
                    <TableRow style={categoryRowStyle}>
                        <TableCell> Mood Category</TableCell>
                        <TableCell align="right">Percentage</TableCell>

                    </TableRow>
                </TableHead>
                <TableBody>
                    {Object.entries(moodPercentages).map(([category, percent]) => (
                        <TableRow
                            key={category}
                            sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                        >
                            <TableCell component="th" scope="row">
                                {category}
                            </TableCell>

                            <TableCell align="right">{percent * 100}%</TableCell>

                        </TableRow>
                    ))}


                </TableBody>
                <TableHead>
                    <TableRow style={categoryRowStyle}>
                        <TableCell> Energy Category</TableCell>
                        <TableCell align="right">Percentage</TableCell>

                    </TableRow>
                </TableHead>
                <TableBody>
                    {Object.entries(energyPercentages).map(([category, percent]) => (
                        <TableRow
                            key={category}
                            sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                        >
                            <TableCell component="th" scope="row">
                                {category}
                            </TableCell>

                            <TableCell align="right">{percent * 100}%</TableCell>

                        </TableRow>
                    ))}


                </TableBody>
            </Table>


        </TableContainer>
    );
}