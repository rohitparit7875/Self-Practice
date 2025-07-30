using QRCoder;
using System;
using System.Drawing;

class QRCodeGen
{
    static void Main()
    {
        Console.Write("Enter text to generate QR Code: ");
        string input = Console.ReadLine();

        QRCodeGenerator qrGenerator = new QRCodeGenerator();
        QRCodeData qrCodeData = qrGenerator.CreateQrCode(input, QRCodeGenerator.ECCLevel.Q);
        QRCode qrCode = new QRCode(qrCodeData);
        Bitmap qrCodeImage = qrCode.GetGraphic(20);

        qrCodeImage.Save("qrcode.png");
        Console.WriteLine("QR Code saved as qrcode.png");
    }
}
