const { chromium } = require("playwright");

async function generatePDF(url) {
    const browser = await chromium.launch();

    const page = await browser.newPage();

    await page.goto(url, {
        waitUntil: "networkidle"
    });

    await page.waitForTimeout(2000);

    // Generate PDF
    await page.pdf({
        path: "output.pdf",
        format: "A4",
        printBackground: true,
        margin: {
            top: "10mm",
            bottom: "10mm",
            left: "10mm",
            right: "10mm"
        }
    });

    await browser.close();

    console.log("PDF created: output.pdf");
}

generatePDF("https://playwright.dev/mcp/introduction");