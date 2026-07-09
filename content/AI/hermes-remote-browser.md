Title: How to Connect Hermes to a Local Browser from a VPS with an SSH Reverse Tunnel
Date: 2026-07-09 18:36
Author: sdontireddy
Category: AI
Tags: AI, Hermes, Browser Automation, SSH, VPS, Remote Debugging
Slug: hermes-remote-browser
Status: published

# How to Connect Hermes to a Local Browser from a VPS with an SSH Reverse Tunnel

When Hermes runs on a VPS, it cannot directly reach a browser session running on your local machine.

If you want Hermes to control your local Edge or Chrome browser, the most reliable approach is:

1. start the browser with remote debugging enabled
2. expose that local debugging port through an SSH reverse tunnel
3. connect Hermes to the VPS-side forwarded port

This setup is especially useful when the browser session is already logged in and you want Hermes to reuse it instead of starting from scratch.

## Architecture

The connection flow looks like this:

```text
Hermes on VPS
   ↓
VPS localhost:9222
   ↓
SSH reverse tunnel
   ↓
Local Windows localhost:9222
   ↓
Edge or Chrome remote debugging
```

The browser still runs locally on your Windows machine. Hermes just reaches it through the tunnel.

## Step 1: Close Existing Browser Sessions

Before starting Edge or Chrome with remote debugging, close existing browser windows.

On Windows PowerShell:

```powershell
taskkill /F /IM msedge.exe
```

For Chrome:

```powershell
taskkill /F /IM chrome.exe
```

This matters because if the browser is already running, launching it again with `--remote-debugging-port=9222` may simply open a normal window and ignore the debugging flag.

## Step 2: Start Edge or Chrome with Remote Debugging Enabled

For Edge, try:

```powershell
& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222 --user-data-dir="C:\edge-hermes-profile"
```

If that path does not exist, try:

```powershell
& "C:\Program Files\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222 --user-data-dir="C:\edge-hermes-profile"
```

For Chrome:

```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\chrome-hermes-profile"
```

The `--user-data-dir` option creates a separate browser profile for Hermes. That keeps the debugging session isolated from your normal browser profile.

## Step 3: Verify Remote Debugging Locally

On your Windows machine, open:

```text
http://127.0.0.1:9222/json/version
```

You should see a JSON response with browser information.

You can also verify the port from PowerShell:

```powershell
netstat -ano | findstr :9222
```

Expected output should look similar to this:

```text
TCP    127.0.0.1:9222    0.0.0.0:0    LISTENING
```

If this local test does not work, fix the browser startup first before moving to the VPS tunnel step.

## Step 4: Enable Remote SSH Forwarding on the VPS

Hermes runs on the VPS, so the VPS must be able to forward traffic back to your local browser.

On the VPS, edit the SSH server config:

```bash
sudo nano /etc/ssh/sshd_config
```

Look for this setting:

```text
AllowTcpForwarding local
```

That setting only allows local forwarding and will block the reverse tunnel.

Change it to:

```text
AllowTcpForwarding remote
GatewayPorts no
```

Or use:

```text
AllowTcpForwarding yes
GatewayPorts no
```

Then restart SSH:

```bash
sudo systemctl restart ssh
```

`GatewayPorts no` is safer because it binds the forwarded port only to the VPS localhost instead of exposing it publicly.

## Step 5: Create the SSH Reverse Tunnel

From your local Windows PowerShell, run:

```powershell
ssh -R 9222:127.0.0.1:9222 root@YOUR_VPS_IP
```

Replace `YOUR_VPS_IP` with your actual VPS IP address.

Keep that SSH session open.

This command means:

```text
VPS port 9222 → forwards to → local Windows 127.0.0.1:9222
```

## Step 6: Verify the Tunnel from the VPS

Inside the VPS SSH session, run:

```bash
curl http://127.0.0.1:9222/json/version
```

If the reverse tunnel is working, this should return the same browser JSON that worked locally on Windows.

If that works, Hermes can now connect to your local browser through the VPS.

## Step 7: Connect Hermes to the Browser

In Hermes, run:

```text
/browser connect http://127.0.0.1:9222
```

If Hermes expects only a host and port, use:

```text
/browser connect 127.0.0.1:9222
```

At this point, Hermes should be connected to your local Edge or Chrome browser.

## Troubleshooting

### Problem: `msedge.exe` is not recognized

If PowerShell cannot find Edge in your PATH, use the full executable path:

```powershell
& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222 --user-data-dir="C:\edge-hermes-profile"
```

If needed, find the exact location first:

```powershell
Get-ChildItem "C:\Program Files*", "C:\Users\$env:USERNAME\AppData\Local\Microsoft\Edge\Application" -Recurse -Filter msedge.exe -ErrorAction SilentlyContinue | Select-Object -First 5 FullName
```

Then use the returned path.

### Problem: Browser opens, but `/json/version` does not work locally

If `http://127.0.0.1:9222/json/version` does not return JSON, remote debugging is not active.

Try restarting the browser with the remote debugging flag:

```powershell
taskkill /F /IM msedge.exe

& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222 --user-data-dir="C:\edge-hermes-profile"
```

Then check the port again:

```powershell
netstat -ano | findstr :9222
```

You need to see port `9222` listening.

### Problem: Local browser works, but VPS curl fails

If the VPS shows this error:

```bash
curl: (7) Failed to connect to 127.0.0.1 port 9222
```

then the VPS cannot see the forwarded browser port.

Check the SSH tunnel:

```bash
ss -lntp | grep 9222
```

If nothing shows, the tunnel did not bind.

Reconnect from Windows with verbose logging:

```powershell
ssh -v -R 9222:127.0.0.1:9222 root@YOUR_VPS_IP
```

Look for an error like:

```text
remote port forwarding failed for listen port 9222
```

If you see that, check `/etc/ssh/sshd_config` on the VPS and make sure this is not limited to local forwarding:

```text
AllowTcpForwarding local
```

Change it to:

```text
AllowTcpForwarding remote
```

Then restart SSH:

```bash
sudo systemctl restart ssh
```

### Problem: `AllowTcpForwarding local`

This was the key issue in this setup.

`AllowTcpForwarding local` only allows `ssh -L` forwarding.

For Hermes on a VPS connecting back to a local browser, you need `ssh -R`, which requires remote forwarding.

Correct setting:

```text
AllowTcpForwarding remote
GatewayPorts no
```

Then restart SSH:

```bash
sudo systemctl restart ssh
```

### Problem: Port 9222 already in use on the VPS

Use a different VPS-side port:

```powershell
ssh -R 9333:127.0.0.1:9222 root@YOUR_VPS_IP
```

Then on the VPS:

```bash
curl http://127.0.0.1:9333/json/version
```

Then connect Hermes:

```text
/browser connect http://127.0.0.1:9333
```

### Problem: Tunnel binds to IPv6 instead of IPv4

Try these from the VPS:

```bash
curl http://localhost:9222/json/version
curl http://[::1]:9222/json/version
```

If `localhost` works but `127.0.0.1` does not, connect Hermes with:

```text
/browser connect http://localhost:9222
```

### Problem: Ubuntu shows `System restart required`

This message may appear when logging into the VPS:

```text
*** System restart required ***
```

That is only an Ubuntu update notice. It is not related to Hermes or browser debugging.

You can handle it later with:

```bash
sudo reboot
```

Do not reboot while testing unless you are ready to reconnect the SSH tunnel and restart Hermes.

## Security Notes

Do not expose the browser debugging port publicly.

Avoid starting Edge or Chrome with this flag:

```text
--remote-debugging-address=0.0.0.0
```

Remote debugging gives control over the browser session. Anyone who can access that port may be able to inspect pages, cookies, sessions, and browser state.

The safer approach is:

```text
Local browser debugging port → SSH reverse tunnel → VPS localhost only
```

Use:

```text
GatewayPorts no
```

to avoid exposing the forwarded port to the public internet.

## Final Working Command Set

### On Windows

Start Edge:

```powershell
taskkill /F /IM msedge.exe

& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222 --user-data-dir="C:\edge-hermes-profile"
```

Verify locally:

```text
http://127.0.0.1:9222/json/version
```

Create the reverse tunnel:

```powershell
ssh -R 9222:127.0.0.1:9222 root@YOUR_VPS_IP
```

### On the VPS

Verify the tunnel:

```bash
curl http://127.0.0.1:9222/json/version
```

Connect Hermes:

```text
/browser connect http://127.0.0.1:9222
```

Once the VPS curl command returns browser JSON, Hermes should be able to connect successfully.
