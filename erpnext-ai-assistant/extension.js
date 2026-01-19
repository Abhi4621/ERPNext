const vscode = require('vscode');

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
    console.log('Congratulations, your extension "erpnext-ai-assistant" is now active!');

    // Command 1: Simple Hello World / Scanner Status
    let helloWorld = vscode.commands.registerCommand('erpnext-ai-assistant.helloWorld', function () {
        vscode.window.showInformationMessage('ERPNext AI Assistant: Retrieval Engine is Online!');
    });

    // Command 2: Open the QA Accuracy Dashboard inside VS Code
    let openDashboard = vscode.commands.registerCommand('erpnext-ai-assistant.openDashboard', function () {
        const panel = vscode.window.createWebviewPanel(
            'erpnextDashboard',
            'ERPNext AI QA Dashboard',
            vscode.ViewColumn.Two, 
            { enableScripts: true }
        );

        // This links your Streamlit Dashboard into a VS Code Tab
        panel.webview.html = `
            <!DOCTYPE html>
            <html>
            <body style="margin:0;padding:0;overflow:hidden;background-color:white;">
                <iframe src="http://localhost:8501" style="width:100%;height:100vh;border:none"></iframe>
            </body>
            </html>
        `;
    });

    context.subscriptions.push(helloWorld, openDashboard);
}

function deactivate() {}

module.exports = { activate, deactivate }