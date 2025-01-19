import React, { useState } from 'react';
import FileUpload from '../components/UploadFile';
import RunAnalysis from '../components/TriggerAnalysis';
import VisualizationViewer from '../components/Visualization';

const StockAnalysisApp = () => {
    const [fileName, setFileName] = useState('');

    return (
        <div>
            <h1>Stock Analysis App</h1>
            <FileUpload />
            <input
                type="text"
                placeholder="Enter file name"
                value={fileName}
                onChange={(e) => setFileName(e.target.value)}
            />
            <RunAnalysis fileName={fileName} />
            <VisualizationViewer fileName={fileName} />
        </div>
    );
};

export default StockAnalysisApp;
