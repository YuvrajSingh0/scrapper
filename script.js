const puppeteer = require('puppeteer');
const fs = require('fs');
const timeout = ms => new Promise(res => setTimeout(res, ms));

async function start() {

const browser = await puppeteer.launch({headless: false, slowMo: 100});
const page = await browser.newPage()
const navigationPromise = page.waitForNavigation()

await page.goto('https://www.gla.ac.in/Placed-student.aspx?mpgid=145&pgidtrail=145')

await navigationPromise;
await page.waitForSelector("#ctl00_ContentPlaceHolder1_ddlcourse")
await page.click('#ctl00_ContentPlaceHolder1_ddlcourse')
await page.select('#ctl00_ContentPlaceHolder1_ddlcourse', 'B.Tech.')
await page.waitForSelector("#ctl00_ContentPlaceHolder1_ddlbranch")
await page.click('#ctl00_ContentPlaceHolder1_ddlbranch')
await page.select('#ctl00_ContentPlaceHolder1_ddlbranch', 'B.Tech. - CS')
await page.waitForSelector('#ctl00_ContentPlaceHolder1_lnksearch')
await page.click('#ctl00_ContentPlaceHolder1_lnksearch')
await navigationPromise;

let data = [];
for (let i = 0; i < 39; i++) {
    await navigationPromise;
    await timeout(2000);
    
    let pageData = await page.evaluate(() => {
        let array = Array.from(document.querySelectorAll('#ctl00_secpage > section > div > div.alumni-list.palce-stu > ul > li > div.alumni'));
        return array.map((element) => 
        {
            return {
                img: element.children[0].currentSrc,
                name: element.nextSibling.nextSibling.children[0].innerText,
                company: element.nextSibling.nextSibling.children[1].innerText,
                branch: element.nextSibling.nextSibling.children[2].innerText,
            };

        })
    })
    
    data = data.concat(pageData);
    
    await navigationPromise;
    await page.waitForSelector('#ctl00_ContentPlaceHolder1_lbtnNext');
    await page.click('#ctl00_ContentPlaceHolder1_lbtnNext');
    await navigationPromise;
    await timeout(2000);
}

fs.writeFile('data.json', JSON.stringify(data), (err) => {
    if (err) throw err;
    console.log('The file has been saved!');
});

await browser.close();
}

start()
