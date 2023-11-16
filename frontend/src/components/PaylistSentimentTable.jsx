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


export default function PlaylistSentimentTable(data) {
    let fullData = data.table;
    const playlist = fullData.playlist;
    const tableStyle= {
        marginBottom: "3em"
    }

    const categoryRowStyle = {
        backgroundColor: "lightgray"
    }

    return (
        <TableContainer component={Paper} style={tableStyle}>
            <Table sx={{ minWidth: 20 }} aria-label="simple table">
                <TableHead>
                    <TableRow style={categoryRowStyle}>
                        <TableCell>Playlist name</TableCell>
                        <TableCell align="right">mood</TableCell>
                        <TableCell align="right">energy</TableCell>


                    </TableRow>
                </TableHead>
                <TableBody>
                    {Object.entries(playlist).map(([name, analysis]) => (
                        <TableRow
                            key={name}
                            sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                        >
                            <TableCell component="th" scope="row">
                                {name}
                            </TableCell>

                            {analysis.mood === "positive" && <TableCell align="right"><InsertEmoticonRoundedIcon /></TableCell> }
                            {analysis.mood === "neutral" && <TableCell align="right"><SentimentNeutralRoundedIcon /></TableCell> }
                            {analysis.mood === "negative" && <TableCell align="right"><SentimentDissatisfiedRoundedIcon /></TableCell> }

                            {analysis.energy === "high" && <TableCell align="right"><BatteryChargingFullRoundedIcon /></TableCell> }
                            {analysis.energy === "medium" && <TableCell align="right"><BatteryCharging50RoundedIcon /></TableCell> }
                            {analysis.energy === "low" && <TableCell align="right"><Battery1BarRoundedIcon /></TableCell> }


                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
}