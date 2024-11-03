const uploadButton = document.getElementById('uploadButton');
const fileInput = document.getElementById('fileInput');
const loadDataButton = document.getElementById('loadData');
const dashboardLink = document.getElementById('dashboardLink');
const generateReportButton = document.getElementById('generateReport');
const reportSection = document.getElementById('reportSection');
const reportMessage = document.getElementById('reportMessage');
const lastDataSection = document.getElementById('lastDataSection');
const lastDataBody = document.getElementById('lastDataBody');

// Load Data button functionality
loadDataButton.addEventListener("click", () => {
    uploadSection.style.display = "block"; // Show the upload section
});

// Return to Dashboard functionality
dashboardLink.addEventListener("click", () => {
    uploadSection.style.display = "none"; // Hide the upload section
});

// Handle file upload
uploadButton.addEventListener("click", () => {
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append("file", file);

    // Post file to Flask backend
    fetch("/upload", {
        method: "POST",
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message); // Show success or error message
        reportMessage.innerText = `Total Records: ${data.total_records}`; // Display total records
        reportSection.style.display = "block"; // Show the report section
        fetchLastUploadedData(); // Fetch last uploaded data after upload
    })
    .catch(error => {
        console.error("Error uploading file:", error);
    });
});

// Fetch last uploaded data
function fetchLastUploadedData() {
    fetch('/last_chart_info')
        .then(response => response.json())
        .then(data => {
            lastDataBody.innerHTML = ""; // Clear previous data
            const row = document.createElement('tr');
            Object.keys(data).forEach(key => {
                const cell = document.createElement('td');
                cell.innerText = `${key}: ${data[key]}`;
                row.appendChild(cell);
            });
            lastDataBody.appendChild(row);
            lastDataSection.style.display = "block"; // Show last data section
        })
        .catch(error => {
            console.error("Error fetching last data:", error);
        });
}

// Generate Report functionality
generateReportButton.addEventListener('click', () => {
    fetch('/report')
        .then(response => response.json())
        .then(data => {
            reportMessage.innerText = `Total Records: ${data.total_records}`;
            reportSection.style.display = "block"; // Show the report section
        })
        .catch(error => {
            console.error("Error fetching report:", error);
            alert('Error generating report.');
        });
});