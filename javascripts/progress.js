// Interactive Progress & LocalStorage Tracker for Python for DevOps Roadmap
document.addEventListener("DOMContentLoaded", () => {
    initProgressTracker();
});

// Support instant SPA page navigation in MkDocs Material
if (typeof location$ !== "undefined") {
    location$.subscribe(() => {
        setTimeout(initProgressTracker, 100);
    });
}

function initProgressTracker() {
    const taskItems = document.querySelectorAll(".task-list-item input[type='checkbox']");
    if (!taskItems.length) return;

    // Enable all checkboxes so user can click them
    taskItems.forEach((checkbox, index) => {
        checkbox.disabled = false;
        checkbox.style.cursor = "pointer";

        const label = checkbox.parentElement ? checkbox.parentElement.textContent.trim().slice(0, 40) : `item_${index}`;
        const storageKey = `roadmap_chk_${index}_${label.replace(/\s+/g, "_")}`;

        // Restore saved state
        const savedState = localStorage.getItem(storageKey);
        if (savedState === "true") {
            checkbox.checked = true;
        }

        // Listen for user check/uncheck
        checkbox.addEventListener("change", () => {
            localStorage.setItem(storageKey, checkbox.checked);
            updateProgressBar();
        });
    });

    injectProgressBar(taskItems);
}

function injectProgressBar(taskItems) {
    let container = document.getElementById("roadmap-progress-container");
    if (!container) {
        const header = document.querySelector("h1");
        if (header) {
            container = document.createElement("div");
            container.id = "roadmap-progress-container";
            container.style.cssText = `
                margin: 20px 0;
                padding: 16px 20px;
                background: var(--md-code-bg-color, #1e293b);
                border-radius: 8px;
                border: 1px solid var(--md-default-fg-color--lightest, #334155);
            `;
            header.insertAdjacentElement("afterend", container);
        }
    }

    if (container) {
        updateProgressBar();
    }
}

function updateProgressBar() {
    const taskItems = document.querySelectorAll(".task-list-item input[type='checkbox']");
    if (!taskItems.length) return;

    const total = taskItems.length;
    let checkedCount = 0;
    taskItems.forEach(item => {
        if (item.checked) checkedCount++;
    });

    const pct = Math.round((checkedCount / total) * 100);
    const container = document.getElementById("roadmap-progress-container");
    if (!container) return;

    container.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-weight: 600; font-size: 15px;">📊 Your Learning Progress</span>
            <span style="font-weight: 700; color: var(--md-primary-fg-color, #009688); font-size: 15px;">${pct}% (${checkedCount} / ${total} Finished)</span>
        </div>
        <div style="width: 100%; height: 10px; background: rgba(150,150,150,0.2); border-radius: 5px; overflow: hidden;">
            <div style="width: ${pct}%; height: 100%; background: linear-gradient(90deg, #009688, #ff5722); transition: width 0.3s ease;"></div>
        </div>
        <div style="margin-top: 10px; font-size: 13px; opacity: 0.8;">
            💡 <em>Click any checkbox below to check off topics. Progress is automatically saved in your browser!</em>
        </div>
    `;
}
