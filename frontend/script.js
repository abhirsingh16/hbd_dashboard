// Global Variables
const rowsPerPage = 1000;
let currentPages = {
  masters: { page: 1, total_records: 0, offset: 0 },
  complete: { page: 1, total_records: 0, offset: 0 },
  incomplete: { page: 1, total_records: 0, offset: 0 },
};

// Fetch Masters Data
function fetchMastersData(page) {
  const offset = (page - 1) * rowsPerPage; // Keep this line
  
  console.log(`Fetching Masters Data for page: ${page}`); // Debugging line

  fetch(`http://127.0.0.1:8000/read_master_input/?offset=${offset}&limit=${rowsPerPage}`)
    
    .then(response => response.json())
    .then(data => {
      console.log("Masters Data Fetched:", data); // Debugging line
      displayData("masters", data.data);

      currentPages.masters.page = page;
      currentPages.masters.total_records = data.total_records;
      currentPages.masters.offset = offset;

      const totalPages = Math.ceil(data.total_records / rowsPerPage);
      updatePagination("masters", page, totalPages);
    })
    .catch(error => console.error("Error fetching Masters data:", error));
}

// Fetch Complete Data
function fetchCompleteData(page = 1) {
  const offset = (page - 1) * rowsPerPage;
  
  fetch(`http://127.0.0.1:8000/read_complete_data/?offset=${offset}&limit=${rowsPerPage}`)
    
    .then(response => response.json())
    .then(data => {
      displayData("complete", data.data);

      currentPages.complete.page = page;
      currentPages.complete.total_records = data.total_records;
      currentPages.complete.offset = offset;

      const totalPages = Math.ceil(data.total_records / rowsPerPage);
      updatePagination("complete", page, totalPages);
    })
    .catch(error => console.error("Error fetching Complete data:", error));
}

// Fetch Incomplete Data
function fetchIncompleteData(page = 1) {
  const offset = (page - 1) * rowsPerPage;
  
  fetch(`http://127.0.0.1:8000/read_incomplete_data/?offset=${offset}&limit=${rowsPerPage}`)
    
    .then(response => response.json())
    .then(data => {
      console.log("Masters Data Fetched:", data); // Check full response
      console.log("Records:", data.data); // Check data.records specifically
      displayData("incomplete", data.data);

      currentPages.incomplete.page = page;
      currentPages.incomplete.total_records = data.total_records;
      currentPages.incomplete.offset = offset;

      const totalPages = Math.ceil(data.total_records / rowsPerPage);
      updatePagination("incomplete", page, totalPages);
    })
    .catch(error => console.error("Error fetching Incomplete data:", error));
}

// Display Data in Tables
function displayData(section, records) {
  const tableBody = document.getElementById(`${section}-table`);
  if (tableBody) {
    tableBody.innerHTML = "";

    if (records.length === 0) {
      tableBody.innerHTML = "<tr><td colspan='25'>No data available</td></tr>";
      return;
    }
    records.forEach(row => {
      let tr = document.createElement("tr");
      tr.innerHTML = `
        <td>${row.id || "N/A"}</td>
        <td>${row.category || "N/A"}</td>
        <td>${row.city || "N/A"}</td>
        <td>${row.name || "N/A"}</td>
        <td>${row.area || "N/A"}</td>
        <td>${row.address || "N/A"}</td>
        <td>${row.phone1 || "N/A"}</td>
        <td>${row.phone2 || "N/A"}</td>
        <td>${row.url || "N/A"}</td>
        <td>${row.ratings || "N/A"}</td>
        <td>${row.sub_category || "N/A"}</td>
        <td>${row.state || "N/A"}</td>
        <td>${row.country || "N/A"}</td>
        <td>${row.email || "N/A"}</td>
        <td>${row.latitude || "N/A"}</td>
        <td>${row.longitude || "N/A"}</td>
        <td>${row.reviews || "N/A"}</td>
        <td>${row.facebook_url || "N/A"}</td>
        <td>${row.linkedin_url || "N/A"}</td>
        <td>${row.twitter_url || "N/A"}</td>
        <td>${row.description || "N/A"}</td>
        <td>${row.pincode || "N/A"}</td>
        <td>${row.virtual_phone || "N/A"}</td>
        <td>${row.whatsapp_no || "N/A"}</td>
        <td>${row.phone3 || "N/A"}</td>
        <td>${row.avg_spent || "N/A"}</td>
        <td>${row.cost_for_two || "N/A"}</td>
      `;
      tableBody.appendChild(tr);
    });
  }
}

// Update Pagination
function updatePagination(section, current, total) {
  const paginationElement = document.getElementById(`pagination-info-${section}`);
  paginationElement.textContent = `Page ${current} of ${total}`;
}

function nextPage(section) {

  const currentPage = currentPages[section].page;
  const totalRecords = currentPages[section].total_records;
  const totalPages = Math.ceil(totalRecords / rowsPerPage);
  
  console.log("Current Pages Object:", currentPages);
  console.log("Section:", section);

  if (!currentPages[section]) {
    console.error(`Section "${section}" is undefined in currentPages.`);
    return;
  }


  if (currentPage < totalPages) {
    const nextPage = currentPage + 1;
    const offset = (nextPage - 1) * rowsPerPage;

    currentPages[section].page = nextPage;
    currentPages[section].offset = offset;  // Store offset
    
    console.log(`Navigating to next page of ${section}: Page ${currentPages[section].page}`);
    console.log(`Next Page Offset: ${currentPages[section].offset}`);

    if (section === "masters") {
      fetchMastersData(currentPages[section].page);
    } else if (section === "complete") {
      fetchCompleteData(currentPages[section].page);
    } else if (section === "incomplete") {
      fetchIncompleteData(currentPages[section].page);
    }
  }
}

function prevPage(section) {

  const currentPage = currentPages[section].page;

  console.log("Current Pages Object:", currentPages);
  console.log("Section:", section);

  if (!currentPages[section]) {
    console.error(`Section "${section}" is undefined in currentPages.`);
    return;
  }

  if (currentPage > 1) {
    currentPages[section].page--;
    console.log(`Navigating to previous page of ${section}: Page ${currentPages[section].page}`);

    if (section === "masters") {
      fetchMastersData(currentPages[section].page);
    } else if (section === "complete") {
      fetchCompleteData(currentPages[section].page);
    } else if (section === "incomplete") {
      fetchIncompleteData(currentPages[section].page);
    }
  }
}


function filterTable(section) {
  const input = document.getElementById(`search-${section}`).value.toLowerCase();
  const rows = document.querySelectorAll(`#${section}-table tr`);
  rows.forEach(row => {
    row.style.display = row.textContent.toLowerCase().includes(input) ? "" : "none";
  });
}

document.addEventListener("DOMContentLoaded", () => {
  fetchMastersData(1);
});