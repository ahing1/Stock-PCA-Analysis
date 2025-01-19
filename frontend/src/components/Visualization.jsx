import React, { useState } from "react";

const VisualizationViewer = () => {
    const [fileName, setFileName] = useState("");

    const visualizationUrls = [
        `${fileName}_2D.png`,
        `${fileName}_3D.png`,
        `${fileName}_Portfolio.png`,
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
            {fileName &&
                visualizationUrls.map((url, index) => (
                    <img
                        key={index}
                        src={`/visualizations/${url}`}
                        alt={`Visualization ${index}`}
                        style={{ width: "400px", margin: "10px" }}
                        className="rounded shadow"
                    />
                ))}
        </div>
    );
};

export default VisualizationViewer;
