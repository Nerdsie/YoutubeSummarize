async function fetchSummary(url) {
  try {
    const encoded = encodeURIComponent(url);
    const response = await fetch(`http://127.0.0.1:5000/summarize?videoUrl=${encoded}`);
    const summary = await response.text();
    return summary;
  } catch (error) {
    console.error("Error fetching summary:", error);
    return "Unable to fetch summary.";
  }
}

async function displaySummary(url) {
  const cacheKey = `summary_${url}`;
  let summary = await browser.storage.local.get(cacheKey);

  // if (!summary[cacheKey]) {
    summary[cacheKey] = await fetchSummary(url);
    await browser.storage.local.set({ [cacheKey]: summary[cacheKey] });
  // }else{
    // alert("cache")
  // }

  alert(`Summary: ${summary[cacheKey]}`);
}

browser.runtime.onMessage.addListener(async (message, sender, sendResponse) => {
  if (message.action === "getSummary") {
    const summary = await fetchSummary(window.location.href);
    return Promise.resolve({summary})
  }
});