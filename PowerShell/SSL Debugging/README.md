# SSL Certificate Debugger

PowerShell scripts to retrieve and display SSL certificate information from domains.

## Purpose

These scripts connect to a domain's SSL port (default 443) and retrieve detailed information about the server's SSL certificate.

## Scripts

- `powerSSL.ps1`: Full-featured version with error handling
- `sslcert.ps1`: Simplified version

## Requirements

- PowerShell
- .NET Framework (usually pre-installed on Windows)

## Usage

### powerSSL.ps1

1. Edit the domain variable at the top:
   ```powershell
   $domain = "example.com"
   $port = 443  # Optional, defaults to 443
   ```

2. Run the script:
   ```powershell
   .\powerSSL.ps1
   ```

### sslcert.ps1

1. Edit the domain:
   ```powershell
   $domain = "example.com"
   ```

2. Run the script:
   ```powershell
   .\sslcert.ps1
   ```

## Output

The scripts display detailed certificate information including:
- Subject
- Issuer
- Valid dates
- Thumbprint
- Serial number
- And more certificate properties

## Features

- DNS resolution verification
- SSL/TLS handshake
- Certificate validation (bypassed for debugging)
- Comprehensive certificate details
- Error handling for connection issues

## Security Note

These scripts bypass certificate validation for debugging purposes. Do not use in production environments where security is critical.