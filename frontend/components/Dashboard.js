"use client";

import { useEffect, useMemo, useState } from "react";
import axios from "axios";
import {
  BarChart,
  Bar,
  ResponsiveContainer,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";
import { CheckCircle2, BarChart3, Sparkles, ShieldCheck } from "lucide-react";
import MetricCard from "./MetricCard";
import TestRunTable from "./TestRunTable";

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || "http://localhost:3001/api"
});

export default function Dashboard() {
  const [runs, setRuns] = useState([]);
  const [suggestions, setSuggestions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const loadData = async () => {
      try {
        const [runsRes, suggestionsRes] = await Promise.all([
          api.get("/tests"),
          api.get("/reports/ai-suggestions")
        ]);

        setRuns(runsRes.data.testRuns || []);
        setSuggestions(suggestionsRes.data.suggestions || []);
      } catch (err) {
        setError("No se pudo conectar con el backend. Verifica que el servicio esté en ejecución.");
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, []);

  const totals = useMemo(() => {
    const totalRuns = runs.length;
    const activeRuns = runs.filter((run) => run.status === "running").length;
    const totalPassed = runs.reduce((sum, run) => sum + (run.passCount || 0), 0);
    const totalFailed = runs.reduce((sum, run) => sum + (run.failCount || 0), 0);
    const passRate = totalRuns > 0 ? Math.round((totalPassed / Math.max(totalPassed + totalFailed, 1)) * 100) : 0;

    return {
      totalRuns,
      activeRuns,
      totalPassed,
      totalFailed,
      passRate
    };
  }, [runs]);

  const chartData = runs.map((run) => ({
    name: run.name,
    passed: run.passCount,
    failed: run.failCount
  }));

  return (
    <main className="mx-auto flex min-h-screen max-w-7xl flex-col gap-8 px-6 py-8 lg:px-10">
      <section className="rounded-[2rem] border border-slate-700 bg-slate-950/80 p-8 shadow-2xl shadow-slate-950/20">
        <div className="flex flex-col gap-4 lg:flex-row lg:items-end lg:justify-between">
          <div>
            <p className="text-sm uppercase tracking-[0.28em] text-slate-400">QAForge AI</p>
            <h1 className="mt-4 text-4xl font-semibold text-white">Dashboard de automatización de pruebas</h1>
            <p className="mt-3 max-w-2xl text-base leading-7 text-slate-300">
              Visualiza ejecuciones en paralelo, métricas en tiempo real y sugerencias AI para tus pipelines de pruebas.
            </p>
          </div>
          <div className="rounded-3xl bg-slate-900/80 p-5 text-slate-200 shadow-xl shadow-slate-950/20">
            <p className="text-sm uppercase text-slate-400">Estado de servicio</p>
            <p className="mt-2 text-2xl font-semibold text-emerald-300">{loading ? "Cargando..." : error ? "Desconectado" : "Conectado"}</p>
          </div>
        </div>
      </section>

      {error ? (
        <div className="rounded-3xl border border-rose-500/30 bg-rose-500/10 p-6 text-rose-100">
          <strong>Error:</strong> {error}
        </div>
      ) : null}

      <section className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
        <MetricCard title="Test runs" value={totals.totalRuns} delta="Ejecuciones totales" icon={BarChart3} />
        <MetricCard title="Pass rate" value={`${totals.passRate}%`} delta="Tasa de éxito" icon={CheckCircle2} />
        <MetricCard title="Fallos" value={totals.totalFailed} delta="Pruebas fallidas" icon={Sparkles} />
        <MetricCard title="En ejecución" value={totals.activeRuns} delta="Workers activos" icon={ShieldCheck} />
      </section>

      <section className="grid gap-6 xl:grid-cols-[1.45fr_0.95fr]">
        <div className="rounded-3xl border border-slate-700 bg-slate-900/80 p-6 shadow-xl shadow-slate-950/20">
          <div className="mb-6 flex items-center justify-between">
            <div>
              <h2 className="text-xl font-semibold text-white">Cobertura de suites</h2>
              <p className="text-sm text-slate-400">Comparación de pruebas completadas y fallidas.</p>
            </div>
          </div>
          <div className="h-[320px]">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={chartData} margin={{ top: 16, right: 10, left: -10, bottom: 0 }}>
                <CartesianGrid stroke="#334155" strokeDasharray="4 4" />
                <XAxis dataKey="name" stroke="#94a3b8" tick={{ fontSize: 12 }} />
                <YAxis stroke="#94a3b8" />
                <Tooltip contentStyle={{ backgroundColor: "#0f172a", borderRadius: 12, borderColor: "#334155" }} />
                <Bar dataKey="passed" stackId="a" fill="#22c55e" radius={[10, 10, 0, 0]} />
                <Bar dataKey="failed" stackId="a" fill="#ef4444" radius={[10, 10, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="rounded-3xl border border-slate-700 bg-slate-900/80 p-6 shadow-xl shadow-slate-950/20">
          <h2 className="text-xl font-semibold text-white">Sugerencias AI</h2>
          <p className="mt-2 text-sm text-slate-400">Recomendaciones simuladas que ayudan a mejorar la cobertura de pruebas.</p>
          <div className="mt-6 space-y-4">
            {suggestions.length > 0 ? (
              suggestions.map((suggestion, index) => (
                <div key={index} className="rounded-3xl border border-slate-700 bg-slate-950/80 p-4 text-slate-200">
                  <p>{suggestion}</p>
                </div>
              ))
            ) : (
              <p className="text-slate-400">Sin sugerencias disponibles.</p>
            )}
          </div>
        </div>
      </section>

      <TestRunTable runs={runs} />

      <section className="rounded-3xl border border-slate-700 bg-slate-900/80 p-6 shadow-xl shadow-slate-950/20">
        <h2 className="text-xl font-semibold text-white">Visión general</h2>
        <p className="mt-3 text-slate-400">
          QAForge AI centraliza ejecuciones, habilita feedback en CI/CD y monitorea fallos en paralelo gracias a Redis, BullMQ y workers.
        </p>
      </section>
    </main>
  );
}
