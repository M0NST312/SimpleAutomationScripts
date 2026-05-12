$domain = ""
$port = 443
$tcpConnection = [System.Net.Sockets.TcpClient]::New($domain, $port)
$sslStream = [System.Net.Security.SslStream]::New($tcpConnection.GetStream(), $false, ({$true -as [System.Net.Security.RemoteCertificateValidationCallback]}))
$sslStream.AuthenticateAsClient($domain)
$cert = $sslStream.RemoteCertificate
[System.Text.Encoding]::UTF8.GetString($cert.Export([System.Security.Cryptography.X509Certificates.X509ContentType]::Cert))
$certDetails = New-Object Security.Cryptography.X509Certificates.X509Certificate2 $cert
$certDetails | Format-List *