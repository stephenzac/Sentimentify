import './App.css'
import  ResponsiveAppBar  from "./components/ResponsiveAppBar.jsx";

import { Route, Routes } from "react-router-dom";
import AboutPage from "./pages/AboutPage.jsx";
import EnterPlaylistPage from "./pages/EnterPlaylistPage.jsx";

function App() {

  return (
    <div id="main-app">
        <ResponsiveAppBar />
        <Routes>
            <Route path="/" element={<EnterPlaylistPage />}/>
            <Route path="/about" element={<AboutPage />} />
        </Routes>

    </div>
  )
}

export default App
