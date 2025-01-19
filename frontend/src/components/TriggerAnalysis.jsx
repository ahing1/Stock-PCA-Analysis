import React, { useState } from "react";

const RunAnalysis = () => {
    const [fileName, setFileName] = useState("");

    const handleRunAnalysis = async () => {
        if (!fileName) {
            alert("Please enter a file name.");
            return;
        }

        try {
            const response = await fetch("/run-analysis", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ file_name: fileName }),
            });
            const result = await response.json();
            alert(result.message || "Analysis completed.");
        } catch (error) {
            alert("Error running analysis.");
        }
    };

    return (
        <div className="max-w-lg mx-auto p-6 bg-white rounded shadow">
            <h2 className="text-2xl font-bold mb-4">Run Analysis</h2>
            <input
                type="text"
                placeholder="Enter file name"
                value={fileName}
                onChange={(e) => setFileName(e.target.value)}
                className="block w-full p-2 border border-gray-300 rounded mb-4"
            />
            <button onClick={handleRunAnalysis} className="w-full bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-600 transition">Run Analysis</button>
        </div>
    );
};

export default RunAnalysis;
