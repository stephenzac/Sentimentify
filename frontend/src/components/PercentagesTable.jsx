import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import "../styles/TableStyles.css";
import nullData from "../assets/NullData.jsx";
export default function PercentagesTable(data) {
    let fullData = data.table;
    if (fullData === null) { fullData = nullData}
    const moodPercentages = fullData.moodPercentages;
    const energyPercentages = fullData.energyPercentages;
    console.log(moodPercentages);


    return (
        <TableContainer component={Paper} >
            <Table sx={{ minWidth: 20 }} aria-label="simple table">
                <TableHead>
                    <TableRow className="category-row">
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
                    <TableRow className="category-row">
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