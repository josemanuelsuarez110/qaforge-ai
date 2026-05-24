'use client'

import * as React from "react"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

export default function ProjectsPage() {
  const [projects, setProjects] = React.useState([
    { id: 1, name: "E-commerce Platform", status: "Active", lastUpdated: "2 days ago" },
    { id: 2, name: "Mobile App", status: "Testing", lastUpdated: "1 week ago" },
    { id: 3, name: "API Integration", status: "Completed", lastUpdated: "2 weeks ago" },
  ])

  const [searchTerm, setSearchTerm] = React.useState("")

  const filteredProjects = projects.filter(project =>
    project.name.toLowerCase().includes(searchTerm.toLowerCase())
  )

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">Projects</h1>
      <div className="flex justify-between items-center">
        <Input
          placeholder="Search projects..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="max-w-sm"
        />
        <Button>Create New Project</Button>
      </div>
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        {filteredProjects.map((project) => (
          <Card key={project.id}>
            <CardHeader>
              <CardTitle>{project.name}</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-2">
                <div className="flex justify-between">
                  <span className="text-sm text-muted-foreground">Status:</span>
                  <span className={`text-sm font-medium ${project.status === "Active" ? "text-green-500" : project.status === "Testing" ? "text-yellow-500" : "text-gray-500"}`}>
                    {project.status}
                  </span>
                </div>
                <div className="flex justify-between">
                  <span className="text-sm text-muted-foreground">Last updated:</span>
                  <span className="text-sm">{project.lastUpdated}</span>
                </div>
                <div className="flex justify-end space-x-2 pt-4">
                  <Button variant="outline" size="sm">View</Button>
                  <Button variant="outline" size="sm">Edit</Button>
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  )
}