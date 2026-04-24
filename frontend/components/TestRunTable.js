"use client";

export default function TestRunTable({ runs }) {
  return (
    <div className="rounded-3xl border border-slate-700 bg-slate-900/80 p-4 shadow-xl shadow-slate-900/25">
      <div className="mb-4 flex items-center justify-between">
        <div>
          <h2 className="text-lg font-semibold text-white">Últimos test runs</h2>
          <p className="text-sm text-slate-400">Vista rápida de ejecución y estado de los suites</p>
        </div>
      </div>
      <div className="overflow-x-auto">
        <table className="min-w-full text-left text-sm">
          <thead>
            <tr className="border-b border-slate-700 text-slate-400">
              <th className="px-4 py-3">Nombre</th>
              <th className="px-4 py-3">Status</th>
              <th className="px-4 py-3">Pasaron</th>
              <th className="px-4 py-3">Fallaron</th>
              <th className="px-4 py-3">Duración</th>
              <th className="px-4 py-3">Creado</th>
            </tr>
          </thead>
          <tbody>
            {runs.map((run) => (
              <tr key={run.id} className="border-b border-slate-800 last:border-b-0">
                <td className="px-4 py-4 text-white">{run.name}</td>
                <td className="px-4 py-4">
                  <span
                    className={`inline-flex rounded-full px-3 py-1 text-xs font-semibold ${
                      run.status === "completed"
                        ? "bg-emerald-500/15 text-emerald-300"
                        : run.status === "running"
                        ? "bg-sky-500/15 text-sky-300"
                        : "bg-amber-500/15 text-amber-300"
                    }`}
                  >
                    {run.status}
                  </span>
                </td>
                <td className="px-4 py-4 text-slate-100">{run.passCount}</td>
                <td className="px-4 py-4 text-slate-100">{run.failCount}</td>
                <td className="px-4 py-4 text-slate-100">{run.duration}</td>
                <td className="px-4 py-4 text-slate-400">{new Date(run.createdAt).toLocaleString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
