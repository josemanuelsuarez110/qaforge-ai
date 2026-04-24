import "../styles/globals.css";

export const metadata = {
  title: "QAForge AI - Dashboard",
  description: "Panel de control para la plataforma de automatización de pruebas QAForge AI"
};

export default function RootLayout({ children }) {
  return (
    <html lang="es">
      <body className="min-h-screen bg-primary text-white">{children}</body>
    </html>
  );
}
