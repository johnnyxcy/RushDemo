#! /usr/bin/env node
const fs = require("fs");
const path = require("path");
const cli = require("prettier/cli");

let args = process.argv.slice(2);

const repoRoot = path.resolve(path.join(__dirname, "./../../.."));

const prettierrc = path.join(repoRoot, ".prettierrc.js");
if (!fs.existsSync(prettierrc)) {
    console.warn(`.prettierrc.js is not found in root dir ${repoRoot}`);
} else {
    args = args.concat(["--config", prettierrc]);
}

const prettierignore = path.join(repoRoot, ".prettierignore");
if (!fs.existsSync(prettierignore)) {
    console.warn(`.prettierignore is not found in root dir ${repoRoot}`);
} else {
    args = args.concat(["--ignore-path", prettierignore]);
}

console.debug("🦄 Running prettier");

cli.run(args);
