const { chromium } = require("playwright");

(async () => {

    const browser = await chromium.launch({
        headless: false
    });

    const context = await browser.newContext({
        httpCredentials: {
            username: "name",
            password: "Pass"
        }
    });

    const page = await context.newPage();

    const url = "https://playwright.dev/mcp/introduction";

    page.setDefaultTimeout(60000);
    page.setDefaultNavigationTimeout(60000);

    try {
        await page.goto(url, {
            waitUntil: "load",
            timeout: 60000
        });

        await page.waitForLoadState("domcontentloaded");
  
        await page.waitForTimeout(10000);
        
        await page.waitForLoadState("networkidle", { timeout: 5000 }).catch(() => {
            console.log("Network not completely idle, continuing anyway...");
        });
        
    } catch (error) {
        console.log("Navigation error:", error.message);
        console.log("Attempting PDF generation anyway...");
    }

    console.log("Generating PDF...");

    await page.pdf({
        path: "output.pdf",
        format: "A4",
        printBackground: true
    });

    console.log("PDF created");

    await browser.close();

})();