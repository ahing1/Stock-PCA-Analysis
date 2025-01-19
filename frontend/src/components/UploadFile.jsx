import React, { useState } from "react";

const FileUpload = () => {
    const [file, setFile] = useState(null);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleUpload = async () => {
        if (!file) {
            alert("Please select a file.");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await fetch("/upload", {
                method: "POST",
                body: formData,
            });
            const result = await response.json();
            alert(result.message || "File uploaded successfully.");
        } catch (error) {
            alert("Error uploading file.");
        }
    };

    return (
        <div className="max-w-lg mx-auto p-6 bg-white rounded shadow">
            <h2 className="text-2xl font-bold mb-4">Upload Stock Data</h2>
            <input type="file" onChange={handleFileChange} className="block w-full text-sm text-gray-700 file:mr-4 file:py-2 file:px-4 file:rounded file:border file:border-gray-300 file:text-sm file:font-semibold file:bg-gray-50 file:text-gray-700 hover:file:bg-gray-100"/>
            <button onClick={handleUpload} className="mt-4 w-full bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-600 transition">Upload</button>
        </div>
    );
};

export default FileUpload;
