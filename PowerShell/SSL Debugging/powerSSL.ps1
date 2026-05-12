$domain = ""
$port = 443

try {
    # Resolve the domain name to ensure it is reachable
    $ipAddress = (Resolve-DnsName -Name $domain).IPAddress
    if (-not $ipAddress) {
        throw "Unable to resolve domain: $domain"
    }

    # Create a TCP connection to the server
    $tcpClient = New-Object System.Net.Sockets.TcpClient($ipAddress, $port)
    $sslStream = New-Object System.Net.Security.SslStream($tcpClient.GetStream(), $false, ([System.Net.Security.RemoteCertificateValidationCallback]{ $true }))

    # Authenticate as a client
    $sslStream.AuthenticateAsClient($domain)

    # Retrieve the certificate
    $cert = $sslStream.RemoteCertificate
    $cert2 = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2($cert)
    
    # Display certificate details
    $cert2 | Format-List *
}
catch {
    Write-Error "Failed to retrieve SSL certificate: $_"
}
finally {
    # Close the connection
    if ($sslStream) { $sslStream.Close() }
    if ($tcpClient) { $tcpClient.Close() }
}

