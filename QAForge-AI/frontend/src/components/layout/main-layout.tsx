'use client'

import * as React from "react"
import { Sidebar } from "@/components/layout/sidebar"
import { Header } from "@/components/layout/header"

interface MainLayoutProps {
  children: React.ReactNode
}

const sidebarItems = [
  { name: "Dashboard", href: "/dashboard" },
  { name: "Projects", href: "/projects" },
  { name: "Reports", href: "/reports" },
  { name: "Settings", href: "/settings" },
]

const headerItems = [
  { name: "Dashboard", href: "/dashboard" },
  { name: "Projects", href: "/projects" },
  { name: "Reports", href: "/reports" },
]

export function MainLayout({ children }: MainLayoutProps) {
  return (
    <div className="flex h-screen overflow-hidden">
      <Sidebar className="hidden md:block w-64 flex-shrink-0" items={sidebarItems} />
      <div className="flex flex-col flex-1 overflow-hidden">
        <Header className="border-b" items={headerItems} />
        <main className="flex-1 overflow-y-auto p-4">
          {children}
        </main>
      </div>
    </div>
  )
}