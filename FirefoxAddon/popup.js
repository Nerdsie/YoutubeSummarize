const summaryElement = document.getElementById("summary");

async function fetchSummary(tabId) {
  try {
    const response = await browser.tabs.sendMessage(tabId, { action: "getSummary" });
    return response.summary;
  } catch (error) {
    console.error("Error fetching summary:", error);
    return error;
  }
}

document.getElementById("summarizeBtn").addEventListener("click", async () => {
  const [tab] = await browser.tabs.query({ active: true, currentWindow: true });

  if (tab.url.includes("youtube.com")) {
    const summary = await fetchSummary(tab.id);
    summaryElement.textContent = summary;
  } else {
    summaryElement.textContent = "This add-on only works on youtube.com";
  }
});
