'use client'

import * as React from "react"
import Link from "next/link"
import { usePathname } from "next/navigation"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"

interface HeaderProps extends React.HTMLAttributes<HTMLDivElement> {
  items: {
    name: string
    href: string
  }[]
}

export function Header({ className, items, ...props }: HeaderProps) {
  const pathname = usePathname()

  return (
    <header
      className={cn(
        "flex h-16 items-center justify-between px-4",
        className
      )}
      {...props}
    >
      <div className="flex items-center space-x-4">
        <Link href="/" className="text-xl font-bold">
          QAForge AI
        </Link>
      </div>
      <nav className="flex items-center space-x-4">
        {items?.map((item, index) => (
          <Button
            key={index}
            variant={pathname === item.href ? "secondary" : "ghost"}
            asChild
          >
            <Link href={item.href}>
              {item.name}
            </Link>
          </Button>
        ))}
      </nav>
    </header>
  )
}