import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import FileUpload from "./components/UploadFile";
import RunAnalysis from "./components/TriggerAnalysis";
import VisualizationViewer from "./components/Visualization";

export const backendUrl = import.meta.env.VITE_BACKEND_URL;

const App = () => {
    return (
        <Router>
            <div className="bg-gray-100 min-h-screen">
                <nav className="bg-blue-600 p-4 text-white shadow">
                    <ul className="flex space-x-4">
                        <li>
                            <Link to="/" className="hover:underline">
                                Upload File
                            </Link>
                        </li>
                        <li>
                            <Link to="/run-analysis" className="hover:underline">
                                Run Analysis
                            </Link>
                        </li>
                        <li>
                            <Link to="/visualizations" className="hover:underline">
                                View Visualizations
                            </Link>
                        </li>
                    </ul>
                </nav>

                <div className="container mx-auto py-8">
                    <Routes>
                        <Route path="/" element={<FileUpload />} />
                        <Route path="/run-analysis" element={<RunAnalysis />} />
                        <Route path="/visualizations" element={<VisualizationViewer />} />
                    </Routes>
                </div>
            </div>
        </Router>
    );
};

export default App;
