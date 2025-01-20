import React, { useState } from "react";
import { backendUrl } from "../App.jsx";

const VisualizationViewer = () => {
    const [fileName, setFileName] = useState("");

    // Construct URLs to fetch images from the backend
    const visualizationUrls = [
        `${backendUrl}/visualizations/${fileName}_2D.png`,
        `${backendUrl}/visualizations/${fileName}_3D.png`,
        `${backendUrl}/visualizations/${fileName}_Portfolio.png`,
    ];

    return (
        <div className="max-w-lg mx-auto p-6 bg-white rounded shadow">
            <h2 className="text-2xl font-bold mb-4">View Visualizations</h2>
            <input
                type="text"
                placeholder="Enter file name"
                value={fileName}
                onChange={(e) => setFileName(e.target.value)}
                className="block w-full p-2 border border-gray-300 rounded mb-4"
            />
            <div className="grid grid-cols-1 gap-4">
                {fileName &&
                    visualizationUrls.map((url, index) => (
                        <div key={index}>
                            <img
                                src={url} // Image URL
                                alt={`Visualization ${index}`} // Alt text for accessibility
                                style={{ width: "400px", margin: "10px" }}
                                className="rounded shadow"
                                onError={(e) => {
                                    e.target.src = "/placeholder-image.png"; // Fallback image
                                    e.target.alt = "Visualization not available";
                                }}
                            />
                            <p>Visualization {index + 1}</p>
                        </div>
                    ))}
            </div>
        </div>
    );
};

export default VisualizationViewer;
