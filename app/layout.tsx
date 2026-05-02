import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "British TV Dramas & Mysteries",
  description: "Your cozy guide to the best British TV — classics & new favorites.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
